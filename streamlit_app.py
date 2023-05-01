import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach, and Rocket Smoothie')
streamlit.text('🐔Hard - Boiled Eggg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
