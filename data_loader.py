import json
import streamlit as st
import pandas as pd

# Will handle the philippines geographic data structure
def load_geojson(): 
    # Load the GeoJSON file
    with open('PHRegions.json', 'r') as f:
        geo_data = json.load(f)
    return geo_data

    
def load_population(selected_year): 
    population = pd.read_csv('Population Dataset/Luzon-Regions-Population.csv')
    df = pd.DataFrame(population)
    ''' 
    Clean Data
    - Dropping missing values 
    '''
    df.dropna(subset=['Population Census 1990'], inplace=True)
    df.drop(df.columns[df.columns.str.contains('^Unnamed')], axis=1, inplace=True)
    data = {'region': df['Name'].tolist(), "values": df[selected_year].tolist()}
    return data

def load_luzon_province(selected_province): 
    provinces = pd.read_csv('Population Dataset/Luzon-Regions-Municipality.csv')
    df = pd.DataFrame(provinces)
    




    
    
    