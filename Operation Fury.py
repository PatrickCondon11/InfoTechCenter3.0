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
    weather_forecast = ["Rainy", "Snowy", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


print(weather())