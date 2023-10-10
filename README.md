
# Temperature Alert - HackAI

## Description

The Temperature Alert project utilizes the uAgent library to provide a convenient tool for users to monitor real-time temperatures in a specified location. This project is designed for anyone who wants to receive temperature alerts based on their preferences. Here's what Temperature Alert can do:

- Connects to a free weather API to fetch real-time temperatures for the specified location.
- Allows users to set their preferred temperature range, including a minimum and maximum temperature.
- Sends an alert/notification to the user when the current temperature in their chosen location falls below the minimum or rises above the maximum threshold they've set.

## Getting Started

### Step 1: Prerequisites

Before you start using Temperature Alert, ensure you have the following prerequisites installed:

- Python (version 3.8 or higher is recommended)
- Poetry (a packaging and dependency management tool for Python)

You can install Poetry by following the instructions [here](https://python-poetry.org/docs/).

### Step 2: Set up .env file

To run the Temperature Alert project, you'll need API keys from two sources:

#### OpenWeather API

1. Visit [OpenWeather](https://openweathermap.org/api) and sign up or log in.
2. Your API key will be available on the dashboard. Use the "Current Weather" data option.

#### API Ninjas

1. Visit [API Ninjas](https://api-ninjas.com/api/geocoding) and sign up or log in.
2. Your API key will be available on the dashboard. Use the "Geocoding API."
   
#### SERVER ADDRESS
Visit [Uagents Doc](https://fetch.ai/docs/guides/agents/getting-uagent-address)

Once you have obtained these API keys, create a `.env` file in the `src` directory with the following content:


~~~
export WEATHER_API_KEY="{YOUR OPEN WEATHER API KEY}"
export LOCATION_API_KEY="{YOUR API NINJAS GEOCODING API KEY}"
export SERVER_ADDRESS="{YOUR SERVER ADRRESS}"
~~~

To use the environment variables from .env and install the project:
~~~
bash
poetry intall
poetry shell
pip install -r requirements.txt
~~~
### Step 3: Run the main script
~~~
To run the project and its agents:
bash
cd src
poetry run python main.py
~~~

## Flowchart

Here's a flowchart explaining the flow and logic of our project:

![Flowchart](https://imgtr.ee/images/2023/10/10/15b0cc72682f41565c864b0a2dfbf808.png)

## Working Screenshots

### Screenshot 1: Connection established through UAgent, Example of input

![17bc4ca6977e4187e51c21751d89a470.png](https://imgtr.ee/images/2023/10/10/17bc4ca6977e4187e51c21751d89a470.png)

### Screenshot 2: Receving Alerts

![cc92b1bdedbf2dcd074f179fcc41f803.png](https://imgtr.ee/images/2023/10/10/cc92b1bdedbf2dcd074f179fcc41f803.png)




You need to look for the following output in the logs:

ALERT: Temperature in YourLocation is {}.


You will get alert as Push notifications as alerts.
You can set your personalised minimum as well as maximum temperature for alert

