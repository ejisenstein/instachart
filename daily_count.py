#Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import pickle

from data_class import InstaClass

#Loading Line/Stacked Bar Datasets
pickle_off = open("pickle_jar/dow.pickle", "rb")
count_dow = pickle.load(pickle_off)
#Loading Grouped Bar Datasets
pickle_bar = open("pickle_jar/groupbar.pickle", "rb")
groupbar_df = pickle.load(pickle_bar)

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
graph_type = st.sidebar.selectbox('Type of Chart', ['Line', 'Stacked Bar Chart', 'Grouped Bar Chart'])
grocery_category = st.sidebar.multiselect('Category Filter By', categories, ['alcohol'])
num_of_categories = st.sidebar.selectbox('Number of Categories', [1, 2, 3])
legend_location = st.sidebar.selectbox('Location of Legend', ['upper left', 'upper center', 'upper right'])

#x axis/y axis variable names
x_label = 'Day of Week'
y_label = 'Count'

#This needs to be turned into an if/else statement, grouped bar chart has a different structure https://stackoverflow.com/questions/42128467/matplotlib-plot-multiple-columns-of-pandas-data-frame-on-the-bar-chart
#For loop to create plotting visualization. Perhaps an iterative loops to merge/join individual columns together
if graph_type != 'Grouped Bar Chart': 
    total_instance_list = [f'instance_{i}' for i in range(num_of_categories)]
    for num, i in enumerate(total_instance_list):
        i = InstaClass(count_dow, grocery_category[num], graph_type, x_label, y_label)
        i.filter_category()
        i.xy_split()
        i.graph_plot()
else: 
    filt_group_df = groupbar_df.loc[groupbar_df['department'].isin(grocery_category)]
    filt_group_df.pivot(index='order_dow', columns='department', values='count').plot(kind='bar')
    
#Matplotlib creation
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend(loc=legend_location)
st.pyplot(plt)
