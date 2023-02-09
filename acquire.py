#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import requests

import os
import pandas as pd

def get_star_wars_data():
    '''
    This function reads the star wars data from 
    'https://swapi.dev/api/ site into a df.
    '''

    url = 'https://swapi.dev/api/people/'
    response = requests.get(url)
    data = response.json()
    people_df = pd.DataFrame(data['results'])
    while data['next'] != None:
        print(data['next'])
        response = requests.get(data['next'])
        data = response.json()
        people_df = pd.concat([people_df, pd.DataFrame(data['results'])], ignore_index = None)
    
    
    url = 'https://swapi.dev/api/planets/'
    response = requests.get(url)
    data = response.json()
    planets_df = pd.DataFrame(data['results'])
    while data['next'] != None:
        print(data['next'])
        response = requests.get(data['next'])
        data = response.json()
        planets_df = pd.concat([planets_df, pd.DataFrame(data['results'])], ignore_index = None)
    
    url = 'https://swapi.dev/api/starships/'
    response = requests.get(url)
    data = response.json()
    starships_df = pd.DataFrame(data['results'])
    while data['next'] != None:
        print(data['next'])
        response = requests.get(data['next'])
        data = response.json()
        starships_df = pd.concat([starships_df, pd.DataFrame(data['results'])], ignore_index = None)

    people_planets_df = people_df.append(planets_df, ignore_index=True)
    people_planets_starships_df = people_planets_df.append(starships_df, ignore_index=True)
    
    return people_planets_starships_df


def acquire_star_wars():
    '''
    This function reads in star wars data from the 
    https://swapi.dev/api/ site, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    
    if os.path.isfile('star_wars.csv'):
        
        # If csv file exists, read in data from csv file.
        people_planets_starships_df = pd.read_csv('star_wars.csv', index_col=0)
        
    else:

        #creates new csv if one does not already exist
        people_planets_starships_df = get_star_wars_data()
        people_planets_starships_df.to_csv('star_wars.csv')

    return people_planets_starships_df



def get_open_power_data():
    '''
    This function reads the open power data from 
    'https://raw.githubusercontent.com site into a df.
    '''
    
    open_power_df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    
    return open_power_df


def acquire_open_power():
    '''
    This function reads in open power data from the 
    https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv 
    site, writes data to a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('open_power.csv'):
        
        # If csv file exists, read in data from csv file.
        open_power = pd.read_csv('open_power.csv', index_col=0)
        
    else:

        #creates new csv if one does not already exist
        open_power = get_open_power_data()
        open_power.to_csv('open_power.csv')

    return open_power

