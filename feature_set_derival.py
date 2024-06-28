#Nandan Dhanesh
#Optimum feature set derival

#Choosing the optimum feature set for the chosen stock depending on its ticker symbol
def optimum_feature_set(symbol):
    if symbol == 'AAPL':
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','High_Change','Low_Change','Open_Week_Spread','End_Week_Vol_Change','Prev_Week_Vol_Change']
    elif symbol == 'SPY':
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','High_Change','Low_Change','Open_Week_Spread']
    elif symbol == 'META':
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','Low_Change','Open_Week_Spread','Avg_Week_Vol_Change']
    elif symbol == 'WMT':
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','High_Change','Low_Change']
    elif symbol == 'SBUX':
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','High_Change','Low_Change','Avg_Week_Vol_Change']
    else:
        feature_set = ['Prev_Vol','Prev_Day_High_Low_Spread','Prev_Day_Price_Change','Pre_Market_Change','Prev_Day_Vol_Change','High_Change','Low_Change','Open_Week_Spread','Avg_Week_Vol_Change','End_Week_Vol_Change','Prev_Week_Vol_Change']
    return(feature_set)