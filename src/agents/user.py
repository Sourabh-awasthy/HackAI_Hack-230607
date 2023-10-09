from uagents.setup import fund_agent_if_low
from uagents import Agent, Context
import requests
from messages.basic import Message
from messages.basic import Response

from dotenv import load_dotenv
load_dotenv()
import json
import os

server_ADDRESS = "agent1q26us2kxn8jdm9slaql775pcrw9lk7n5ruf49ws0pd7nrdnspm0gvxv5hf0"
min_temp=float(20.01)  # Set your preferred minimum temperature
max_temp=float(30.02)  # Set your preferred maximum temperature

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
    # a = geo_location()
    # print(a)

user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],

)

fund_agent_if_low(user.wallet.address())


# @user.on_interval(period=2.0)
# async def send_message(ctx: Context):
#     await ctx.send(server_ADDRESS, Message(latitude=latitude,longitude=longitude))
@user.on_interval(period=2.0)
async def send_message(ctx: Context):
    latitude, longitude = Temperature.geo_location()
    if latitude is not None and longitude is not None:
        message = Message(
            latitude=latitude,
            longitude=longitude,
            min_temp=min_temp,
            max_temp=max_temp,
            msg="Bring it on"
        )
        await ctx.send(server_ADDRESS, message)
    else:
        print("Unable to retrieve location.")

@user.on_message(model=Response)
async def message_handler(ctx: Context, sender: str, msg: Response):
    ctx.logger.info(f"Received message from server: {msg.Temp}")




if __name__ == "__main__":
    user.run()







#     @staticmethod
#     def get_weather_data(latitude, longitude):
#         WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
#         WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
#         weather_data= requests.get(WEATHER_API_URL)
#         if weather_data.status_code == 200:
#             data= weather_data.json()
#             temperature= data['main']['temp'] - 273.15
#             return temperature
#         else:
#             print("Error fetching weather data!")

# def get_temp(): 
#     latitude, longitude = Temperature.geo_location()
#     if latitude is not None and longitude is not None:
#             print(f"Latitude: {latitude:.6f}°, Longitude: {longitude:.6f}°")
    
#             # Get weather data based on the user's location
#             temperature = Temperature.get_weather_data(latitude, longitude)
#             if temperature is not None:
#                 print(f"Temperature: {temperature:.2f}°C")
#                 return temperature
#     else:
#         print("Unable to retrieve your location.")


# if _name_ == "_main_":
#     agent = TemperatureAlertAgent(
#         name="MyTemperatureAgent",
#         location="YourLocation",
        
#     )

#     while True:
#         agent.check_temperature()