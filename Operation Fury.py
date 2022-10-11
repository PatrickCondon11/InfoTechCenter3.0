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


def gas_level_alert():
    if gas_level_indicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")

    elif gas_level_indicator == "Low":
        print("***WARNING YOUR GAS TANK IS LOW***\n***You have less than 20 miles left***")
        sleep(1)
        print("Finding closest gas station")
        sleep(2)
        print("The closest gas station is", random.randint(5, 25), "miles away.")

    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is at a quarter of a tank and you have 80 miles left.")


gas_level_alert()
