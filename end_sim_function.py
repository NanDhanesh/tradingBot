#Nandan Dhanesh
#End simulation function

import typing_function as tp
from time import sleep

def end_sim(portfolio, end_date, end_price):
    buy_prices = []
    buy_dates = []
    sell_prices = []
    sell_dates = []

    for position in portfolio.getOpenPositions():
        portfolio.closePosition(end_date, end_price)
    portfolio.update(end_price)
    tp.typing("------------------------------------------- END OF SIM -------------------------------------------\n")
    tp.typing("The overall closed P/L for the 300 days of simulation is: ")
    if portfolio.getClosedPL() >= 0 :
        print("\033[0;32m",portfolio.getClosedPL(),"\033[0;0m\n")
    else:
        print("\033[0;31m",portfolio.getClosedPL(),"\033[0;0m\n")
    sleep(1)
    

    for position in portfolio.getClosedPositions():
        buy_prices.append(position.getBuyPrice())
        buy_dates.append(position.getBoughtDate())
        sell_prices.append(position.getSellPrice())
        sell_dates.append(position.getSoldDate())


    tp.typing("The following charts will show the performance of the system over the trading period")
    tp.typing("The chart on the left shows the capital in the account over the trading period")
    tp.typing("The chart on the right shows at which points the stock was bought and sold \n")
    sleep(1)

    return buy_prices, buy_dates, sell_prices, sell_dates
    




