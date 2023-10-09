# import requests
# from uagents.setup import fund_agent_if_low
# from uagents.resolver import get_agent_address
# from uagents import Agent, Context
# from messages.basic import Message
# from messages.basic import Response
# import os
# import json
# from dotenv import load_dotenv
# # from main import Temperature
# load_dotenv()
# class Temperature:
#     @staticmethod
#     def geo_location():
#             city = input("Enter City: ")
#             state= input("Enter state: ")
#             country= input("Enter country: ")
#             latitude = None
#             longitude = None
#             LOCATION_API_KEY= os.getenv("LOCATION_API_KEY")
#             LOCATION_API_URL= f"https://api.api-ninjas.com/v1/geocoding?city={city}&country={country}"
#             location_data= requests.get(LOCATION_API_URL, headers={'X-Api-Key': LOCATION_API_KEY})
#             if location_data.status_code == requests.codes.ok:
#                 api_response = json.loads(location_data.text)
#                 for location in api_response:
#                     if (location.get("country") == country and location.get("state") == state and location.get("name").lower() == city.lower()):
#                         latitude = location.get("latitude")
#                         longitude = location.get("longitude")
#                     break

#                 if latitude is not None and longitude is not None:
#                     return latitude, longitude
#                 else:
#                     print("Location not found in the API response.")
#             else:
#                 print("Unable to get location.")

#     @staticmethod
#     def get_weather_data():
#         if Temperature.latitude is not None and Temperature.longitude is not None:
#             WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
#             WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
#             weather_data= requests.get(WEATHER_API_URL)
#             if weather_data.status_code == 200:
#                 data= weather_data.json()
#                 temperature= data['main']['temp'] - 273.15
#                 return temperature
#             else:
#                 print("Error fetching weather data!")
# class TemperatureAlertAgent(Agent, Temperature ):
#     def __init__(self, name, location, min_temp, max_temp):
#         super().__init__(name=name)
#         self.location = location
#         self.min_temp = min_temp
#         self.max_temp = max_temp

#     def check_temperature(self):
#         try:
#             temperature= Temperature
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

# server = Agent(
#     name="agent server",
#     port=8001,
#     seed="agent server secret phrase",
#     endpoint=["http://127.0.0.1:8001/submit"],
# )
# fund_agent_if_low(server.wallet.address())


# @server.on_message(model=Message)
# async def message_handler(ctx: Context, sender: str, msg: Message):
#     ctx.logger.info(f"Received message from {sender}: {msg.longitude}")

#     # send the response
#     await ctx.send(sender, Message(msg="Hello there user."))

# @server.on_message(model=Message)
# async def message_handler(ctx: Context, sender: str, msg: Message):
#     ctx.logger.info(f"Received message from user: {msg.city}")

    # Create a response message with the required fields
#     response_msg = Response(
#         Temp=14.6,
#         msg="Hello there user."
#     )

#     # send the response
#     await ctx.send(sender, response_msg)

# if __name__ == "__main__":
#     server.run()


import requests
from dotenv import load_dotenv
load_dotenv()
from uagents.setup import fund_agent_if_low
from uagents.resolver import get_agent_address
from uagents import Agent, Context
import os
import json
from messages.basic import Message
from messages.basic import Response

class Temperature:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country
        self.latitude = None
        self.longitude = None

    @staticmethod
    def geo_location(city, state, country):
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
            weather_data = requests.get(WEATHER_API_URL)
            if weather_data.status_code == 200:
                data = weather_data.json()
                temperature = data['main']['temp'] - 273.15
                return temperature
            else:
                print("Error fetching weather data!")

server = Agent(
    name="agent server",
    port=8001,
    seed="agent server secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
fund_agent_if_low(server.wallet.address())

@server.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from user({sender})")
    
    city = msg.city
    state = msg.state
    country= msg.country
    min_temp = msg.min_temp
    max_temp = msg.max_temp
    latitude, longitude= Temperature.geo_location(city, state, country)
    if latitude is not None and longitude is not None:
        temperature = Temperature.get_weather_data(latitude, longitude)
        print(f"Temperature in {city}, {state}, {country}: {temperature}°C")
        if temperature < min_temp:
            alert_msg = f"Alert: Temperature({temperature}°C) is below minimum Min temperature ({min_temp}°C)"
        elif temperature > max_temp:
            alert_msg = f"Alert: Temperature({temperature}°C) is above maximum Max temperature ({max_temp}°C)"
        else:
            alert_msg = f"Temperature({temperature}°C) is within the acceptable range ({min_temp}-{max_temp}°C)"
        response_msg = Response(
            Temp=temperature,
            msg= alert_msg
        )
        await ctx.send(sender, response_msg)
    else:
        response_msg = Response(
            Temp=None,
            msg="Location not found!"
        )
        await ctx.send(sender, response_msg)


if __name__ == "_main_":
    server.run()