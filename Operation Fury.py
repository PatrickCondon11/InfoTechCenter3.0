# Welcome Screen
# Devoloper: Patrick Condon
# Version: 1.0

'''
Our welcome screen will start our program letting drivers know
that the info tech center OS is loading
'''

# Import Libraries Here
from time import sleep # We imported the sleep function from the time library

print("\033[3;32m")
print("\n\nWelcome to Operation Fury Info Tech Center")
sleep(2)
print("\n\033[3;34mOperation Fury's Operating System booting up\033[0m")
for i in range(3):
    print("OS Booting Up...")
    sleep(2)
print("\033[3;34mOS Booted Up")