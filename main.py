# ========== Import packages ========== #
import requests
import os
import streamlit as st

# ========== Get environment variables ========== #
nasa_api_key = os.getenv( "NASA_API_KEY" )

# ========== API request ========== #
response = requests.get( f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}" )

data = response.json()

data_title = data["title"]
data_description = data["explanation"]
data_image = data["url"]

# ========== Streamlit ========== #
st.title( data_title )
st.image( data_image)
st.write( data_description )