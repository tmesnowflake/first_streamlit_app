# Streamlit app 
import streamlit as sl
import pandas as pd 
import requests
import snowflake.connector

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
sl.title('Parents new healthy dinner')

sl.header('Breakfast Favourites')
sl.text('🥣 Omega3 & Blueberry Waffles')
sl.text('🥗 Kale, Spinach & rocket smoothie')
sl.text('🐔 Boiled Free Range egg')
sl.text('🥑 Avo on toast')

sl.header('Build your own smoothie')
fruit_selected  = sl.multiselect ('Pick your fruit: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

sl.dataframe(fruit_to_show)



sl.header('Fruit Advice! you fkn noobs')
fruit_choice = sl.text_input('What Fruit do you want to know about?', 'kiwi')
sl.write(fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#sl.text(fruityvice_response.json())

fv_normalised = pd.json_normalize(fruityvice_response.json())
sl.dataframe(fv_normalised)


my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
sl.text("Hello from Snowflake:")
sl.text(my_data_row)
