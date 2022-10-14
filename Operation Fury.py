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


street_name_list = ["presidents", "10th st", "m-89", "mile"]
random_street_name = random.choice(street_name_list)
list_of_presidents = ["Washington", "Adams", "Jefferson", "Reagon", "Lincoln", "Roosevelt", "Van Buren"]
random_president_name = random.choice(list_of_presidents)
list_of_street_types = ["Ave", "St", "Blvd", "Ln"]
random_street_type = random.choice(list_of_street_types)
street_number = random.randint(1, 50)
michigan_highway_number = random.randint(1, 220)
mile_road_number = random.randint(1, 30)


def gas_level_alert():
    if gas_level_indicator == "Empty":
        print("\033[3;31m***WARNING YOU ARE ON EMPTY***\033[0m")
        sleep(1)
        print("Calling emergency contact")
        sleep(2)
        if emergency_contact_availability == 0:
            print("Emergency contact unavailable")
            calling_second_contact = input("Do you want to call secondary emergency contact\nType Y or N.\n")
            if (calling_second_contact == "Y" or "y"):
                sleep(2)
                print("Calling secondary emergency contact")
                sleep(2)
                print("Successfully called secondary emergency contact")
        else:
            print("Successfully called emergency contact")

    elif gas_level_indicator == "Low":
        print("\033[3;31m***WARNING YOUR GAS TANK IS  EXTREMELY LOW***\n***You have 20 miles left***")
        sleep(1)
        print("\033[0mFinding closest gas station using google maps")
        sleep(2)

        if random_street_name == "presidents":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", random_president_name, random_street_type)

        elif random_street_name == "m-89":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on M-" + str(michigan_highway_number))

        elif (random_street_name == "10th st" and int(street_number) == 3 or int(street_number) == 13 or int(
                street_number) == 23 or int(street_number) == 33 or int(street_number) == 43):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "rd St")

        elif (random_street_name == "10th st" and int(street_number) == 2 or int(street_number) == 12 or int(
                street_number) == 22 or int(street_number) == 32 or int(street_number) == 42):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "nd St")

        elif (random_street_name == "10th st" and int(street_number) == 1 or int(street_number) == 11 or int(
                street_number) == 21 or int(street_number) == 31 or int(street_number) == 41):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "st St")

        elif random_street_name == "mile":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", mile_road_number, "Mile Rd")

        else:
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "th St")

        if miles_to_gas_station > 20:
            sleep(1)
            print("***WARNING***\nYou will not reach the closest gas station")
            sleep(2)
            print("Calling Emergency Contact")
            sleep(2)
            if emergency_contact_availability == 0:
                print("Emergency contact unavailable")
                calling_second_contact = input("Do you want to call secondary emergency contact\nType Y or N.\n")
                if (calling_second_contact == "Y" or "y"):
                    sleep(2)
                    print("Calling secondary emergency contact")
                    sleep(2)
                    print("Successfully called secondary emergency contact")

            else:
                print("Successfully called emergency contact")

    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is at a quarter tank of gas and you have", random.randint(50, 100), "miles left.")

        if random_street_name == "presidents":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", random_president_name, random_street_type)

        elif random_street_name == "m-89":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on M-" + str(michigan_highway_number))

        elif (random_street_name == "10th st" and int(street_number) == 3 or int(street_number) == 13 or int(
                street_number) == 23 or int(street_number) == 33 or int(street_number) == 43):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "rd St")

        elif (random_street_name == "10th st" and int(street_number) == 2 or int(street_number) == 12 or int(
                street_number) == 22 or int(street_number) == 32 or int(street_number) == 42):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "nd St")

        elif (random_street_name == "10th st" and int(street_number) == 1 or int(street_number) == 11 or int(
                street_number) == 21 or int(street_number) == 31 or int(street_number) == 41):
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "st St")

        elif random_street_name == "mile":
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", mile_road_number, "Mile Rd")

        else:
            print("The closest gas station is a", list_of_gas_stations(), "gas station", miles_to_gas_station,
                  "miles away on", str(street_number) + "th St")

    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is at half a tank of gas and you have", random.randint(125, 175), "miles left.")

    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank and you have", random.randint(200, 250), "miles left.")

    elif gas_level_indicator == "Full Tank":
        print("Your gas tank is at a full tank of gas and you have 300 miles left.")


gas_level_alert()