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


weather_alert1 = weather()

random_int1 = random.randint(15, 30)
random_int2 = random.randint(10, 20)
random_int3 = random.randint(5, 25)


def vehicle_response_system():
    if weather_alert1 == "Icy":
        print("\nVRS has changed your alarm to be", random_int1, "minutes earlier based on the NWS forecast of icy roads.")

    elif weather_alert1 == "Raining" and random_int3 >= 15:
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of heavy rain.")
    elif weather_alert1 == "Raining":
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of rain.")

    elif weather_alert1 == "Storming":
        print("\nVRS has changed your alarm to be", random_int2, "minutes earlier based on the NWS forecast of storms in the area.")

    elif weather_alert1 == "Foggy" and random_int3 >= 15:
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of heavy fog.")
    elif weather_alert1 == "Foggy":
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of fog.")

    elif weather_alert1 == "Sunny":
        print("\nBased on the NWS forecast there is clear visibility and sunny skies.")

    elif weather_alert1 == "Cloudy":
        print("\nBased on the NWS there is lowered visibility and cloudy skies.")


vehicle_response_system()
