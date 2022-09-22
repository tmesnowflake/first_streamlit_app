# Streamlit app 
import streamlit as sl
import pandas as pd 

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

sl.title('Parents new healthy dinner')

sl.header('Breakfast Favourites')
sl.text('🥣 Omega3 & Blueberry Waffles')
sl.text('🥗 Kale, Spinach & rocket smoothie')
sl.text('🐔 Boiled Free Range egg')
sl.text('🥑 Avo on toast')

sl.header('Build your own smoothie')
sl.multiselect ('Pick your fruit: ', list(my_fruit_list['Fruit']), ['Avocado', 'Strawberries'])

sl.dataframe(my_fruit_list[my_fruit_list['Fruit', 'Calories']])
