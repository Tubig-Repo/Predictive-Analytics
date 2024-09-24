import streamlit as st
import plotly.express as px


def plot_map(data , geo_data):
    # Create the choropleth map
    fig = px.choropleth_mapbox(data, 
                            geojson=geo_data, 
                            locations='region', 
                            featureidkey="properties.name",  # Adjust based on your GeoJSON structure
                            color='values', 
                            color_continuous_scale="Viridis",
                            mapbox_style="carto-positron",
                            zoom=5, 
                            center={"lat": 12.8797, "lon": 121.7740},  # Centered on the Philippines
                            opacity=0.5
                            )
    
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    
    return fig