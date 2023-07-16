# Script to convert JSON file from OpenWeather containing list of city info to a numpy array of just city IDs.
# This will make it easy to reference any city ID randomly on an API call. The JSON may be updated from time to time
# so it's probably a good idea to download a fresh copy from the site and run this script every so often to update
# the list. Latest curl address as of 05/23/2021: http://bulk.openweathermap.org/sample/city.list.json.gz
# Link to page with full list of downloadable files: http://bulk.openweathermap.org/sample/

# Import the relevant libraries
import json
import requests
import numpy as np
from numpy import save
from numpy import load

# Pull a current version of the city list
cityZipLink = "http://bulk.openweathermap.org/sample/city.list.json.gz"
currentCities = requests.get(cityZipLink)


# Open the file and load JSON contents to 'cities' object
with open("/home/jovyan/Personal/PassGen/wthrdata/citylist.json",'r') as cities_file:
    cities = json.load(cities_file)

# Create an empty list to populate with IDs
city_id_list = []

# Loop through each of the city records and just return the ID number, appending each ID to the list
for city in cities:
    city_id_list.append(city['id'])

# Convert the list to a numpy array
city_array = np.array(city_id_list)

# Save array as .npy for fast loading
save('CityIdArray.npy', city_array)

