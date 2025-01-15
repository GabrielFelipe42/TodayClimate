import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    print("API_KEY not found. Ensure .env file is set up correctly.")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str, units: str = "metric"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
    }
    print(f"Requesting weather data with params: {params}")
    response = requests.get(BASE_URL, params=params)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Unauthorized. Check if the API_KEY is correct.")
    else:
        print(f"Unexpected error: {response.text}")
    return {"error": f"Failed to fetch weather data. Status code: {response.status_code}"}
