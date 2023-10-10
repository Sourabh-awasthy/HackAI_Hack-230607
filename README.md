#  Temperature Alert 
## Description
The Temperature Alert using uAgent library, a tool that:
* Connects to a free weather API to fetch real-time temperatures for the specified location.
* Lets users set their preferred temperature range (e.g., a minimum and maximum temperature) and
location.
* Sends an alert/notification to the user when the current temperature in their chosen
location goes below the minimum or above the maximum threshold they've set.


### Step 1: Prerequisites
Before starting, you'll need the following:
* Python (3.8+ is recommended)
* Poetry (a packaging and dependency management tool for Python)
    (Link for installation https://python-poetry.org/docs/)


### Step 2: Set up .env file
To run the demo, you need API keys from:
* OpenWeather API (Current data)
* API Ninjas (Geocoding API)

##### OpenWeather API
* Visit OpenWeather(https://openweathermap.org/api).
* Sign up or log in.
* Your API key will be available on the dashboard.
* Use Current Weather data.

##### API Ninjas
* Visit API Ninjas(https://api-ninjas.com/api/geocoding).
* Sign up or log in.
* Your API key will be available on the dashboard.
* Use Geocoding Api.



Once you have the key, create a .env file in the src directory.
```bash
export WEATHER_API_KEY="{GET THE OPEN WEATHER API KEY}"
export LOCATION_API_KEY="{GET THE API NINJAS GEOCODING API KEY}"
export SERVER
```
To use the environment variables from .env and install the project:
```bash
poetry intall
poetry shell
pip install -r requirements.txt
```
### Step 3: Run the main script
To run the project and its agents:
```bash
cd src
poetry run python main.py
```


You need to look for the following output in the logs:
```
ALERT: Temperature in YourLocation is {}.
```

You will get alert as Push notifications as alerts.
You can set your personalised minimum as well as maximum temperature for alert
