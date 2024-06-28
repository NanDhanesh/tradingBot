#Nandan Dhanesh
#Random forest classifier 

#Import Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
#Import data handling library pandas
import pandas as pd


def classify(df_source, feature_set):
        
    df_testing = df_source.tail(300) #Forming the dataframe with the data to be traded on (last 300 days of data)
    df_training = df_source.drop(df_source.index[-300:]) #Forming the dataframe with the data to be trained on 

    X_train = df_training[feature_set]  #Identifying which columns of the training dataframe will act as features   
    y_train = df_training['Labels']  #Identifying which column of the training dataframe will act as the label

    X_test = df_testing[feature_set] #Identifying which columns of the testing dataframe will act as features
    y_test = df_testing['Labels'] #Identifying which column of the testing dataframe will act as the label

    #Initialising a Random Forest Classifier as 'classifier' with the 3 optimised hyperparameters 
    classifier=RandomForestClassifier(n_estimators=100, max_depth=8, max_leaf_nodes=100)

    #Train the model using the training set
    classifier.fit(X_train,y_train)

    #Use the model to predict the labels of the testing data (trade decisions)
    y_pred=classifier.predict(X_test)
    #Getting the probability (confidence) of each of the model's predictions
    probabilities = classifier.predict_proba(X_test)

    high_prob = [] #Defining the list for the probability of each day's classification (highest of 3 probabilities)

    for i in range(len(probabilities)):
            high_prob.append(probabilities[i][y_pred[i]])#Chooses the day's highest probability to correspond with the prediction

    dates = df_testing.index #Create a list with the date of each trading day

    data = {'Date' : dates, #Adds column name 'Date' with the dates
            'Recommendation' : y_pred, #Adds column name 'Recommendation' with trade recs
            'Probability' : high_prob, #Adds column name 'Probability' with confidence of rec
            'Open Price' : df_testing['Open']} #Adds column name 'Open Price' with open price of each day
    df_recommendation = pd.DataFrame(data) #Creating the dataframe of trade recommendation


    return df_recommendation













