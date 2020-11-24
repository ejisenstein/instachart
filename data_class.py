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
        fig, ax = plt.subplots()
        if self.graph_type == 'Line': 
            ax.plot(self.x, self.y)
        else: 
            ax.bar(self.x, self.y)
        ax.set(xlabel=self.x_label, ylabel=self.y_label,
               title=f'{self.y_label} of {self.grocery_category}')
        return fig, ax
        
