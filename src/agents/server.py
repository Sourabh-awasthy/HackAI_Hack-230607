import requests
# from uagents import Agent
# import os
# import json
from dotenv import load_dotenv
# from main import Temperature
load_dotenv()

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


from uagents.setup import fund_agent_if_low
from uagents.resolver import get_agent_address
from uagents import Agent, Context

from messages.basic import Message
from messages.basic import Response



server = Agent(
    name="agent server",
    port=8001,
    seed="agent server secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
fund_agent_if_low(server.wallet.address())


# @server.on_message(model=Message)
# async def message_handler(ctx: Context, sender: str, msg: Message):
#     ctx.logger.info(f"Received message from {sender}: {msg.longitude}")

#     # send the response
#     await ctx.send(sender, Message(msg="Hello there user."))

@server.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from user: {msg.longitude}")

    # Create a response message with the required fields
    response_msg = Response(
        Temp=14.6,
        msg="Hello there user."
    )

    # send the response
    await ctx.send(sender, response_msg)

if __name__ == "__main__":
    server.run()