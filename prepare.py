# tabular data manipulation
import numpy as np
import pandas as pd
# datetime utilities
from datetime import timedelta, datetime
# visualization
import matplotlib.pyplot as plt

# no yelling in the library
import warnings
warnings.filterwarnings("ignore")

def store_prep(df):
    
    # convert 'sale_date' column to datetime format
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y %H:%M:%S %Z')
    
    # plot the distribution of 'sale_amount' and 'item_price'
    df[['sale_amount', 'item_price']].hist()
    df.sale_amount.hist()
    plt.title('Distribution of Sale Amount')
    plt.xlabel('sale_amount')
    plt.ylabel('Count')
    plt.show()
    
    # plot the distribution of 'item_price'
    df.item_price.hist()
    plt.title('Distribution of Item Price')
    plt.xlabel('item_price')
    plt.ylabel('Count')
    plt.show()
    
    # set the index to 'sale_date'
    df = df.set_index('sale_date').sort_index()
    
    # add a 'month' column to dataframe
    df['month'] = df.index.month
    # add a 'day_of_week' column to dataframe
    df['day_of_week'] = df.index.day_name()
    # add 'sales_total' column to dataframe ('sales_total' = 'sale_amount' * 'item_price')
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def prepare_opsd(df):
    
    # convert 'Date' column to datetime format
    df.Date = pd.to_datetime(df.Date, format = '%Y-%m-%d')
    
    # plot the distribution of the variables
    df.hist(figsize=(10, 10))
    
    # set the index to 'Date'
    df = df.set_index('Date').sort_index()
    
    # add 'month' column to dataframe
    df['month'] = df.index.month
    # add 'year' column to dataframe
    df['year'] = df.index.year
    
    # fill any missing values
    df = df.fillna(value=0)
    
    return df

