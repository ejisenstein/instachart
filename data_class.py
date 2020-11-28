import pandas as pd
import matplotlib.pyplot as plt 


#Class
class InstaClass: 
    
    def __init__(self, data, grocery_category, graph_type, x_label, y_label):
        self.data = data
        self.grocery_category = grocery_category
        self.graph_type = graph_type
        self.x_label = x_label
        self.y_label = y_label
        self.filtered_data = None
        self.x = None
        self.y = None
        
    def filter_category(self):
        self.filtered_data = self.data[self.grocery_category]
        
    def xy_split(self):
        self.x=self.filtered_data.iloc[0]
        self.y=self.filtered_data.iloc[1]
    
    def graph_plot(self):
        if self.graph_type == 'Line': 
            plt.plot(self.x, self.y, label=self.grocery_category)
        else: 
            plt.bar(self.x, self.y, label=self.grocery_category)
