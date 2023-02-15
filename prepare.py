#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


def prepare_store(df):
    '''
    This function takes in a dataframe and 
    prepares acquired store data for exploration '''
    
    # converts the sale_date column from an object to a datetime format
    df['sale_date'] = pd.to_datetime(df['sale_date'], infer_datetime_format=True)
    
    # creates a new column from the sale_date column with just the month name
    df['month'] = df['sale_date'].dt.month_name()
    
    # creates a new column from the sale_date column with just the day
    df['day_of_week'] = df['sale_date'].dt.day_name()
    
    # sets the date column as the index
    df = df.set_index('sale_date')
    
    # creates a new column by multiplying the sales total by the sale amoun to 
    # get the total price
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df


def prepare_power(df):
    '''
    This function takes in a dataframe and 
    prepares acquired german power data for exploration '''
    
    # converts the Date column from an object to a datetime format
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    
    # creates a new column from the Date column with just the month name
    df['month'] = df['Date'].dt.month_name()
    
    # creates a new column from the Date column with just the year
    df['year'] = pd.DatetimeIndex(df['Date']).year
    
    # sets the Date column as the index
    df = df.set_index('Date')
    
    # fills in all nan values with a zero
    df = df.fillna(0)
    
    return df

