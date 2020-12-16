#Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import pickle

from data_class import Line_Stacked_Bar, Grouped_Bar, Product_Group_Bar

#Loading Line/Stacked Bar Datasets
pickle_off = open("pickle_jar/dow_two.pickle", "rb")
count_dow = pickle.load(pickle_off)
#Loading Grouped Bar Datasets
pickle_bar = open("pickle_jar/groupbar_two.pickle", "rb")
groupbar_df = pickle.load(pickle_bar)
#Department Grouped Bar
#Filter By Product
pickly = open("pickle_jar/brine/dgp_brine.pickle", "rb")
dep_group_bar_df = pickle.load(pickly)
#Filter By Hour of Day
kosher = open("pickle_jar/brine/hod_gb_brine.pickle", "rb")
hod_df = pickle.load(kosher)

#Title of Website
st.title('Instachart')

#Paragraph explaining what this dashboard does
st.write('Instachart is a dynamic visualization of the [Instachart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis) dataset. You can adjust the visualization through the sidebar as a  line chart, bar chart, or grouped bar chart. You can view as many grocery categories as you want, organized by day of the week (unfortuntately the dataset did not specify which numbers refer to which day)')

#Different categories to filter instacart orders
categories = ['alcohol', 'babies', 'bakery', 'beverages', 'breakfast',
 'bulk', 'canned goods', 'dairy eggs', 'deli', 'dry goods pasta',
 'frozen', 'household', 'international', 'meat seafood', 'missing',
 'other', 'pantry', 'personal care', 'pets', 'produce', 'snacks']

#x axis/y axis variable names
x_label = 'Day of Week'
y_label = 'Count'

#Select Box 1
graph_type = st.selectbox('Type of Chart', ['Line Chart', 'Stacked Bar Chart', 'Grouped Bar Chart'])
if graph_type == 'Grouped Bar Chart': 
    type_gb_chart = st.selectbox('Values for Grouped Bar Chart', ['Category', 'Product with Day of Week', 'Product with Hour of Day'])


grocery_category_one = st.sidebar.multiselect('1. Category Filter By', categories, ['alcohol'])
# num_of_categories = st.sidebar.selectbox('Number of Categories', [1, 2, 3])
legend_location = st.sidebar.selectbox('1. Location of Legend', ['upper left', 'upper center', 'upper right'])


#Grouped Bar Chat for referencehttps://stackoverflow.com/questions/42128467/matplotlib-plot-multiple-columns-of-pandas-data-frame-on-the-bar-chart
#If/Else statement determining whether its a grouped bar chart vs. stacked or line chart. Grouped Bar charts require a for loop. 
if graph_type != 'Grouped Bar Chart': 
    total_instance_list = [f'instance_{i}' for i in range(len(grocery_category_one))]
    for num, i in enumerate(total_instance_list):
        i = Line_Stacked_Bar(count_dow, grocery_category_one[num], graph_type, x_label, y_label)
        i.filter_split_graph()
elif type_gb_chart == 'Category': 
    i = Grouped_Bar(groupbar_df)
    i.select_multiple_categories('department', grocery_category_one)
    i.pivot_plot('order_dow', 'department', 'count', 'bar')
elif type_gb_chart == 'Product with Day of Week':
    i = Product_Group_Bar(dep_group_bar_df)
    #Custom Sidebar for Product Name Filter
    product_category = st.sidebar.multiselect('2. Product Filter By', i.return_multiselect_list('product_name'))
    
    i.groupby_rename_reset(['product_name', 'order_dow'], 'order_id', 'count', 'count')
    i.select_multiple_categories('product_name', product_category)
    i.pivot_plot('order_dow', 'product_name', 'count', 'bar')
elif type_gb_chart == 'Product with Hour of Day':
    x_label = 'Hour of the Day'
    dow = st.sidebar.selectbox('DOW Filter By', [0, 1, 2, 3, 4, 5, 6])
    i = Product_Group_Bar(hod_df)
    i.basic_filter('department', grocery_category_one)
    i.basic_filter('order_dow', dow)
    
    #Custom Sidebar for Product Filter
    product_category = st.sidebar.multiselect('2. Product Filter By', i.return_multiselect_list('product_name'))
    
    i.groupby_rename_reset(['order_hour_of_day','product_name'], 'order_id', 'count', 'count')
    i.select_multiple_categories('product_name', product_category)
    i.pivot_plot('order_hour_of_day', 'product_name', 'count', 'bar')

    
    
#Matplotlib creation
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend(loc=legend_location)
st.pyplot(plt)

st.write('This application was created by [Evan Isenstein](https://github.com/ejisenstein/) using streamlit. He enjoys reading history books, watching the Tennessee Titans, and listening to classic rock.')
