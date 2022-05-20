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