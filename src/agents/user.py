from uagents.setup import fund_agent_if_low
from uagents import Agent, Context
import requests
from messages.basic import Message
from messages.basic import Response

from dotenv import load_dotenv
load_dotenv()
import json
import os

server_ADDRESS = os.getenv("SERVER_ADDRESS")
def user_inputs():  
   min_temp= input("Enter Min temp: ")  # Set your preferred minimum temperature
   max_temp=input("Enter Max temp: ")  # Set your preferred maximum temperature
   city = input("Enter City: ")
   state= input("Enter state: ")
   country= input("Enter country: ")
   return min_temp, max_temp, city, state, country

user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(user.wallet.address())


@user.on_interval(period=2.0)
async def send_message(ctx: Context):
    min_temp, max_temp, city, state, country = user_inputs()
    message = Message(
            min_temp=min_temp,
            max_temp=max_temp,
            city= city,
            state= state,
            country= country
        )
    print(message)
    await ctx.send(server_ADDRESS, message)
    # else:
    #     print("Unable to retrieve location.")

@user.on_message(model=Response)
async def message_handler(ctx: Context, sender: str, msg: Response):
    ctx.logger.info(f"Received message from server:({sender}): Temperature at{msg.Temp} {msg.msg}")




if __name__ == "__main__":
    user.run()
