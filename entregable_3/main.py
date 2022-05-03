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

from heapq import nlargest
from locale import currency
import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter()

class TableOperator:
   
    current_data_frame = None
    pd_columns_dict = None
    pd_datetime_df = None
    def __init__(self):
        self.pd_columns_dict = dict()

    def parse_csv(self, filename, *args):
        self.current_data_frame = pd.read_csv(filename, encoding='ISO-8859=1')
        self.pd_datetime_df = self.current_data_frame.copy()
        self.pd_datetime_df['Year'] = pd.to_datetime((self.current_data_frame.groupby('City').head()['Year']), format='%Y')
        self.pd_datetime_df.set_index( self.pd_datetime_df['Year'])
        for column in args:
            self.pd_columns_dict[column] = self.current_data_frame.loc[:,column]
            
    def split_column_in_two(self, split_var, index, data_name_a, data_name_b, index_split=[1,0]) -> pd.DataFrame: 
        
        to_split_val = np.char.split(np.array([ to_split for to_split in self.pd_columns_dict[index] ]), ', ')
        a_array = np.array([val_a[index_split[0]] for val_a in to_split_val])
        b_array = np.array([val_b[index_split[1]] for val_b in to_split_val])
        data_set = pd.DataFrame({data_name_a: a_array, data_name_b: b_array})
        
        return data_set 

    def count_values_in_column(self, data_frame, columns) -> pd.DataFrame:
        df =  data_frame.groupby(columns).count()
        return df

    def display_split(self):
        pp.pprint(self.split_column_in_two(',', 'Athlete', 'Name', 'LastName'))


    def display_top_medal_country(self):
        pp.pprint(self.count_values_in_column(self.current_data_frame, ['Country']).sort_values('Medal', ascending=False).head(10)['Medal'])
        pp.pprint(self.count_values_in_column(self.current_data_frame, ['Country']).sort_values('Medal', ascending=False).head(1)['Medal'])

    def display_medals_year_males(self):
        year_males = self.current_data_frame
        year_males = year_males[year_males['Event_gender'] == 'M']  
        pp.pprint(to.count_values_in_column(year_males, 'Year')['Athlete'])

to = TableOperator()
to.parse_csv('Summer-Olympic-medals-1976-to-2008.csv', 'Athlete', 'Event')

# Year converted to data index
pp.pprint(to.pd_datetime_df)

# Name splitting into 2 columns
to.display_split()
# Display the top 10 and Top country by medals
to.display_top_medal_country()
# Display Medals by Male gender per year
to.display_medals_year_males()



