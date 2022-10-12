# Gasoline
# Developer: Patrick Condon
# Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if,elif,else
condition
"""

# import library here
import random
from time import sleep


# Gas level function
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter tank", "Full Tank"]
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

def gas_station_street
    street_name_list = 



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
            if calling_second_contact == "Y":
                sleep(2)
                print("Calling emergency contact")
            if calling_second_contact == "y":
                sleep(2)
                print("Calling secondary emergency contact")
                sleep(2)
                print("Successfully called secondary emergency contact")

    elif gas_level_indicator == "Low":
        print("\033[3;31m***WARNING YOUR GAS TANK IS  EXTREMELY LOW***\n***You have 20 miles left***")
        sleep(1)
        print("\033[0mFinding closest gas station using google maps")
        sleep(2)
        print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
              "miles away.")
        if miles_to_gas_station > 20:
            sleep(1)
            print("***WARNING***\nYou will not reach the closest gas station")
            sleep(2)
            print("Calling Emergency Contact")
            sleep(2)
            if emergency_contact_availability == 0:
                print("Emergency contact unavailable")
                calling_second_contact = input("Do you want to call secondary emergency contact\nType Y or N.\n")
                if calling_second_contact == "Y":
                    sleep(2)
                    print("Calling emergency contact")
                if calling_second_contact == "y":
                    sleep(2)
                    print("Calling secondary emergency contact")
                    sleep(2)
            print("Successfully called emergency contact")

    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is at a quarter of a tank and you have", random.randint(50, 100), "miles left.")
        print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
              "miles away.")

    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is at half of a tank and you have", random.randint(125, 175), "miles left.")

    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is at a quarter of a tank and you have", random.randint(200, 250), "miles left.")

    else:
        print("Your gas tank is at a quarter of a tank and you have 300 miles left.")


gas_level_alert()
