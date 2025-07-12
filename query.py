import requests
import pandas as pd

#fetching data from the backend

def queryWeatherData():
    url = 'http://127.0.0.1:5000/api/name'
    response = requests.get(url)

    data = response.json()
    return data
df = queryWeatherData()

