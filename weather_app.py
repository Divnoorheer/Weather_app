import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def display_weather(data):
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]

    print(f"\n🌍 Weather in {location}, {country}")
    print(f"🌡 Temperature: {temp_c}°C")
    print(f"☁️ Condition: {condition}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_kph} kph")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)


