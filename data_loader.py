import json
import streamlit as st
import pandas as pd
import re
# Will handle the philippines geographic data structure
def load_geojson(): 
    # Load the GeoJSON file
    with open('Population Dataset/PHRegions.json', 'r') as f:
        geo_data = json.load(f)
    return geo_data
# def load_province_geojson(): 
def load_geojson_province():
    with open('Population Dataset/PH_MuniDist_Simplified.json', 'r') as f:
        geo_data = json.load(f)
    return geo_data

    
def load_population(selected_year): 
    population = pd.read_csv('Population Dataset/Luzon-Region-Population_Cleaned.csv')
    df = pd.DataFrame(population)
    
    # change location name of MIMAROPA to Mimaropa only 
    df.loc[df['Name'] == 'MIMAROPA', 'Name'] = 'Mimaropa'
    ''' 
    Clean Data
    - Change  Selected Year or Population census from FLOAT to Object
    '''
    df[selected_year] = df[selected_year].str.replace(',', '').astype(float)
    # initializing the requested year of population and name of region 
    data = {'region': df['Name'].tolist(), "values": df[selected_year].tolist()}
    return data

def load_luzon_province(selected_year): 
    # Get the data population
    provinces = pd.read_csv('Population Dataset/Luzon-Province-Population_Cleaned.csv')
     
    # Convert Selected Year to Float
    provinces[selected_year] = provinces[selected_year].str.replace(',', '').astype(float)
    # Remove parentheses on names 
    provinces['Name'] = provinces['Name'].apply(lambda x: re.sub(r'\s*\(.*?\)\s*', '', x).strip())
     
    return provinces
# def load_luzon_province(selected_province): 
#     # Acuqire the data
#     provinces = pd.read_csv('Population Dataset/Luzon-Province-Population_Cleaned.csv')
#     # Instantiate the Province Column and current province
#     df['Province'] = pd.NA
#     # Current province will be the value of the province in the iteration
#     current_province = None
#     for index,row  in df.iterrows(): 
#         if row['Status'] == 'Province': 
#             current_province = row['Name']
#         df.at[index, 'Province'] = current_province
#     df = pd.DataFrame(provinces)
#     return df





    
    
    