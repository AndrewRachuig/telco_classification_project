import pandas as pd
import numpy as np
import scipy.stats as stats

# Visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

# Modeling imports
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC


def pre_model(train, validate, test, drop_columns_list = []):
    '''
    This function does any final preparation necessary prior to modeling. It takes in the train, validate, test subsets made 
    previously does transformations (e.g. dropping non-encoded columns) and returns the final versions of train, validate, test.
    
    Arguments:
        train - a subset of the entire dataframe, previously split, to be used for training my models
        validate - a subset of the entire dataframe, previously split, to be used for validation of my models
        test - a subset of the entire dataframe, previously split, to be used for testing my final model
        drop_columns_list = a list of columns determined during EDA to not be useful features for modeling
   
   Returns: train, validate, test dataframes ready for modeling
    '''
    # makes a list of unencoded columns to drop PLUS puts customer_id back in (this is necessary for a later step 
    # involving customer_id)
    unencoded_train_to_drop = train.select_dtypes('object').columns
    unencoded_train_to_drop = unencoded_train_to_drop.drop('customer_id')
    
    unencoded_validate_to_drop = validate.select_dtypes('object').columns
    unencoded_validate_to_drop = unencoded_validate_to_drop.drop('customer_id')
    
    unencoded_test_to_drop = test.select_dtypes('object').columns
    unencoded_test_to_drop = unencoded_test_to_drop.drop('customer_id')
    
    
    # Drops all unencoded columns
    train = train.drop(columns = (unencoded_train_to_drop))
    validate = validate.drop(columns = (unencoded_validate_to_drop))
    test = test.drop(columns = (unencoded_test_to_drop))
    
    # Drops columns in the drop_columns_list
    train = train.drop(columns = drop_columns_list)
    validate = validate.drop(columns = drop_columns_list)
    test = test.drop(columns = drop_columns_list)
    
    return train, validate, test


def max_depth_iterator(X_train, y_train, X_validate, y_validate):
    '''This is a function to test how max_depth affects the accuracy of the decision tree model on both the training and the validate 
    set to hopefully find the optimal depth.
    
    Arguments: 
        X_train - this is the X_train data
        y_train - this is the y_train data
        X_validate - this is the X_validate data
        y_validate - this is the y_validate data
    '''
    for n in range(1,15):
        clf = DecisionTreeClassifier(max_depth=n, random_state=123)
        clf.fit(X_train, y_train)
        print(f'Accuracy of Decision Tree classifier on training set with a max_depth of {n}: {round(clf.score(X_train, y_train),4)*100}%')
        print(f'Accuracy of Decision Tree classifier on validate set with a max_depth of {n}: {round(clf.score(X_validate, y_validate),4)*100}%')
        print("-----------------------------------")



def rf_iteration(X_train, y_train, X_validate, y_validate, trees = 100):
    ''' This function runs through both max_depth, and min_sample_leaf to give me a better idea of what are the best hyperparamters 
    to choose for a random forest model. I can also come back to it later and tweak n_estimators for further customization.

     Arguments: 
        X_train - this is the X_train data
        y_train - this is the y_train data
        X_validate - this is the X_validate data
        y_validate - this is the y_validate data
        trees - This is the number of n_estimators to use. Default set at 100

    Returns: A dictionary with the results of all the iterations.   
    '''
    results = {}
    max_depth = []
    min_samples_leaf = []
    Train_accuracy = []
    Validate_accuracy = []
    Train_Validate_diff = []
    for x in range(1,16):
        for y in range(1,16):
            rf = RandomForestClassifier(max_depth=x, random_state=123, min_samples_leaf = y, n_estimators = trees)
            rf.fit(X_train, y_train)
            max_depth.append(x)
            min_samples_leaf.append(y)
            Train_accuracy.append(rf.score(X_train, y_train))
            Validate_accuracy.append(rf.score(X_validate, y_validate))
            Train_Validate_diff.append(rf.score(X_train, y_train) - rf.score(X_validate, y_validate))
    results = {"max_depth": max_depth, "min_samples_leaf" : min_samples_leaf, "Train_accuracy" : Train_accuracy, "Validate_accuracy" : Validate_accuracy, "Train_Validate_diff" : Train_Validate_diff}
    return results


def knn_results(X_train, y_train, X_validate, y_validate):
    ''' This function iterates through knn model n_neighbors to see with value finds the best results. It returns a dictionary of said results.
    
     Arguments: 
        X_train - this is the X_train data
        y_train - this is the y_train data
        X_validate - this is the X_validate data
        y_validate - this is the y_validate data
        trees - This is the number of n_estimators to use. Default set at 100

    Returns: A dictionary with the results of all the iterations.   
    '''
    results = {}
    K = []
    Train_accuracy = []
    Validate_accuracy = []
    Train_Validate_diff = []
    for x in range(1,21):
        knn = KNeighborsClassifier(n_neighbors=x, weights='uniform')
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_train)
        K.append(x)
        Train_accuracy.append(knn.score(X_train, y_train))
        Validate_accuracy.append(knn.score(X_validate, y_validate))
        Train_Validate_diff.append(knn.score(X_train, y_train) - knn.score(X_validate, y_validate))
    results = {"K" : K, "Train_accuracy" : Train_accuracy, "Validate_accuracy" : Validate_accuracy, "Train_Validate_diff" : Train_Validate_diff}
    return results


def rf_super(X_train, y_train, X_validate, y_validate):
    '''This function is essentially a super iterator for a random forest model in which it goes through the following hyperparameters iteratively
    to find the optimal resulting model: max_depth, min_samples_leaf, n_estimators, criterion, min_samples_split. See below for ranges.

    Warning: This takes a LONG time to iterate through. I recommend saving resulting dataframe to csv instead of rerunning again later.

    Arguments: 
        X_train - this is the X_train data
        y_train - this is the y_train data
        X_validate - this is the X_validate data
        y_validate - this is the y_validate data
        trees - This is the number of n_estimators to use. Default set at 100

    Returns: A dictionary with the results of all the iterations.   
'''

    results = {}
    max_depth = []
    min_samples_leaf = []
    n_estimators = []
    criterion = []
    min_samples_split = []
    
    Train_accuracy = []
    Validate_accuracy = []
    Train_Validate_diff = []
    features_dropped = []
    
    for depth in range(1,16):
        for leaf in range(1,8):
            for split in range(2, 10):
                for tree in [100, 500, 1000]:
                    for crit in ['gini', 'entropy']:

                        rf = RandomForestClassifier(max_depth=depth, min_samples_split=split, random_state=123, 
                                                    min_samples_leaf = leaf, n_estimators = tree, criterion= crit)
                        rf.fit(X_train, y_train)

                        max_depth.append(depth)
                        min_samples_leaf.append(leaf)
                        min_samples_split.append(split)
                        n_estimators.append(tree)
                        criterion.append(crit)

                        Train_accuracy.append(rf.score(X_train, y_train))
                        Validate_accuracy.append(rf.score(X_validate, y_validate))
                        Train_Validate_diff.append(rf.score(X_train, y_train) - rf.score(X_validate, y_validate))
    
    results = {"max_depth": max_depth, "min_samples_leaf" : min_samples_leaf, "min_samples_split" : min_samples_split,
               "n_estimators" : n_estimators, "criterion" : criterion, "Train_accuracy" : Train_accuracy, 
               "Validate_accuracy" : Validate_accuracy, "Train_Validate_diff" : Train_Validate_diff}
    
    return results

