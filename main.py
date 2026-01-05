# ========== Import packages ========== #
import requests
import os

# ========== Get environment variables ========== #
nasa_api_key = os.getenv( "NASA_API_KEY" )

# ========== API request ========== #
response = requests.get( f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}" )




# ========== Test ========== #

print( response.json() )