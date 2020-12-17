import pandas as pd
import matplotlib.pyplot as plt 


#Class
class Line_Stacked_Bar: 
    
    def __init__(self, data, grocery_category, graph_type, x_label, y_label):
        self.data = data
        self.grocery_category = grocery_category
        self.graph_type = graph_type
        self.x_label = x_label
        self.y_label = y_label
        self.filtered_data = None
        self.x = None
        self.y = None
    
    def filter_split_graph(self):
        self.filter_category()
        self.xy_split()
        self.graph_plot()
        
    def filter_category(self):
        self.filtered_data = self.data[self.grocery_category]
        
    def xy_split(self):
        self.x=self.filtered_data.iloc[0]
        self.y=self.filtered_data.iloc[1]
    
    def graph_plot(self):
        if self.graph_type == 'Line Chart': 
            plt.plot(self.x, self.y, label=self.grocery_category)
        else: 
            plt.bar(self.x, self.y, label=self.grocery_category)


class Grouped_Bar:

    def __init__(self, data):
        self.data = data
        self.filtered_data = None

    def select_multiple_categories(self, column_filter, category_list):
        self.filtered_data = self.data.loc[self.data[column_filter].isin(category_list)]

    def pivot_plot(self, idx, clmns, vals, kind_plot):
        self.filtered_data.pivot(index=idx, columns=clmns, values=vals).plot(kind=kind_plot)


class Product_Group_Bar(Grouped_Bar):
    
    def __init__(self, data):
        super().__init__(data)
        self.reset_data = None

    def basic_filter(self, filter_column, filter_item):
        self.data = self.data[self.data[filter_column] == filter_item]
        
    def return_multiselect_list(self, column_name):
        return [i for i in self.data[column_name].unique()]
    
    def groupby_rename_reset(self, column_name_list, column_agg, aggregator, new_column_name):
        self.reset_data = self.data.groupby(column_name_list).agg({column_agg: aggregator}, inplace=True)
        self.reset_data.rename(columns={column_agg: new_column_name}, inplace=True)
        self.reset_data.reset_index(inplace=True)
        
    def select_multiple_categories(self, column_filter, category_list):
        self.filtered_data = self.reset_data.loc[self.reset_data[column_filter].isin(category_list)]

        