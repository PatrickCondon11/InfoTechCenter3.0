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

#Gas level function
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter tank", "Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level

gas_level_gauge()

if gas_level_gauge() == "Empty":
    print("Your gas tank is empty")