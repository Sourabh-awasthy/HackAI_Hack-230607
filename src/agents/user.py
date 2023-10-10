from uagents.setup import fund_agent_if_low
from uagents import Agent, Context
import requests
from messages.basic import Message
from messages.basic import Response
# from flask import Flask, render_template, session
# from utils.app import Weather_data

from dotenv import load_dotenv
load_dotenv()
import json
import os
# from utils.app import weather_preferences


# @app.route('/display_weather_data')
# def display_weather_data():
#     # Access the form data from the session
#     data = session.get('weather_data')

#     if data:
#         # Use the form data as needed
#         print(f'Country: {data["country"]}')
#         print(f'State: {data["state"]}')
#         print(f'City: {data["city"]}')
#         print(f'Min Temperature: {data["min_temperature"]}')
#         print(f'Max Temperature: {data["max_temperature"]}')
#     else:
#         print('No form data available.')

server_ADDRESS = "agent1q26us2kxn8jdm9slaql775pcrw9lk7n5ruf49ws0pd7nrdnspm0gvxv5hf0"
min_temp=float(input("Enter The Minimum Temperature: ")) 
max_temp=float(input("Enter The Minimum Temperature: ")) 
city = input("Enter The City: ").lower()
state= input("Enter The State: ").lower()
country= input("Enter The Country: ").lower()

class Location:
    @staticmethod
    def geo_location():
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

user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],

)

fund_agent_if_low(user.wallet.address())

@user.on_interval(period=2.0)
async def send_message(ctx: Context):
    latitude, longitude = Location.geo_location()
 
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
    ctx.logger.info(f"Received message from server: {msg.msg}")




if __name__ == "__main__":
    user.run()







   

