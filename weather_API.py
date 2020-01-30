import requests
import json

KEY = "be1ae457a890894c4854d1796e11012f"
city_name = ""

# url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}"

while True:
        city_name = input("enter city name: ").strip()
        if city_name == 'q':
                break
        params = {
        "city_name":city_name
        }
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}&units=metric"
        res = requests.get(url)
        res = json.loads(res.text)
        print(str(res['main']["temp"]) + " °C")