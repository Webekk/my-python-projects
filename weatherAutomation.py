# For this program I used the weatherapi.com, it's really cool and free so you can experiment
# This is my first API call, things are still a little complicated for me but i'm getting used to it
import requests
from dotenv import load_dotenv
import os
load_dotenv()
url = "http://api.weatherapi.com/v1/current.json"
city = "Cracow"
weather_key = os.getenv("WEATHER_API_KEY")
params = {
    "key" : weather_key,
    "q" : city,
    "days" : 14,
    "lang" : "pl",
    "solar" : "yes"
}

response = requests.get(url,params=params)
data = response.json()
#print(f"The 14 day weather forecast for {city}")

# for day in data["forecast"]["forecastday"]:
#     print(day["date"], "-", day["day"]["avgtemp_c"], "°C")
#     print(data["current"]["condition"]["text"])

#Showing the weather for the current city
print(data)
print(f"The weather forecast for {city}")
print(f"Current time in {city}: {data["location"]["localtime"]}")
print(f"Current temperature in {city}: {data["current"]["temp_c"]}°C")
