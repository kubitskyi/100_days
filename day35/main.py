import os
from dotenv import load_dotenv
from twilio.rest import Client

import requests

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params ={
    "lat": 50.280820,
    "lon": 24.638330,
    "appid": weather_api_key,
    "cnt": 4,
}

will_rain = False
response = requests.get(OWN_ENDPOINT, params=weather_params)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
        
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)