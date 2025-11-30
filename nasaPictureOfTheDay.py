import requests
import os
from dotenv import load_dotenv

load_dotenv()


day = input("Enter a day for nasa picture of the day: (DD) ")
month = input("Enter a month for nasa picture of the day: (MM) ")
year = input("Enter a year for nasa picture of the day: (YYYY) ")

formatted_Date = f"{year}-{month}-{day}"

url = "https://api.nasa.gov/planetary/apod"
api_key = os.getenv("NASA_API_KEY")

params = {
    "api_key" : api_key,
     "date" : formatted_Date
}

response = requests.get(url, params = params)
data = response.json()

# print(data) This API returns a dict object so I cannot iterate over it like in weatherAPI cause there was a list inside of dict

# Gotta watch out for the data that the API returns
print(response)
for key, value in data.items():
    print(f"{key.upper():15} : {value}")
