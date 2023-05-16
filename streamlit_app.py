import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach, and Rocket Smoothie')
streamlit.text('🐔Hard - Boiled Eggg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 

# Display the table on the page.

#create the repeatable code block called a function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalised

#New Section
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get infor.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlist.error()
#streamlit.write('The user entered ', fruit_choice)


#streamlit.text(fruityvice_response.json())

streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','choco')
streamlit.write('The user entered ', add_my_fruit)

streamlit.write('thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
