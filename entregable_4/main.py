# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
# ---

from timeit import repeat
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pprint

pp = pprint.PrettyPrinter()
class TableOperator:

    csv_dataframe = ''
    operation_dataframe = ''
    def __init__(self):
        pass

    def parse_csv(self, filename):
        csv_dataframe = pd.read_csv(filename, encoding='ISO-8859=1')
        self.operation_dataframe = csv_dataframe.copy()
    
    def get_df_column_from_df(self, df, column_id) -> pd.DataFrame:
        return df[column_id]

    def show_histogram(self):
        plt.close()
        sns.set_style('whitegrid')
        plt.title('Salary Histogram')
        plt.xlabel('Salary')
        plt.ylabel('Employees')
        sns.histplot(self.get_df_column_from_df(self.operation_dataframe, 'Salary'))
        plt.show()
    
    def show_violin_plot(self):
        plt.close()
        
        sns.set_style('whitegrid')
        plt.title('Salary Violin Plot')
        sns.violinplot(x='Sex', y='Salary', hue='Sex', data=self.operation_dataframe)
        plt.show()
    
    def show_date_of_hire_plot(self):
        plt.close()
        plt.title('Date of Hire')
        hires = pd.to_datetime(self.operation_dataframe['DateofHire'])
        value_count = hires.value_counts()
        value_count.plot(use_index=True) 
        plt.show()

to = TableOperator()
to.parse_csv('HRDataset_v14.csv')
to.show_histogram()
to.show_violin_plot()
to.show_date_of_hire_plot()
