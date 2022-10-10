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
random_int2 = random.randint(10, 25)
random_int3 = random.randint(5, 15)


def vehicle_response_system():
    if weather_alert1 == "Icy":
        print("\nVRS has changed your alarm to be", random_int1,
              "minutes earlier based on the NWS forecast of icy roads.")
        print("VRS will only allow your car to go 30MPH")

    elif weather_alert1 == "Snowing":
        print("\nVRS has changed your alarm to be", random_int2,
              "minutes earlier based on the NWS forecast of Snow in the area.")
        print("VRS will only allow your car to go 50MPH")

    elif (weather_alert1 == "Raining" and random_int3 >= 15):
        print("\nVRS has changed your alarm to be", random_int2,
              "minutes earlier based on the NWS forecast of heavy rain.")
        print("VRS will only allow your car to go 60MPH")

    elif weather_alert1 == "Raining":
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of rain.")
        print("VRS will only allow your car to go 70MPH")

    elif weather_alert1 == "Storming":
        print("\nVRS has changed your alarm to be", random_int2,
              "minutes earlier based on the NWS forecast of storms in the area.")
        print("VRS will only allow your car to go 50MPH")

    elif (weather_alert1 == "Foggy" and random_int3 >= 15):
        print("\nVRS has changed your alarm to be", random_int2,
              "minutes earlier based on the NWS forecast of heavy fog.")
        print("VRS will only allow your car to go 60MPH")

    elif weather_alert1 == "Foggy":
        print("\nVRS has changed your alarm to be", random_int3, "minutes earlier based on the NWS forecast of fog.")
        print("VRS will only allow your car to go 70MPH")

    elif weather_alert1 == "Cloudy":
        print("\nBased on the NWS there is lowered visibility and cloudy skies.")
        print("VRS will only allow your car to go 80MPH")

    else:
        print("\nBased on the NWS there is clear visibility and a bright, sunny sky.")


vehicle_response_system()