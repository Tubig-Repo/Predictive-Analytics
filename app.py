import streamlit as st
import json
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import data_loader
import visualization
# Title for the Visualization
st.title("Population Density in the Philippines")
option_island = st.selectbox(
      "Select By Island",
      ("Luzon" , "Visayas", "Mindanao")
)
option_census_year = st.selectbox(
    "Select Population Census",
    ("Population Census 1990" , "Population Census 2000" , "Population Census 2010", "Population Census 2015", "Population Census 2020")
)
# Load Data
geo_data = data_loader.load_geojson()
population_data = data_loader.load_population(option_census_year)

# Create the choropleth map

fig = visualization.plot_map(data=population_data,geo_data=geo_data)

# Display the map in Streamlit
st.plotly_chart(fig)


