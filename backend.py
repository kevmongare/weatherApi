import requests
from flask import Flask, jsonify #fot outputing json from the api
from flask_cors import CORS#for connection to frontend 
app = Flask(__name__)

CORS(app) 

@app.route("/api/weather")
def queryWeatherData():
    url = 'https://api.openweathermap.org/data/2.5/weather?' \
          'q=nairobi' \
          '&appid=c32170926bb267e9e09b323867c11c47&units' \
          '=metric'
    try:
        new_Weather = requests.get(url)
        new_Weather.raise_for_status()

        data =new_Weather.json()

        weatherData = {
            'Country':data['sys']['country'],
            'City':data['name'],
            'Main_Weather':data['weather'][0]['main'],
            'Weather':data['weather'][0]['description'],
            'Temperature':data['main']['temp']

        }
        return jsonify(weatherData)
        
    except requests.exceptions.HTTPError as http_error:
        print(f'Api connection error: {http_error}')
    return None



@app.route("/api/name")
def myName():
    name = {
        'firstname':'Kevin',
        'surname':'Karanja',
        'age': 25,
        'Address': 'Nairobi, Kenya'}
    return jsonify(name)

@app.route("/api/age")
def myAge():
    age = 25
    return jsonify(age)     
if __name__ == "__main__":
    app.run(debug=True)



# df =queryWeatherData()
# print(f'Expect the following dictionary{df}')

# # return None # fallback
# # # df = queryWeatherApi()

    
