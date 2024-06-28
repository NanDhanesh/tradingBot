#Nandan Dhanesh
#Buy and sell rules

import rule_class as grc

#Forming the class for buy and sell rules
class BuySellRule(grc.GenRule):
    #Initialising with attributes name, condition, and type
    def __init__(self, name, condition, type):
        #Inheriting name and condition attributes from Gen_rule (general rule)
        super().__init__(name, condition)
        self._type = type

    #Defining a new method specific to buy and sell rules
    def getType(self):
        return self._type




