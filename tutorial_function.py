#Nandan Dhanesh
#Welcome function

import typing_function as tf

def tutorial():
    print("\033[0;0m")
    tf.typing("This is a simulation of automated stock trading using machine learning")
    tf.typing("Choose any stock that is listed on the NYSE or NASDAQ exchanges\n")
    tf.typing("All of the historical data on your chosen stock will be retrieved")
    tf.typing("A Random Forest machine learning model will be trained on the historical data")
    tf.typing("The model will then attempt to make trading decisions for the most recent 300 trading days")
    tf.typing("It will trade using a portfolio of 10,000 simulated US Dollars\n")
    tf.typing("It will decide whether to 'Buy', 'Sell', or 'Hold' each day")
    tf.typing("Its decisions will be executed only if they meet an assortment of risk rules\n")
    tf.typing("Rule 1.) The system will only take 'long' positions and cannot sell if it does not own anything")
    tf.typing("Rule 2.) Only a maximum of 65% of the portfolio can be invested before taking a new position")
    tf.typing("Rule 3.) Each new position will be bought with an equivalent of 30% of the account's capital")
    tf.typing("Rule 4.) Each position will be sold if it rises 5% from its buy point to protect profit")
    tf.typing("Rule 5.) Each position will be sold if it falls 5% from its buy point to limit losses")
    tf.typing("Rule 6.) Each position will be sold after 10 days if it has not hit the profit target or stop loss\n")
    tf.typing("Despite being a simulation of past trading days, all decisions made will be blind to future data")
    tf.typing("All positions will be tracked and performance will be displayed at the end\n")
    tf.typing("\033[1;35mA new position being bought will look like this\033[0;0m")
    tf.typing("\033[1;36mA position being sold will look like this\033[0;0m\n")
    tf.typing("\033[3;32mA position hitting its profit target and being sold will look like this\033[0;0m")
    tf.typing("\033[3;31mA position hitting its stop loss and being sold will look like this\033[0;0m")
    tf.typing("\033[3;33mA position hitting its 10 day lifespan and being sold will look like this\033[0;0m\n")
    tf.typing("Some popular stocks are: TSLA(Tesla Motors), MSFT(Microsoft Corp.) and NVDA(Nvidia Corp.)")
    # symbol = input("\033[0;0mEnter a stock ticker to get started: ")
    # return symbol

