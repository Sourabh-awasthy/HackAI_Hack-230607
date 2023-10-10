from uagents.setup import fund_agent_if_low
from uagents import Agent, Context
import requests
from messages.basic import Message
from messages.basic import Response
from dotenv import load_dotenv
import json
import os
load_dotenv()

server_ADDRESS = os.getenv("SERVER_ADDRESS")

min_temp=float(input("Enter The Min_Temperature(Celsius): ")) 
max_temp=float(input("Enter The Min_Temperature(Celsius): "))
city = input("Enter The City :").lower()
state= input("Enter The State :").lower()
country= input("Enter The Country Code(Example for INDIA->IN) :").lower()
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
                    if (location.get("country").lower() == country and location.get("state").lower() == state and location.get("name").lower() == city):
                        latitude = location.get("latitude")
                        longitude = location.get("longitude")
                    break

                if latitude is not None and longitude is not None:
                    return latitude, longitude
                else:
                    return None, None
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
    '''<<--------->>---------<<-------->>------<<--------->>
        
        
    '''
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




if __name__ == "_main_":
    user.run()