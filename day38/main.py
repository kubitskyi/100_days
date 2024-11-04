import os
import requests
import datetime
from dotenv import load_dotenv


load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 1.75
AGE = 29

exercise_text = input(">>>")

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheets_endpoint = os.getenv('SHEETY_ENDPOINT')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_headers={
    "Authorization": f"Basic {SHEETY_TOKEN}"
}
exercise_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_body , headers=headers)
exercise_json = exercise_response.json()

date_time_now = datetime.datetime.now()

for exercise in exercise_json["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": date_time_now.strftime("%d/%m/%Y"),
                "time": date_time_now.strftime("%X"),
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise["nf_calories"]
            }
        }

sheet_response = requests.post(url=sheets_endpoint, headers=sheety_headers, json=sheet_inputs)

print(sheet_response.text)