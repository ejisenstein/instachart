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
st.title('Instachart')

#Paragraph explaining what this dashboard does
st.write('Instachart is a dynamic visualization of the [Instachart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis) dataset. You can adjust the visualization through the sidebar as a  line chart, bar chart, or grouped bar chart. You can view as many grocery categories as you want, organized by day of the week (unfortuntately the dataset did not specify which numbers refer to which day)')

#Different categories to filter instacart orders
categories = ['alcohol', 'babies', 'bakery', 'beverages', 'breakfast',
 'bulk', 'canned goods', 'dairy eggs', 'deli', 'dry goods pasta',
 'frozen', 'household', 'international', 'meat seafood', 'missing',
 'other', 'pantry', 'personal care', 'pets', 'produce', 'snacks']

#Select Box
graph_type = st.sidebar.selectbox('Type of Chart', ['Line', 'Stacked Bar Chart', 'Grouped Bar Chart'])
grocery_category = st.sidebar.multiselect('Category Filter By', categories, ['alcohol'])
# num_of_categories = st.sidebar.selectbox('Number of Categories', [1, 2, 3])
legend_location = st.sidebar.selectbox('Location of Legend', ['upper left', 'upper center', 'upper right'])

#x axis/y axis variable names
x_label = 'Day of Week'
y_label = 'Count'

#Grouped Bar Chat for referencehttps://stackoverflow.com/questions/42128467/matplotlib-plot-multiple-columns-of-pandas-data-frame-on-the-bar-chart
#If/Else statement determining whether its a grouped bar chart vs. stacked or line chart. Grouped Bar charts require a for loop. 
if graph_type != 'Grouped Bar Chart': 
    total_instance_list = [f'instance_{i}' for i in range(len(grocery_category))]
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

st.write('This application was created by [Evan Isenstein](https://github.com/ejisenstein/) using streamlit. He enjoys reading history books, watching the Tennessee Titans, and listening to classic rock.')