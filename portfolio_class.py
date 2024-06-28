#Nandan Dhanesh
#Portfolio class

#Importing the position_class project file
import position_class as pc

#Creating the main Portfolio class to house all positions
class Portfolio:
    def __init__(self, starting_capital):
        #Initialising all class attributes
        self._totalCapital = starting_capital
        self._startingCapital = starting_capital
        self._allocatedCapital = 0
        self._unallocatedCapital = starting_capital
        self._openPositions = []
        self._closedPositions = []
        self._openPL = 0
        self._closedPL = 0
        #Time Capital used to track the total capital on each day for performance charting at the end of the sim
        self._timeCapital = []


    #Defining all getter functions
    def getTotalCapital(self):
        return self._totalCapital

    def getAllocatedCapital(self):
        return self._allocatedCapital

    def getUnallocatedCapital(self):
        return self._unallocatedCapital

    def getClosedPL(self):
        return self._closedPL

    def getOpenPositions(self):
        return self._openPositions

    def getClosedPositions(self):
        return self._closedPositions

    def getNumOpenPositions(self):
        return len(self._openPositions)

    def getTimeCapital(self):
        return self._timeCapital


    #Defining the method used when a new position is to be opened and added to the portfolio
    def openPosition(self, bought_date, buy_price, position_size):
        #Initialising a position object and adding it to the open positions of the portfolio
        self._openPositions.append(pc.Position(bought_date, buy_price, position_size))
        #Adjusting allocated and unallocated capital after a new position is bought
        self._allocatedCapital += buy_price * position_size
        self._unallocatedCapital -= buy_price * position_size

    #Defining the method used when an existing position must be sold and removed from the portfolio
    def closePosition(self, sold_date, sell_price):
        #Setting sale date and price of the position
        self._openPositions[0].setSoldDate(sold_date) 
        self._openPositions[0].setSellPrice(sell_price)
        #Adjusting unallocated and allocated capital in the portfolio
        self._unallocatedCapital += sell_price * self._openPositions[0].getPositionSize()
        self._allocatedCapital -= sell_price * self._openPositions[0].getPositionSize()
        #Adding the final profit/loss of the position to the portfolio's closed P/L
        self._closedPL += ((sell_price - self._openPositions[0].getBuyPrice())) * self._openPositions[0].getPositionSize()
        #Adding the closed position object to the portfolio's closed positions list
        self._closedPositions.append(self._openPositions[0])
        #Removing the position from the portfolio's open positions list and thus closing it
        self._openPositions.pop(0)
        #Returning the buy date, buy price, and position size of the closed position for performance tracking
        return self._closedPositions[-1].getBoughtDate(), self._closedPositions[-1].getBuyPrice(), self._closedPositions[-1].getPositionSize()

    #Defining the method used to update all existing positions each day
    def update(self, current_price):
        #Resetting open profit/loss and allocated capital to 0
        self._openPL = 0
        self._allocatedCapital = 0
        #For each open position, add the open profit/loss to openPL, update the lifespan, and add its value to alloc_allocatedCapital
        for position in (self._openPositions):
            self._openPL += ((current_price) - (position.getBuyPrice())) * position.getPositionSize()
            position.incrementLifespan()
            self._allocatedCapital += ((current_price) * position.getPositionSize())
        #Calculating the new total capital and unallocated capital in the porfolio
        self._totalCapital = self._startingCapital + self._closedPL + self._openPL
        self._unallocatedCapital = self._totalCapital - self._allocatedCapital
        #Adding the day's total capital to the timeCapital list for performance tracking
        self._timeCapital.append(self._totalCapital)
        
    #Defining the method used to check whether the stop losses of any positions were hit
    def checkStops(self, current_date, current_price):
        for ind in (self._openPositions):
            #If the current price is below the stop price, close the position and print out the loss message in red
            if ind.getStopPrice() >= current_price:
                self.closePosition(current_date, current_price)
                print("\033[3;31mPosition bought on ", ind.getBoughtDate(), " hit sell stop and was sold for a loss of: ", ((current_price - ind.getBuyPrice()) * ind.getPositionSize()), "\033[0;0m")
            
    #Defining the method used to check whether the profit targets of any positions were hit
    def checkTargets(self, current_date, current_price):
        for ind in (self._openPositions):
            #If the current price is above the profit target, close the position and print out the profit message in green
            if ind.getTargetPrice() <= current_price:
                self.closePosition(current_date, current_price)
                print("\033[3;32mPosition bought on ", ind.getBoughtDate(), " hit profit target and was sold\033[0;0m")

    #Defining the method used to check whether any positions had lifespans run out
    def checkLifespans(self, current_date, current_price):
        for ind in (self._openPositions):
            #If the lifespan has hit 0, close the position and print out the lifespan message in yellow
            if ind.getLifespan() <= 0:
                self.closePosition(current_date, current_price)
                print("\033[3;33mPosition bought on ", ind.getBoughtDate(), " hit its lifespan and was sold\033[0;0m")


    

            
            





