import requests

url = "https://potterapi-fedeperin.vercel.app/en/books"
params = {"index": 2}
response = requests.get(url, params=params)
book = response.json()
print(book)
