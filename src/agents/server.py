import requests
from dotenv import load_dotenv
load_dotenv()
from uagents.setup import fund_agent_if_low
from uagents import Agent, Context
import os
from messages.basic import Message
from messages.basic import Response
from plyer import notification

    
class Temperature:
    @staticmethod
    def get_weather_data(latitude, longitude):

        """ 
           Used to fetch the weather of the given Location
           -----------------------------------------------
           Input >>>> latitude, longitude
           -----------------------------------------------
           Return >>>> temperature
        """           
        
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}"
        weather_data = requests.get(WEATHER_API_URL)
        if weather_data.status_code == 200:
            data = weather_data.json()
            temperature = data['main']['temp'] - 273.15
            return temperature
        else:
            print("Error fetching weather data!")

# Create Agent named 'server'
server = Agent(
    name="agent server",
    port=8001,
    seed="agent server secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
fund_agent_if_low(server.wallet.address())

@server.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    """
        -------------------------------------------
        Used to handle the message from user Agent!
        -------------------------------------------
    """
    ctx.logger.info(f"Received message from user")
    
    latitude = msg.latitude
    longitude = msg.longitude
    temperature = Temperature.get_weather_data(latitude, longitude)
    
    min_temp = msg.min_temp
    max_temp = msg.max_temp
    
    # Logic to test if the temperature is in the given range.
    if temperature < min_temp:
        alert_msg = f"Alert: Temperature({temperature}°C) is below minimum temperature i.e ({min_temp}°C)"
        notification.notify(
            title = 'Alert',
            message = f"Temperature({temperature}°C) is below minimum ({min_temp}°C)",
            app_icon = None,
            timeout = 10,
        )
    elif temperature > max_temp:
        alert_msg = f"Alert: Temperature({temperature}°C) is above maximum temperature i.e ({max_temp}°C)"
        notification.notify(
            title = 'Alert',
            message = f"Temperature({temperature}°C) is above maximum temperature i.e ({max_temp}°C)",
            app_icon = None,
            timeout = 10,
        )
    else:
        alert_msg = f"Temperature {temperature}°C is within the acceptable range ({min_temp}-{max_temp}°C)"
    
    response_msg = Response(
        Temp=temperature,
        msg=alert_msg
    )
    
    # send the response
    await ctx.send(sender, response_msg)

if __name__ == "_main_":
    server.run()