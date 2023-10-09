import requests
from uagents import Agent
import os
import json
from dotenv import load_dotenv
from main import Temperature
load_dotenv()

class TemperatureAlertAgent(Agent, Temperature ):
    def __init__(self, name, location, min_temp, max_temp):
        super().__init__(name=name)
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp

    def check_temperature(self):
        try:
            temperature= Temperature
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
