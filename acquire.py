import pandas as pd
import requests
import os

def get_items():
    
    if os.path.isfile('items.csv'):
        
        df = pd.read_csv('items.csv', index_col=0)
        
    else:

        response = requests.get('https://python.zach.lol/api/v1/items')
        data = response.json()
        n = data['payload']['max_page']
    
        items_list = []

        for i in range(1, n+1):
            url = 'https://python.zach.lol/api/v1/items?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['items']
            items_list += page_items
        
        df = pd.DataFrame(items_list)
    
        df.to_csv('items.csv')
    
    return df

def get_stores():
    
    if os.path.isfile('stores.csv'):
        
        df = pd.read_csv('stores.csv', index_col=0)
        
    else:
    
        response = requests.get('https://python.zach.lol/api/v1/stores')
        data = response.json()
        n = data['payload']['max_page']
    
        stores_list = []

        for i in range(1, n+1):
            url = 'https://python.zach.lol/api/v1/stores?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['stores']
            stores_list += page_items
        
        df = pd.DataFrame(stores_list)
    
        df.to_csv('stores.csv')
    
    return df

def get_sales():
    
    if os.path.isfile('sales.csv'):
        
        df = pd.read_csv('sales.csv', index_col=0)
        
    else:
        
        response = requests.get('https://python.zach.lol/api/v1/sales')
        data = response.json()
        n = data['payload']['max_page']
    
        sales_list = []

        for i in range(1, n+1):
            url = 'https://python.zach.lol/api/v1/sales?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data['payload']['sales']
            sales_list += page_items
    
        df = pd.DataFrame(sales_list)
    
        df.to_csv('sales.csv')
        
    return df  

def merge_data():
    
    items = pd.read_csv('items.csv', index_col=0)
    stores = pd.read_csv('stores.csv', index_col=0)
    sales = pd.read_csv('sales.csv', index_col=0)
    
    combine1 = pd.merge(sales, stores, how='left', left_on='store', right_on='store_id').drop(columns='store')
    
    combined_df = pd.merge(combine1, items, how='left', left_on='item', right_on='item_id').drop(columns='item')
    
    combined_df.to_csv('combined_df.csv')
    
    return combined_df

def get_zach_data(name):
    
    if os.path.isfile(name + '.csv'):
        df = pd.read_csv(name + '.csv', index_col=0)
        
    else:
    
        url = 'https://python.zach.lol/api/v1/'
        response = requests.get(url + name)
        data = response.json()
        
        output = data['payload'][name]
    
        while data['payload']['next_page'] != None:
            response = requests.get(url + data['payload']['next_page'])
            data = response.json()
            output.extend(data['payload'][name])
        
        df = pd.DataFrame(output)
    
        df.to_csv(name + '.csv')
    
    return df

def get_opsd_germany():
    
    if os.path.isfile('opsd_germany.csv'):
        df = pd.read_csv('opsd_germany.csv', index_col=0)
        
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('opsd_germany.csv')
    return df


def csv_to_dataframe(url, key1, key2= None):
    '''
    Function to take in any url and keys and create a dataframe
    '''
    # Let's take an example url and make a get request
    response = requests.get(url)
    #create dictionary object
    data = response.json()
    if key2 != None:
        data_list = response.json()[key1][key2]
    else:
        data_list = response.json()[key1]
    df= pd.DataFrame(data_list)
    return df

def create_df_api_standard(url, key, item, name):
    '''
    Only for single page.
    prior to running this function need to know url and keys so as to specifiy which field within the data you 
    wish to create a DF on.
    '''
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[key][item])
    df.to_csv(name + '.csv')
    
    return df