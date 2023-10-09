import requests
from uagents import Agent
import os
import json
from dotenv import load_dotenv
load_dotenv()


class Temperature:
    @staticmethod
    def geo_location():
            city = "agra"
            state= "Uttar Pradesh" 
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
                    print(f"Latitude: {latitude}")
                    print(f"Longitude: {longitude}")
                else:
                    print("Location not found in the API response.")
            else:
                print("Unable to get location.")

            return latitude, longitude

        # map_link = f"https://www.openstreetmap.org/#map=18/{latitude}/{longitude}"
        # print(f"Latitude: {latitude:.6f}°, Longitude: {longitude:.6f}°")
        # print(f"Map Link: {map_link}")

    @staticmethod
    def get_weather_data(latitude, longitude):
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
        weather_data= requests.get(WEATHER_API_URL)
        if weather_data.status_code == 200:
            data= weather_data.json()
            temperature= data['main']['temp'] - 273.15
            print("Temp= {}", temperature)
            return temperature
        else:
            print("Error fetching weather data!")




# class TemperatureAlertAgent(Agent, Temperature ):
#     def __init__(self, name, location, min_temp, max_temp):
#         super().__init__(name=name)
#         self.location = location
#         self.min_temp = min_temp
#         self.max_temp = max_temp

#     def check_temperature(self):
#         try:
#             temperature= Temperature.get_weather_data()

#             if temperature is not None:
#                 if temperature < self.min_temp:
#                     self.send_alert(f"Temperature in {self.location} is below {self.min_temp}°C.")
#                 elif temperature > self.max_temp:
#                     self.send_alert(f"Temperature in {self.location} is above {self.max_temp}°C.")
#                 else:
#                     print(f"Temperature in {self.location} is within the desired range.")
#             else:
#                 print("Temperature data not available in the API response.")

#         except Exception as e:
#             print(f"Error fetching temperature data: {str(e)}")

#     def send_alert(self, message):
#         # Replace this with your preferred method of sending alerts (e.g., email, SMS)
#         print(f"ALERT: {message}")



if __name__ == "__main__":
    # agent = TemperatureAlertAgent(
    #     name="MyTemperatureAgent",
    #     location="YourLocation",
    #     min_temp=20,  # Set your preferred minimum temperature
    #     max_temp=30,  # Set your preferred maximum temperature
    # )

    # while True:
    #     agent.check_temperature()
    latitude, longitude = Temperature.geo_location()
    if latitude is not None and longitude is not None:
        print(f"Latitude: {latitude:.6f}°, Longitude: {longitude:.6f}°")

        # Get weather data based on the user's location
        temperature = Temperature.get_weather_data(latitude, longitude)
        if temperature is not None:
            print(f"Temperature: {temperature:.2f}°C")
        else:
            print("Unable to retrieve your location.")
