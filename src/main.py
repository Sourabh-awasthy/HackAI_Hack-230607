import requests
from uagents import Agent
import os
from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={WEATHER_API_KEY}"

class Temperature:
    def temp_at_loc():
        loc= requests.get(WEATHER_API_URL)
        data = loc.json()
        temp= data['main']['temp'] - 273.15
        print(temp)
        return temp



class TemperatureAlertAgent(Agent, Temperature ):
    def __init__(self, name, location, min_temp, max_temp):
        super().__init__(name=name)
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp

    def check_temperature(self):
        try:
            temperature= Temperature.temp_at_loc()

            if temperature is not None:
                if temperature < self.min_temp:
                    self.send_alert(f"Temperature in {self.location} is below {self.min_temp}°C.")
                elif temperature > self.max_temp:
                    self.send_alert(f"Temperature in {self.location} is above {self.max_temp}°C.")
                else:
                    print(f"Temperature in {self.location} is within the desired range.")
            else:
                print("Temperature data not available in the API response.")

        except Exception as e:
            print(f"Error fetching temperature data: {str(e)}")

    def send_alert(self, message):
        # Replace this with your preferred method of sending alerts (e.g., email, SMS)
        print(f"ALERT: {message}")



if __name__ == "__main__":
    agent = TemperatureAlertAgent(
        name="MyTemperatureAgent",
        location="YourLocation",
        min_temp=20,  # Set your preferred minimum temperature
        max_temp=30,  # Set your preferred maximum temperature
    )

    while True:
        agent.check_temperature()
