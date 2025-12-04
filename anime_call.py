import requests

resp = requests.get("https://nekos.best/api/v2/neko")
data = resp.json()
for item in data["results"]: # First I need to the result element
    for k, v in item.items(): # Then iterate over it with another for loop
        print(f"{k}: {v}")