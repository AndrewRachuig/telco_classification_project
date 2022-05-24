import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

def normality_testing(train_explore):
    '''This function takes in a train subset of the data and visualizes the shape the tenure, total_charges, and monthly_charges
    specifically looking for normality.
    It then runs a levene test for equal variance and prints out the results under the accompanying visualization.'''

    for num in ['tenure', 'total_charges', 'monthly_charges']:
        plt.figure(figsize=(10,3))
        sns.histplot(data=train_explore[train_explore.churn == 'No'][num])
        sns.histplot(data=train_explore[train_explore.churn == 'Yes'][num], color='orange')
        stat, p = stats.levene(train_explore[train_explore.churn == 'Yes'][num], train_explore[train_explore.churn == 'No'][num])
        plt.show()
        print(f'The levene test for {num} when comparing churn vs no churn shows a p value of {p} \nwhich means the variance is not equal.')


def explore_categoricals(df, target, alpha = .05, only_report=False):
    '''
    This function takes in a subset of the train dataframe which contains on the categorical variable columns and runs a Chi 
    Test of Independence on all variables in comparison to the target variable. It prints the null and alternative hypotheses
    for each comparison and displays results indicating whether the results reject or fail to reject the null hypothesis based
    on the supplied alpha.  Returns a dataframe containing the variable (feature) name and the p value of chi2 test for all 
    variables having a p < alpha.
    
    Arguments:
                df - a subset of the train dataframe containing ONLY categorical variables
                target - specifies the target variable to compare with all other variables in the subset df
                alpha - a specified alpha for statistical significance. Default set to .05
                only_report - if set to True only prints out the lists reporting statistical signficance or not.
                
    Return: dataframe with variable names and p value results from the chi2 test for all variables where p < alpha.
    
    '''
    if only_report == True:
        stat_significant = []
        p_value= []
        not_stat_significant = []
        a = alpha
        explore_cat = df
        for col in explore_cat.columns:
            observed = pd.crosstab(df[col], df[target])
            chi2, p, degf, expected = stats.chi2_contingency(observed)
            if p < a:
                stat_significant.append(col)
                p_value.append(p)
            else:
                not_stat_significant.append(col)
    
        print(f"Statistically signficant relationships with the target variable ({target}) were found with the following features:")
        print(stat_significant)
        print("----------------------------------\n")
        print(f"Statistically signficant relationships with the target variable ({target}) were NOT found with the following features:")
        print(not_stat_significant)

    else:
        print("Exploring relationships between categorical variables and the target categorical variable.")
        print("----------------------------------\n")
        stat_significant = []
        p_value= []
        not_stat_significant = []
        a = alpha
        explore_cat = df
        for col in explore_cat.columns:
            print(f"Null Hypothesis: There is no relationship between {col} and {target}.")
            print(f"Alternative Hypothesis: There is a relationship between {col} and {target}.")
            print("\n")
            print("Results of Chi Squared Test of Independence")
            observed = pd.crosstab(df[col], df[target])
            chi2, p, degf, expected = stats.chi2_contingency(observed)
            if p < a:
                print(f"P ({p}) is less than alpha ({a}).\n")
                print(f"I reject the null hypothesis. There is a statistically significant relationship between {col} and {target}.")
                stat_significant.append(col)
                p_value.append(p)
            else:
                print(f"P ({p}) is more than alpha ({a}).\n")
                print(f"I fail to reject the null hypothesis that there is no relationship between {col} and {target}.")
                not_stat_significant.append(col)
            print("\n----------------------------------\n")
        
        print(f"Statistically signficant relationships with the target variable ({target}) were found with the following features:")
        print(stat_significant)
        print("----------------------------------\n")
        print(f"Statistically signficant relationships with the target variable ({target}) were NOT found with the following features:")
        print(not_stat_significant)
    return pd.DataFrame({"feature": stat_significant, "p_value": p_value})
