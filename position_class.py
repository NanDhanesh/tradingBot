#Nandan Dhanesh
#Defining the position class

#Creating the class to be used for each trading position
class Position:
    def __init__(self, bought_date, buy_price, position_size):
        #Initialising all attributes
        self._boughtDate = bought_date
        self._soldDate = 0
        self._buyPrice = buy_price
        self._sellPrice = 0
        self._stopPrice = (buy_price * 0.95) #Stop loss is 5% below buy price
        self._targetPrice = (buy_price * 1.1) #Profit target is 5% above buy price #Changed
        self._lifespan = 10
        self._positionSize = position_size

    #Defining all getter methods
    def getBuyPrice(self):
        return self._buyPrice

    def getSellPrice(self):
        return self._sellPrice

    def getBoughtDate(self):
        return self._boughtDate

    def getSoldDate(self):
        return self._soldDate

    def getStopPrice(self):
        return self._stopPrice

    def getTargetPrice(self):
        return self._targetPrice

    def getLifespan(self):
        return self._lifespan

    def getPositionSize(self):
        return self._positionSize

    #Defining setter methods for closing positions and position maintenance
    def setSoldDate(self, sold_date):
        self._soldDate = sold_date
    
    def setSellPrice(self, sell_price):
        self._sellPrice = sell_price

    def incrementLifespan(self):
        self._lifespan += -1
