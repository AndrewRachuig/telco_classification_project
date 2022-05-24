# <center>Upturn in Churn an Urgent Concern </center>

<img src="img/leaky_customers.jpg" width=600 height=600 />

## Project Summary

### Project Objectives

- Provide a Jupyter Notebook with the following:
    - Data Acquisition
    - Data Preparation
    - Exploratory Data Analysis
        - Statistical testing where needed for exploration of data 
    - Model creation and refinement
    - Model Evaluation
    - Conclusions and Next Steps
- Creation of python modules to assist in the entire process and make it easily repeatable.
    - acquire.py
    - prepare.py
    - explore.py
    - model.py
- Ask exploratory questions of the data that will give an understanding about the attributes and drivers of customers churning.     
    - Answer questions through charts and statistical tests.
- Construct the best possible model for predicting customer churn.
    - Make predictions for a group of customers.
- Adequately document and annotate all code.
- Give a 5 minute presentation to a group of collegues and managers covering the final notebook deliverable with a walkthrough of work I did, why, goals, what you found, your methdologies, and my conclusions.
- Field questions from instructors and peers about my specific code, approach to the project, findings and model.

### Business Goals
- Identify features from the dataset which may be driving churn. **Why are customers churning?**
- Construct a ML classificationmodel which accurately predicts which customers will churn.
- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and the resulting outcome.

### Audience
- My target audience for my notebook walkthrough is my direct manager and their manager. 

### Project Deliverables
- A github readme explaining the project
- A jupyter notebook containing my final report (properly documented and commented)
- All modules containing functions created to achieve the final report notebook
- A csv file containing customer_id, probability of churn, and prediction of churn by using my final model on the test dataset.
- 1+ non-final notebook (s) created while working on the project, containing exploration & modeling work (and other work)
- A presentation of final report notebook

### Project Context
- The telco data I'm using came from the Codeup database

### Data Dictionary

Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn | 7043 non-null: object | customer churn Yes or No |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| internet_service_type_id       | 7043 non-null: int64 |    id refering to type of internet service used |
| payment_type_id        | 7043 non-null: int64 |    id refering to type of payment used |
| contract_type_id       | 7043 non-null: int64 |    id refering to type of contract used |
| customer_id        | 7043 non-null: object |    individual customer id string |
| gender       | 7043 non-null: object |    customer male or female |
| senior_citizen        | 7043 non-null: int64 |    is customer senior |
| partner       | 7043 non-null: object |    does customer have a partner |
| dependents        | 7043 non-null: object |    does customer have dependents |
| tenure       | 7043 non-null: int64 |    length customer with company in months |
| phone_service        | 7043 non-null: object |    Yes or No |
| multiple_lines       | 7043 non-null: object |    Yes, No, or No phone service |
| online_security        | 7043 non-null: object |    Yes, No, No internet service |
| online_backup       | 7043 non-null: object |    Yes, No, No internet service |
| device_protection        | 7043 non-null: object |    Yes, No, No internet service |
| tech_support       | 7043 non-null: object |    Yes, No, No internet service |
| streaming_tv        | 7043 non-null: object |    Yes, No, No internet service |
| streaming_movies       | 7043 non-null: object |    Yes, No, No internet service |
| paperless_billing        | 7043 non-null: object |    Yes or No |
| monthly_charges       | 7043 non-null: float64 |    monthly bill amount in USD |
| total_charges        | 7043 non-null: object |    lifetime total charged to customer in USD  |
| contract_type       | 7043 non-null: object |    One Year, Two Year, Month-to-month |
| payment_type        | 7043 non-null: object |    Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)|
| internet_service_type       | 7043 non-null: object |    Fiber optic, DSL, None |
