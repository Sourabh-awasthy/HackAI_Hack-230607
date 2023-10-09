from uagents import Bureau

from agents.user import Temperature
from agents.response import TemperatureAlertAgent


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    bureau.add(Temperature)
    bureau.add(TemperatureAlertAgent)
    bureau.run()