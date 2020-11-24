#Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import pickle

from data_class import InstaClass

#Loading Pickled DataSets
pickle_off = open("pickle_jar/dow.pickle", "rb")
count_dow = pickle.load(pickle_off)

#Title of Website
st.title('Instacart Interactive DataSets')

#Paragraph explaining what this dashboard does
st.write('Rather than having one graph, why not have multiple?')

#Different categories to filter instacart orders
categories = ['alcohol', 'babies', 'bakery', 'beverages', 'breakfast',
 'bulk', 'canned goods', 'dairy eggs', 'deli', 'dry goods pasta',
 'frozen', 'household', 'international', 'meat seafood', 'missing',
 'other', 'pantry', 'personal care', 'pets', 'produce', 'snacks']

#Select Box
graph_type = st.sidebar.selectbox('Type of Chart', ['Line','Bar'])
# multiple_line = st.sidebar.selectbox('')
grocery_category = st.selectbox('Category Filter By', categories)

#x axis/y axis variable names
x_label = 'day of week'
y_label = 'count'

#Class instantiation
s1 = InstaClass(count_dow, grocery_category, graph_type, x_label, y_label)

s1.filter_category()
s1.xy_split()
fig, ax = s1.graph_plot()
st.pyplot(fig)





#options = st.multiselect(
#'What are your favorite colors',
#  ['Green', 'Yellow', 'Red', 'Blue'],
#  ['Yellow', 'Red'])


