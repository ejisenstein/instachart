#Imports
import streamlit as st
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt 
import pickle

#Loading Pickled DataSets
pickle_off = open("pickle_jar/dow.pickle", "rb")
count_dow = pickle.load(pickle_off)

#Begin actual
st.title('Instacart Interactive DataSets')

st.write('Rather than having one graph, why not have multiple?')

categories = ['alcohol', 'babies', 'bakery', 'beverages', 'breakfast',
 'bulk', 'canned goods', 'dairy eggs', 'deli', 'dry goods pasta',
 'frozen', 'household', 'international', 'meat seafood', 'missing',
 'other', 'pantry', 'personal care', 'pets', 'produce', 'snacks']

graph_type = st.sidebar.selectbox('Type of Chart', ['Line','Bar'])
grocery_category = st.selectbox('Category Filter By', categories)


#options = st.multiselect(
#'What are your favorite colors',
#  ['Green', 'Yellow', 'Red', 'Blue'],
#  ['Yellow', 'Red'])



def get_grocery_category(name):
    data = None
    data = count_dow[name]  
    return data
#   if name != 'all':
#         
#     else: 
#         data = count_dow

def type_of_chart(graph_type):
    filtered_data = get_grocery_category(grocery_category)
    if graph_type == 'Line':
        fig, ax = plt.subplots()  
        ax.plot(filtered_data.iloc[0],filtered_data.iloc[1])
        ax.set(xlabel='day of week', ylabel='count',
        title=f'Count of {grocery_category} items vs. day of week')
    else: 
        fig, ax = plt.subplots()  
        ax.bar(filtered_data.iloc[0],filtered_data.iloc[1])
        ax.set(xlabel='day of week', ylabel='count',
        title=f'Count of {grocery_category} items vs. day of week')
    return fig, ax
       
fig, ax = type_of_chart(graph_type)

st.pyplot(fig)
