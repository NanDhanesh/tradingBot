#Nandan Dhanesh
#Importing data with yfinance and calculating features for final DataFrame

import yfinance as yf
import numpy as np

# Creating a DataFrame of selected ticker
def import_data(symbol):

    ticker = yf.Ticker(symbol) #Initialises a ticker variable for the chosen stock 'symbol'
    df_source = ticker.history(period = 'max') #Forms the Pandas DataFrame 'df_source' with imported data from yfinance for the max time period

    if df_source.empty: #If no data is found (incorrect symbol), return empty Dataframe for validation to take place
        return df_source

    df_source.replace([np.inf, -np.inf], np.nan, inplace=True) #Replacing any infinite values with null values
    df_source.dropna(inplace=True) #Removing all rows with null values (erroneous data)
    df_source = df_source[df_source.Open != 0]   #Removing all rows that have 0 values for the 4 core metrics (erroneous data)
    df_source = df_source[df_source.Volume != 0]
    df_source = df_source[df_source.High != 0]
    df_source = df_source[df_source.Low != 0]

    #Creating all of the lists that need to be used later
    days = []                   #Lists used for intermediate calculations
    change = []                 
    opens = []                  
    dates = []                  
    change_labels = []          
    highs = []
    lows = []
    closes = []
    week_start_opens = []
    week_mean_volumes =[]       #^^^^^^^^^^^^^^^^^^
    volume = []                 #List for Feature 0
    high_low_spread = []        #List for Feature 1
    prev_change =[]             #List for Feature 2
    pre_market = []             #List for Feature 3
    volume_change = []          #List for Feature 4
    high_change = []            #List for Feature 5
    low_change = []             #List for Feature 6
    week_start_change = []      #List for Feature 7
    avg_week_vol_change = []    #List for Feature 8
    end_week_vol_change =[]     #List for Feature 9
    prev_week_vol_change = []   #List for Feature 10

    counter = 0 #Initialises a counter for use in a later calculation

    #Iterates through each row and adds the metrics to their relevant lists
    for ind in (df_source.index):
        days.append(ind.day)
        dates.append(ind)
        opens.append(df_source['Open'][ind])
        volume.append(df_source['Volume'][ind])
        highs.append(df_source['High'][ind])
        lows.append(df_source['Low'][ind])
        closes.append(df_source['Close'][ind])

    weeks = [[days[0]]] #Creating list for days of the week
    week_starts = [] #Creating list for first days of each week

    #########################################################################################################################
    #                               Calculating each feature's values below this line                                       #
    #########################################################################################################################

    #########################################################################################################################
    #                                                   Feature 1                                                           #
    #########################################################################################################################

    #Calculating the percentage difference between the high of each day and the low of each day (feature 1)
    for i in range(1,len(highs)-2):
        high_low_spread.append(((highs[i]-lows[i])/lows[i])*100)

    #########################################################################################################################
    #                                                   Feature 2                                                           #
    #########################################################################################################################

    #Calculates the percentage change in open prices from one day to next day (feature 2)
    for i in range(2,len(df_source.index)-1):
        change.append((((opens[i+1]-opens[i])/opens[i]))*100)
    
    #########################################################################################################################
    #                                                   Feature 3                                                           #
    #########################################################################################################################

    #Calculating the price change of the previous day and the pre_market change from the previous day to the current day (feature 3)
    for i in range(1, len(closes)-2):
        prev_change.append(((closes[i]-opens[i])/opens[i])*100)
        pre_market.append(((opens[i+1]-closes[i])/closes[i])*100)

    #########################################################################################################################
    #                                                 Features 4,5,6                                                        #
    #########################################################################################################################

    #Calculating features 4, 5, 6
    for i in range((len(volume)-3)):
        high_change.append(((highs[i+1]-highs[i])/highs[i])*100)#Calculating the percentage change in the high price 
        low_change.append(((lows[i+1]-lows[i])/lows[i])*100)#Calculating the percentage change in the low price
        if volume[i] == 0:
            volume_change.append(0)#To avoid division by 0, assigning 0% change
        else:
            volume_change.append(((volume[i+1]-volume[i])/volume[i])*100)#Calculating volume change between days

    #########################################################################################################################
    #                                              Used for features 7-10                                                   #
    #########################################################################################################################

    #Adds each week's worth of days as a list to list 'weeks'
    for i in range(1,(len(days))): 
        if (days[i]) != (days[i-1]+1):
            weeks.append([days[i]])
        else:
            weeks[len(weeks)-1].append(days[i])
        
    day_week_volume = weeks #Initialising 'day_week_volume' as a copy of 'weeks'

    #Adding the volume of each day of each week to a list within the list 'day_week_volume'
    for i in range(len(weeks)): 
        for y in range(len(weeks[i])):
            day_week_volume[i][y] = volume[counter] #Replacing default values stored in 'day_week_volumes'
            counter += 1
    
    #########################################################################################################################
    #                                                   Feature 7                                                           #
    #########################################################################################################################

    #Adds the start day of each week to list 'week_starts' (used for feature 7)
    for i in range(len(weeks)):
        week_starts.append(weeks[i][0])
        for i in range(len(weeks[i])-1):
            week_starts.append(0)


    #Adds the open price of each week to list 'week_start_opens' (used for feature 7)
    for i in range(len(week_starts)):
        if week_starts[i] != 0:
            week_start_opens.append(opens[i])
        else:
            week_start_opens.append(0)
    
    #Adds the open price of each week as an element for each day in that week (used for feature 7)
    for i in range((len(week_start_opens))-1):
        if week_start_opens[i] != week_start_opens[i+1] and week_start_opens[i+1] == 0:
            week_start_opens[i+1] = week_start_opens[i]

    #Calculates percentage change from week open to day of the week open (feature 7)
    for i in range(2,len(opens)-1):
        week_start_change.append(((opens[i]-week_start_opens[i])/week_start_opens[i])*100)

    #########################################################################################################################
    #                                                   Feature 8                                                           #
    #########################################################################################################################

    #Adding the mean daily volume upto each day of each week to a list within a the list (used for feature 8 and 9)
    for i in range(len(day_week_volume)): 
        volume_count = 0
        week_mean_volumes.append([])
        for y in range(len(day_week_volume[i])):
            volume_count += day_week_volume[i][y]
            week_mean_volumes[i].append(volume_count/(y+1))

    #For each day in each week, adding the mean volume up to the same day in the previous week to list 'avg_week_vol_change' (feature 8)
    for i in range(len(weeks[0])):
        avg_week_vol_change.append(0) #For the first week, add 0's as placeholders as there is no previous week
    for i in range(1,len(weeks)): 
        for y in range(len(weeks[i])):
            if y == 0:
                avg_week_vol_change.append(0) #For the first day of each week, use value 0% as there is no previous day
            elif len(weeks[i]) <= len(weeks[i-1]) and week_mean_volumes[i-1][y-1] != 0:
                avg_week_vol_change.append(((week_mean_volumes[i][y-1] - week_mean_volumes[i-1][y-1])/week_mean_volumes[i-1][y-1])*100)
            elif len(weeks[i]) > len(weeks[i-1]) or week_mean_volumes[i-1][y-1] == 0: #If there are fewer days in the week prior, just add the final mean volume for that week
                avg_week_vol_change.append(0)

    #########################################################################################################################
    #                                                   Feature 9                                                           #
    #########################################################################################################################

    #Measuring the percentage change between the mean daily voume of the week before and the extrapolated mean for the current week (feature 9)
    for i in range(len(week_mean_volumes[0])):
        end_week_vol_change.append(0) #For the first week, add 0's as placeholders as there is no previous week
    for i in range(1,len(week_mean_volumes)): 
        for y in range(len(week_mean_volumes[i])):
            if y == 0: 
                end_week_vol_change.append(0) #For the first day of each week, there will be no extrapolated mean so add 0% change
            elif (week_mean_volumes[i-1][-1]) != 0:
                end_week_vol_change.append(((week_mean_volumes[i][y-1]-week_mean_volumes[i-1][-1])/week_mean_volumes[i-1][-1])*100)
            elif (week_mean_volumes[i-1][-1]) == 0: #To avoid division by 0, add 0% change 
                end_week_vol_change.append(0)

    #########################################################################################################################
    #                                                   Feature 10                                                          #
    #########################################################################################################################

    #Measuring the change between the volume of the day before and the volume of the same day in the week before (feature 10)
    for i in range(len(day_week_volume[0])):
        prev_week_vol_change.append(0) #For the first week, add 0's as placeholders as there is no previous week
    for i in range(1,len(day_week_volume)): 
        for y in range (len(day_week_volume[i])):
            if y == 0: #For the first day of each week, there is no volume of the day before so add 0% change
                prev_week_vol_change.append(0) 
            elif len(day_week_volume[i]) <= (len(day_week_volume[i-1])) and day_week_volume[i-1][y-1] != 0: 
                prev_week_vol_change.append(((day_week_volume[i][y-1]-day_week_volume[i-1][y-1])/day_week_volume[i-1][y-1])*100)
            elif (len(day_week_volume[i])) > (len(day_week_volume[i-1])): #If the current week is longer than the previous week, add 0% to keep within range
                prev_week_vol_change.append(0)
            elif day_week_volume[i-1][y-1] == 0: #To avoid division by 0, add 0% if the chosen day in the week before has volume of 0
                prev_week_vol_change.append(0)
    

    #########################################################################################################################
    #                               Formatting DataFrame for final output below this line                                   #
    #########################################################################################################################

    #Removes the volumes of the last two days and the first day of trading in the dataframe, creating feature 0
    volume.pop(0)
    for i in range(2):
        volume.pop(-1)


    def advanced_formatting(feature_list): #Formatting for the 3 advanced features (8,9,10) by removing 3 values each
        feature_list.pop(-1) 
        feature_list.pop(1)
        feature_list.pop(0)

    advanced_formatting(avg_week_vol_change) #Formatting feature 8 for DataFrame
    advanced_formatting(end_week_vol_change) #Formatting feature 9 for DataFrame
    advanced_formatting(prev_week_vol_change) #Formatting feature 10 for DataFrame
        
    #Removes the last and first two rows in the dataframe
    df_source.drop((dates[-1]), inplace = True)
    df_source.drop((dates[1]), inplace = True)
    df_source.drop((dates[0]), inplace = True)

    #Adds each of the features as columns to the DataFrame
    df_source['Change'] = change                                #Used for labels
    df_source['Prev_Vol'] = volume                              #Feature 0
    df_source['Prev_Day_High_Low_Spread'] = high_low_spread     #Feature 1
    df_source['Prev_Day_Price_Change'] = prev_change            #Feature 2
    df_source['Pre_Market_Change'] = pre_market                 #Feature 3
    df_source['Prev_Day_Vol_Change'] = volume_change            #Feature 4
    df_source['High_Change'] = high_change                      #Feature 5
    df_source['Low_Change'] = low_change                        #Feature 6
    df_source['Open_Week_Spread'] = week_start_change           #Feature 7
    df_source['Avg_Week_Vol_Change'] =  avg_week_vol_change     #Feature 8
    df_source['End_Week_Vol_Change'] =  end_week_vol_change     #Feature 9
    df_source['Prev_Week_Vol_Change'] = prev_week_vol_change    #Feature 10

    #Removes two unwanted columns that were imported by yfinance
    df_source.drop('Dividends', inplace=True, axis=1)
    df_source.drop('Stock Splits', inplace=True, axis=1)

    #Iterates through the dataframe to create labels for each day 
    for ind in (df_source.index):
        if (df_source['Change'][ind]) > 0.5:
            change_labels.append(2) #Adds 'buy' label to list of labels
        elif (df_source['Change'][ind]) < -0.5: 
            change_labels.append(0) #Adds 'sell' label to list of labels
        else:
            change_labels.append(1) #Adds 'hold' label to list of labels

    df_source['Labels'] = change_labels #Creates 'Labels' column in DataFrame for the labels

    return(df_source)

