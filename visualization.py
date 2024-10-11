import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Create the choropleth map
def plot_map(data , geo_data):

    fig = px.choropleth_mapbox(data, 
                            geojson=geo_data, 
                            locations='location', 
                            featureidkey="properties.name",  # Adjust based on your GeoJSON structure
                            color='values', 
                            color_continuous_scale="Viridis",
                            mapbox_style="carto-positron",
                            zoom=5, 
                            center={"lat": 12.8797, "lon": 121.7740},  # Centered on the Philippines
                            opacity=0.5
                            )
    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Population",  # Label for the color bar
            titlefont=dict(size=20),  # Title font size
            tickfont=dict(size=16),  # Size of the color bar values
            thickness=30,
            len=1
            
        )
    )

    fig.update_layout( height=700,margin={"r": 0, "t": 0, "l": 0, "b": 0})
    
    return fig

#Create the Bar Chart 
def plot_bar(data, selected_year): 
    
    fig = go.Figure()
    
     # Add a single bar for the selected year
    fig.add_trace(
        go.Bar(
            y=data['location'],
            x=data['values'],
            hovertemplate="%{x}",
            name=selected_year,
            orientation="h",
        )
    )
    
    fig.update_layout(
        paper_bgcolor="#bcbcbc",
        plot_bgcolor="#f9e5e5",
        width=900,
        height=600,
        title=f"{selected_year} Data by Region",
        xaxis_title="Value",
        yaxis_title="Region"
    )

    # Display the chart
    return fig

    