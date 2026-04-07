import requests

city = input("Enter city: ")

api_key = input("Enter API key: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

r = requests.get(url)

if r.status_code == 200:
    data = r.json()

    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    description = data["weather"][0]["description"]

    print("Weather:", description)
    print("Temperature:", round(temp_celsius, 2), "°C")
else:
    print("Error:", r.status_code)
    print(r.text)