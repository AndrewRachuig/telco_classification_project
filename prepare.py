import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# train test split from sklearn
from sklearn.model_selection import train_test_split

def split_telco(df):
    '''
    Takes in a prepped telco dataframe, splits it into train, validate and test subgroups stratifying it on the target
    of churn and then returns those subgroups.
    
    Arguments: df - a cleaned pandas dataframe with the expected feature names and columns in the telco dataset
    Return: train, validate, test - dataframes ready for the exploration and model phases.
    '''
    train, test = train_test_split(df, train_size = 0.8, stratify = df.churn_Yes, random_state = 1234)
    train, validate = train_test_split(train, train_size = 0.7, stratify = train.churn_Yes, random_state = 1234)
    return train, validate, test


def clean_telco(df):
    '''
    Takes in a dirty telco dataframe and returns a cleaned/transformed telco dataframe.

    Arguments: df - a pandas dataframe with the expected feature names and columns as acquired from the acquire.py script.
    Return: cleaned_telco - a dataframe with various cleaning operations performed on it.
    '''

    # This finds all "nulls" in the total_charges column which take the form of an empty space ' ' here since this is an object column, 
    # and replaces them with zeros and then converts the column to a numeric one.

    df.total_charges.replace(' ', '0', inplace=True)
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

    # From exploring the data, I found that the columns internet_service_type, payment_type, and contract_type all correspond
    # direclty to internet_service_type_id, payment_type_id, and contract_type_id; additionally, the information in the 
    # phone_service column is 100% reproduced with ADDITIONALY info in the multiple_lines column.  Thus I will be dropping 
    # internet_service_type_id, payment_type_id, contract_type_id, and phone_service as redundant columns.

    df.drop(columns = ['internet_service_type_id', 'payment_type_id', 'contract_type_id', 'phone_service'], inplace=True)

    # From exploring the data, I found there are 11 total customers who have 0 total_charges and 11 total customers who
    # have a tenure of 0. All customers who had a tenure of total charges and tenure of 0 did not churn. Since they have no possiblity 
    # of churning yet, I'm dropping these eleven customers from the dataset to make the data cleaner.

    df.drop(df[df.total_charges == 0].index, inplace=True)

    # Dropping any duplicates.
    df.drop_duplicates(inplace=True)

    return df

def encode_telco(df):
    '''
    This function takes in a cleaned telco dataframe and using one-hot encoding, encodes categorical variables. It does not drop the original
    categorical columns. This is done purposefully to allow for easier Exploratory Data Analysis.  Removal of original categorical columns
    will be done in a separate function 'drop_pre_encoded'.

    Arguments: df - a cleaned telco dataframe with the expected feature names and columns
    Returns: encoded - a telco dataframe with all desired categorical columns encoded.
    '''
    dummies_list = df.select_dtypes(object).columns
    dummies_list = dummies_list.drop('customer_id')

    dummy_df = pd.get_dummies(df[dummies_list], drop_first=True)
    encoded = pd.concat([df, dummy_df], axis = 1)
    return encoded


def cat_hists(df):
    ''' This function takes in the raw telco dataframe and prints histograms for each of the categorical columns (minus total_charges
    which has not been changed yet) in the telco dataset. This will give me a good sense of how each categorical column is shaped. 
    '''

    cat_cols = df.select_dtypes('object').columns
    cat_cols = cat_cols.drop('total_charges')


    for col in cat_cols:
        sns.histplot(df[col])
        plt.show()
        print(f"Count of variables in {col}: \n{df[col].value_counts()}\n--------------------")