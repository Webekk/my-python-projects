import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "http://api.weatherapi.com/v1/forecast.json"
city = "Cracow"
weather_key = os.getenv("WEATHER_API_KEY")

params = {
    "key": weather_key,
    "q": city,
    "days": 2,      # dziś + jutro
    "lang": "pl",
    "aqi": "no",
    "alerts": "no"
}

response = requests.get(url, params=params)
data = response.json()

print(data)

# --- PODSTAWOWE INFO ---
print(f"\nPrognoza pogody dla: {city}")
print(f"Aktualny czas: {data['location']['localtime']}")
print(f"Aktualna temperatura: {data['current']['temp_c']} °C")
print(f"Odczuwalna: {data['current']['feelslike_c']} °C")
print("-" * 40)

# --- JUTRZEJSZA PROGNOZA GODZINOWA ---
tomorrow = data["forecast"]["forecastday"][1]   # index 1 = jutro

print(f"\nPrognoza na jutro: {tomorrow['date']}\n")

for hour in tomorrow["hour"]:
    time = hour["time"]
    temp = hour["temp_c"]
    feels = hour["feelslike_c"]
    condition = hour["condition"]["text"]

    print(f"{time} | Temp: {temp}°C | Odczuwalna: {feels}°C | {condition}")
