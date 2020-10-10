import json
from botocore.vendored import requests
import datetime

def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["city"]
    
    r = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": city , "appid":"749b69174a2c1a0d0a282fbdc642e701"} )
    data = r.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_degree = data["wind"]["deg"]
    sunrise = datetime.datetime.fromtimestamp(int(data["sys"]["sunrise"])).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(int(data["sys"]["sunset"])).strftime('%Y-%m-%d %H:%M:%S')
    
    output = 'Weather Description: {description}, Temperature: {temperature} K, Pressure: {pressure} hPa, Humidity: {humidity}%, Wind speed: {wind_speed} m/s, Wind degree: {wind_degree} degrees, Sunrise time: {sunrise}, Sunset time: {sunset}'.format(description=description, temperature=temperature, pressure=pressure, humidity=humidity, wind_speed=wind_speed, wind_degree=wind_degree, sunrise=sunrise, sunset=sunset)
    
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": output
            }
        }
    }