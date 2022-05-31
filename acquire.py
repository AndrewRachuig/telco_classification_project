import env
import pandas as pd
import os


def get_telco_data():
    ''' This function allows access to the requisite telco dataset. It accesses a local cache of the data if there is a 
    local copy stored. If no local copy exists, it uses credentials stored in env.py to make a call to the SQL 
    database, returns the data and then creates a local cached copy in a .csv file so as to not need to query the SQL 
    database in the future. 
    
    The stored local copy is called telco.csv 
    
    If at any point a fresh copy of the SQL database is needed, the original cached .csv must be deleted.
    
    Returns: a dataframe of the telco data.
    '''
    
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT * 
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id);     
        '''
        url = env.get_db_url('telco_churn')
        df = pd.read_sql(query, url)
        df.to_csv(filename, index=False)

        return df  

# Small function getting me a value_count of all object columns; this gives me a preliminary look at the data.
def obj_val_cnt(df):
    ''' This function takes in a raw telco dataframe and prints out value counts for each object column
    '''
    for col in df.columns:
        if df[col].dtype == 'object':
            print(df[col].value_counts(dropna=False))


# This function gives me a dataframe with summary statistics with range added on the end.
def describe_with_range(df):
    '''This function takes in a raw telco dataframe and returns a dataframe containingsummary statistics for numerical columns with 
    range added on the end.
    '''
    summary_stats = df.describe().T
    summary_stats['range'] = summary_stats['max'] - summary_stats['min']
    return summary_stats
    