#Nandan Dhanesh
#Function to output text by typing

import sys
from time import sleep

def typing(message):
    for char in message:
        sleep(0.07) 
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(0.3) #
    print("")

def typing_quick(message):
    for char in message:
        sleep(0.005) 
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(0.3) 
    print("")