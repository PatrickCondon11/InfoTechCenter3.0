# Weather
# Developer: Patrick Condon
# Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using if, elif & else statements
to check the condition and print a specific list element
"""

# import libraries here
import random


# Weather condition list using the random.choice library
# to remember choose a condition and storing it in its brain
def weather():
    weather_forecast = ["Raining", "Snowing", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


weather_alert = weather()


def vehicle_response_system():
    if weather_alert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forecast of", weather_alert, "roads")


vehicle_response_system()
