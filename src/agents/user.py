from uagents import Agent, Context
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

agent = Agent(name="alice")


@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent {ctx.name} and my address is {ctx.address}.")


if __name__ == "__main__":
    agent.run()

from src.agents.response import TemperatureAlertAgent

class Temperature:
    @staticmethod
    def geo_location():
            city = "Jaipur"
            state= "Rajasthan" 
            country= "IN"
            latitude = None
            longitude = None
            LOCATION_API_KEY= os.getenv("LOCATION_API_KEY")
            LOCATION_API_URL= f"https://api.api-ninjas.com/v1/geocoding?city={city}&country={country}"
            location_data= requests.get(LOCATION_API_URL, headers={'X-Api-Key': LOCATION_API_KEY})
            if location_data.status_code == requests.codes.ok:
                api_response = json.loads(location_data.text)
                for location in api_response:
                    if (location.get("country") == country and location.get("state") == state and location.get("name").lower() == city.lower()):
                        latitude = location.get("latitude")
                        longitude = location.get("longitude")
                    break

                if latitude is not None and longitude is not None:
                    return latitude, longitude
                else:
                    print("Location not found in the API response.")
            else:
                print("Unable to get location.")
    
    @staticmethod
    def get_weather_data(latitude, longitude):
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
        weather_data= requests.get(WEATHER_API_URL)
        if weather_data.status_code == 200:
            data= weather_data.json()
            temperature= data['main']['temp'] - 273.15
            return temperature
        else:
            print("Error fetching weather data!")

def get_temp(): 
    latitude, longitude = Temperature.geo_location()
    if latitude is not None and longitude is not None:
            print(f"Latitude: {latitude:.6f}°, Longitude: {longitude:.6f}°")
    
            # Get weather data based on the user's location
            temperature = Temperature.get_weather_data(latitude, longitude)
            if temperature is not None:
                print(f"Temperature: {temperature:.2f}°C")
                return temperature
    else:
        print("Unable to retrieve your location.")


if __name__ == "__main__":
    agent = TemperatureAlertAgent(
        name="MyTemperatureAgent",
        location="YourLocation",
        min_temp=20,  # Set your preferred minimum temperature
        max_temp=30,  # Set your preferred maximum temperature
    )

    while True:
        agent.check_temperature()
    
