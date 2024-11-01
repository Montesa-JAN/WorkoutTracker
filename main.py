import requests
from datetime import datetime
import os

WEIGHT_KG = 55
HEIGHT_CM = 175
AGE = 22
GENDER = "Male"

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

NUTRITIONIX_ENDPOINT = "NUTRITIONIX_ENDPOINT"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

user_input = input("Tell me which exercises you did: ")

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

bearer_header = {
    "Authorization": TOKEN,
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
data = response.json()

today_now = datetime.now().strftime("%x")
time_now = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    exercise_data = {
        "workout": {
            "date": today_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(SHEETY_ENDPOINT, json=exercise_data, headers=bearer_header)

print(sheety_response)
