# Using a cat facts API, made a call all by myself without the help of any tutorial
import requests


url = "https://meowfacts.herokuapp.com/"

params = {
    "data": [
        "0",
    ],

}
response = requests.get(url, params=params)

data = response.json()

for cats in data['data']:
    print(cats)