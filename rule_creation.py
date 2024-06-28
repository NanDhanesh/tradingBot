#Nandan Dhanesh
#Initialisation of rule objects

import rule_class as grc
import buy_rule_class as brc

#Creating the general rule object 'confidence rule' to regulate trade all recommendations
confidence_rule = grc.GenRule('Confidence', 'If confidence is below 45%, do not execute recommendation')

#Creating the two buy/sell rule objects that regulate buy recommendations
buy_rule_1 = brc.BuySellRule('Buy Rule 1', 'If unallocated capital is below 35% of total capital, do not buy', 'Buy')
buy_rule_2 = brc.BuySellRule('Buy Rule 2', 'If cost of a new positions is greater than unallocated capital, do not buy', 'Buy')

#Creating the buy/sell rule objects that regulates sell recommendations
sell_rule_1 = brc.BuySellRule('Sell Rule 1', 'If number of positions in portfolio is below 1, do not sell', 'Sell')

#Defining a function to check if the general rule and both buy rules are met before executing a buy recommendation
def check_buy(confidence, total_capital, un_capital, stock_price, position_size):
    if confidence_rule.checkRule(confidence, 0.5) == True and buy_rule_1.checkRule(un_capital/total_capital, 0.35) == True and buy_rule_2.checkRule(un_capital, stock_price * position_size) == True:
        return True
    else:
        return False

#Defining a function to check if both the general rule and sell rule are met before executing a sell recommendation
def check_sell(confidence, num_positions):
    if confidence_rule.checkRule(confidence, 0.45) == True and sell_rule_1.checkRule(num_positions, 1) == True:
        return True
    else:
        return False