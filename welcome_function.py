#Nandan Dhanesh
#Welcome function

import typing_function as tf
import tutorial_function as tut
import data_formatting as dt

def welcome():

    accept = ['Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no']

#     print("\033[0;32m \n")
#     tf.typing_quick(""" /$$$$$$$$                       /$$ /$$                            /$$$$$$  /$$                         /$$             /$$                              
# |__  $$__/                      | $$|__/                           /$$__  $$|__/                        | $$            | $$                              
#    | $$  /$$$$$$  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$       | $$  \__/ /$$ /$$$$$$/$$$$  /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$       
#    | $$ /$$__  $$|____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$ | $$| $$_  $$_  $$| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$      
#    | $$| $$  \__/ /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$| $$ \ $$ \ $$| $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/      
#    | $$| $$      /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$| $$ | $$ | $$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$            
#    | $$| $$     |  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/| $$| $$ | $$ | $$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$            
#    |__/|__/      \_______/ \_______/|__/|__/  |__/ \____  $$       \______/ |__/|__/ |__/ |__/ \______/ |__/ \_______/   \___/   \______/ |__/            
#                                                    /$$  \ $$                                                                                              
#                                                   |  $$$$$$/                                                                                              
#                                                    \______/      
#                                                    \033[0;0m """)

    tf.typing("\nWelcome to the Trading Simulator\n")
    tutorial = str(input("\nWould you like a tutorial? (Y/N): ")) 

    while tutorial not in accept:
        tutorial = str(input("\nWould you like a tutorial? (Y/N): "))

    if tutorial in accept[0:4]:
        symbol = tut.tutorial()
    else: 
        symbol = input("\n\033[0;0mEnter a stock ticker to get started: ")

    symbol.upper()

    df_source = dt.import_data(symbol) 

    while len(df_source.index) <= 800:
        print("Stock is newly listed, delisted or does not exist \n")
        symbol = input("Enter a new ticker: ")
        "\n"
        df_source = dt.import_data(symbol)

    return symbol, df_source