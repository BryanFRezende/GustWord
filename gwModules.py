import json
import requests
import numpy as np
from numpy import load
from datetime import datetime

class emptyWeathArray:
    def __init__(self):
        self.array = {
            
            'coord': {
                'lon': None, 
                'lat': None
            }, 
            
            'weather': [
                {
                    'id': None, 
                    'main': None, 
                    'description': None, 
                    'icon': None
                }
            ], 
            
            'base': None, 
            
            'main': {
                'temp': None, 
                'feels_like': None, 
                'temp_min': None, 
                'temp_max': None, 
                'pressure': None, 
                'humidity': None
            }, 
            
            'visibility': None, 
            
            'wind': {
                'speed': None, 
                'deg': None
            }, 
            
            'clouds': {
                'all': None
            }, 
            
            'dt': None, 
            
            'sys': {
                'type': None, 
                'id': None, 
                'country': None, 
                'sunrise': None, 
                'sunset': None
            }, 
            
            'timezone': None, 
            
            'id': None, 
            
            'name': None, 
            
            'cod': None
        }
        


def randCityArray(cityIDarray, numberOfCities):
    if numberOfCities == 1:
        randomCity = int(np.random.choice(cityIDarray))
        return randomCity

    elif numberOfCities > 1:
        arrayOfCities = np.empty(0)
        for i in range(0,numberOfCities):
            randomCity = int(np.random.choice(cityIDarray))
            np.append(arrayOfCities, randomCity)
        return arrayOfCities

    else:
        raise ValueError('Enter an integer value greater than 0 for the second parameter.')



def getCityWeather(cityID, arrayORstring, appID):
    if arrayORstring == 'array':
        requestArray = []
        for element in cityID:
            requestString = f'http://api.openweathermap.org/data/2.5/weather?id={element}&appid={appID}'
            weatherJSON = requests.get(requestString)
            requestArray.append(weatherJSON.json())
        return requestArray
    
    elif arrayORstring == 'string':
        requestString = f'http://api.openweathermap.org/data/2.5/weather?id={cityID}&appid={appID}'
        weatherJSON = requests.get(requestString)
        return weatherJSON.json()
    
    else:
        raise TypeError('Must enter "array" or "string" as second parameter.')



def allCities(cityIDarray, appID):
    allWeather = getCityWeather(cityIDarray, "array", appID)

    dtime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    saveName = f"All_Cities_Weather_Data_{dtime}.csv"
    try:
        with open(saveName, "x") as writeFile:
            json.dump(allWeather, writeFile)

    except FileExistsError:
        print("Filename already exists. Try running script again or report error to GitHub page.")

    return allWeather


def getAppID():
    with open('.apikey', 'r', encoding="utf-8") as f:
        appid = f.readlines()[1].rstrip()
    return appid
