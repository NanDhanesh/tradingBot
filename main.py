#Nandan Dhanesh
#Main loop

import time
#Importing all other project files for use in the main loop
import classifier_function as clf
import feature_set_derival as fs
import portfolio_class as prc
import rule_creation as rc
import end_sim_function as es
import post_sim as ps
import welcome_function as wf
import typing_function as tf

#Calls welcome function to start program and stores returned ticker symbol and dataset
symbol, df_source = wf.welcome() 
#Derives the optimum feature set for the specific stock based on its ticker symbol
feature_set = fs.optimum_feature_set(symbol) 
#Calls classify function that returns the recommendations of the trained RF model
trade_recs = clf.classify(df_source, feature_set)
#Initiates the portfolio object with $10,000 of simulated capital
portfolio = prc.Portfolio(10000)

tf.typing("The model has been trained and is ready to start trading\n")
tf.typing("DISCLAIMER: This is only a simulation and should not be used when trading real financial markets \n\n\n")
time.sleep(3)

#Main loop
for i in range(len(trade_recs)-1):

    #Establishes the position size in shares as 30% of the portfolio's capital worth of the current share price
    position_size = (0.3*portfolio.getTotalCapital()) // trade_recs['Open Price'][i] 

    print("-------------------------------------------", trade_recs['Date'][i].date(), "-------------------------------------------\n")

    #Checks profit targets, stop losses, and lifespans of all existing open positions
    portfolio.checkTargets(trade_recs['Date'][i], trade_recs['Open Price'][i])
    portfolio.checkStops(trade_recs['Date'][i], trade_recs['Open Price'][i])
    portfolio.checkLifespans(trade_recs['Date'][i], trade_recs['Open Price'][i])

    #Handling a buy recommendation
    if trade_recs['Recommendation'][i] == 2:
        #If the buy recommendation meets all risk rules, buy a new position at the current open price
        if rc.check_buy(trade_recs['Probability'][i], portfolio.getTotalCapital(), portfolio.getUnallocatedCapital(), trade_recs['Open Price'][i], position_size) == True:
            portfolio.openPosition(trade_recs['Date'][i], trade_recs['Open Price'][i], position_size)
            print("\033[1;35mBought ", position_size, symbol, "at price", trade_recs['Open Price'][i], "\033[0;0m\n")
        #If any risk rules are not met, do not execute the buy recommendation and display non-execution message
        else:
            print("Buy order not executed, rules not met \n")

    #Handling a hold recommendation
    if trade_recs['Recommendation'][i] == 1:
        print("Holding current positions \n")

    #Handling a sell recommendation
    if trade_recs['Recommendation'][i] == 0:
        #If the sell recommendation meets rules, sell the oldest position at the current open price
        if rc.check_sell(trade_recs['Probability'][i], len(portfolio.getOpenPositions())) == True:
            bought_date, buy_price, position_size = portfolio.closePosition(trade_recs['Date'][i], trade_recs['Open Price'][i])
            #If the closed postion was profitable, print the profit in green
            if ((trade_recs['Open Price'][i] - buy_price) * position_size) >= 0:
                print("\033[1;36mSold position bought on ", bought_date," at price ", trade_recs['Open Price'][i], " for a profit of \033[1;32m", ((trade_recs['Open Price'][i] - buy_price) * position_size), "\033[0;0m\n")
            #If the closed postion was not profitable, print the loss in red
            else:
                print("\033[1;36mSold position bought on ", bought_date," at price ", trade_recs['Open Price'][i], " for a loss of \033[1;31m", ((trade_recs['Open Price'][i] - buy_price) * position_size), "\033[0;0m\n")
        #If any rules are not met, do not execute the sell recommendation and display non-execution message
        else:
            print("Sell order not executed, rules not met \n")

    #Update the current prices and lifespans of all open positions
    portfolio.update(trade_recs['Open Price'][i])
    #Printing the number of currently open positions
    print("There are", portfolio.getNumOpenPositions(), "open positions\n")
    #Printing total account value, allocated capital, and unallocated capital
    print("Account value:               ", portfolio.getTotalCapital())
    print("Allocated capital:           ", portfolio.getAllocatedCapital())
    print("Unallocated capital:         ", portfolio.getUnallocatedCapital())
    #If the closed profit/loss is positive, print the profit in green, otherwise print the loss in red
    if portfolio.getClosedPL() >= 0:
        print("Closed P/L:                  \033[0;32m", portfolio.getClosedPL(), "\033[0;0m\n")
    else:
        print("Closed P/L:                  \033[0;31m", portfolio.getClosedPL(), "\033[0;0m\n")

    #Sleep for 0.8 seconds before simulating next trading day to make trading easier to follow
    time.sleep(0.8)

#After 300 days of simulation are over, use EndSim function to close all outstanding positions and return buy+sell prices/dates of all closed positions
buy_prices, buy_dates, sell_prices, sell_dates = es.end_sim(portfolio, trade_recs['Date'][-1], trade_recs['Open Price'][-1])

#Plot 2 charts showing total capital over time and buy and sell points on the stock price chart
ps.capital_plot(portfolio.getTimeCapital(), trade_recs['Open Price'], trade_recs['Date'], buy_prices, buy_dates, sell_prices, sell_dates)
