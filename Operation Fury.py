# **********************************************************************************************************************
# Import Libraries Here
from time import sleep
#We imported the sleep function from the time library
import random
# **********************************************************************************************************************


# Welcome Screen
# Developer: Patrick Condon
# Version: 1.0

"""
Our welcome screen will start our program letting drivers know
that the info tech center OS is loading
"""

print("\033[3;32m")
print("\n\nWelcome to Operation Fury Info Tech Center")
sleep(2)
print("\n\033[3;34mOperation Fury's Operating System booting up\033[0m")
for i in range(3):
    print("OS Booting Up...")
    sleep(1)
print("\033[3;34mOS Booted Up\033[0m\n")
sleep(1.5)


# Gasoline
# Developer: Patrick Condon
# Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if,elif,else
condition
"""

# Gas level function
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level


# Variable calling the gas_level_gauge to store value once
gas_level_indicator = gas_level_gauge()
miles_to_gas_station = round(random.uniform(1, 25), 1)
emergency_contact_availability = random.randint(0, 1)


def list_of_gas_stations():
    gas_station_list = ["Shell", "Circle K", "Marathon", "Speedway", "Meijer"]
    gas_station_nearby = random.choice(gas_station_list)
    return gas_station_nearby


"""
#th st, presidents, m #, de ave
"""

"""
def gas_station_street():
    street_name_list = ["presidents", "10th st", "m-89"]
    random_street_name = random.choice(street_name_list)
    list_of_presidents = ["Washington", "Adams", "Jefferson", "Reagon", "Lincoln", "Roosevelt", "Van Buren"]
    random_president_name = random.choice(list_of_presidents)
    list_of_street_types = ["Ave", "St", "Blvd", "Ln"]
    random_street_type = random.choice(list_of_street_types)
    street_number = random.randint(1, 50)
    michigan_highway_number = random.randint(1, 99)
    if random_street_name == "presidents":
        president_gas_station_road = (random_president_name, list_of_street_types)
        return president_gas_station_road
    if random_street_name == "10th st":
        th_st_gas_station_road = street_number
        return (th_st_gas_station_road and "th st")
    if random_street_name == "m-89":
        m_gas_station = ("m -", michigan_highway_number)
        return ("m -" and michigan_highway_number)


gas_station_street()
"""

def gas_level_alert():
    if gas_level_indicator == "Empty":
        print("\033[3;31m***WARNING YOU ARE ON EMPTY***\033[0m")
        sleep(1)
        print("Calling emergency contact")
        sleep(2)
        print("Successfully called emergency contact")
        if emergency_contact_availability == 0:
            print("Emergency contact unavailable")
            calling_second_contact = input("Do you want to call secondary emergency contact\nType Y or N.\n")
            if calling_second_contact == ("Y" or "y"):
                sleep(2)
                print("Calling secondary emergency contact")

    elif gas_level_indicator == "Low":
        print("\033[3;31m***WARNING YOUR GAS TANK IS  EXTREMELY LOW***\n***You have 20 miles left***")
        sleep(1)
        print("\033[0mFinding closest gas station using google maps")
        sleep(2)
        print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
              "miles away on",)
        if miles_to_gas_station > 20:
            sleep(1)
            print("***WARNING***\nYou will not reach the closest gas station")
            sleep(2)
            print("Calling Emergency Contact")
            sleep(2)
            if emergency_contact_availability == 0:
                print("Emergency contact unavailable")
                calling_second_contact = input("Do you want to call secondary emergency contact\nType Y or N.\n")
                if calling_second_contact == ("Y" or "y"):
                    sleep(2)
                    print("Calling secondary emergency contact")
                    sleep(2)
                    print("Successfully called secondary emergency contact")
            else:
                print("Successfully called emergency contact")

    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is at a quarter tank of gas and you have", random.randint(50, 100), "miles left.")
        print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
              "miles away on")

    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is at half a tank of gas and you have", random.randint(125, 175), "miles left.")

    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank and you have", random.randint(200, 250), "miles left.")

    elif gas_level_indicator == "Full Tank":
        print("Your gas tank is at a full tank of gas and you have 300 miles left.")


gas_level_alert()


# Weather
# Developer: Patrick Condon
# Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using if, elif & else statements
to check the condition and print a specific list element
"""

# Weather condition list using the random.choice library
# to remember choose a condition and storing it in its brain

def weather():
    weather_forecast = ["Raining", "Snowing", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


weather_alert1 = weather()
# import library here




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
