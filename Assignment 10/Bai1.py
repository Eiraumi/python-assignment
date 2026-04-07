import requests

url = "https://api.chucknorris.io/jokes/random"
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    print(data["value"])
else:
    print("Error")