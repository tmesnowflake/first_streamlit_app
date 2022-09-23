# Streamlit app 
import streamlit as sl
import pandas as pd 
import requests

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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
sl.text(fruityvice_response.json())
