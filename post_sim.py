#Nandan Dhanesh
#Post_simulation visualisations

from matplotlib import pyplot as plt

def capital_plot(time_pl, opens, dates, buy_prices, buy_dates, sell_prices, sell_dates):
    #fig = plt.figure()
    #fig.set_size_inches(10,5)
    #plt.plot(Dates, time_pl)
    #plt.show()

#def PositionPlot(opens, dates, buy_prices, buy_dates, sell_prices, sell_dates):
    #fig = plt.figure()
    #fig.set_size_inches(10,5)
    #plt.plot(dates, opens, label = 'Price', zorder = 0)
    #plt.scatter(buy_dates, buy_prices, color = 'green', label = 'Buys', zorder = 5)
    #plt.scatter(sell_dates, sell_prices, color = 'red', label = 'Sells', zorder = 10)
    #plt.show()

    # Create figure

    fig = plt.figure()
    fig.set_size_inches(20,7)

    # Define Data Coordinates


    # Create each subplot individually#


    plt.subplot(2, 2, 1)
    plt.plot(dates, time_pl)
    plt.xlabel('Date')
    plt.ylabel('Total Capital')
    plt.subplot(2, 2, 2)
    plt.plot(dates, opens, label = 'Price', zorder = 0)
    plt.scatter(buy_dates, buy_prices, color = 'green', label = 'Buys', zorder = 5)
    plt.scatter(sell_dates, sell_prices, color = 'red', label = 'Sells', zorder = 5)
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    # One Title
    plt.suptitle('Trading Performance and Decisions Over Time')

    # Auto adjust
    plt.tight_layout()
    # Display

    plt.show()