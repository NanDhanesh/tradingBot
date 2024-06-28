#Nandan Dhanesh
#General rule class

#Creating the class for general rules (not buy or sell specific)
class GenRule:
    #Initialising and defining class attributes
    def __init__(self, name, condition):
        self._name = name 
        self._condition = condition

    #Defining two getter methods for the class
    def getName(self):
        return self._name

    def getCondition(self):
        return self._condition

    #Defining CheckRule method to check if the rule is met or not 
    def checkRule(self, value_check, benchmark):
        if value_check < benchmark:
            return False
        else:
            return True



