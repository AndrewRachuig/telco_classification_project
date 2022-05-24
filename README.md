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
| phone_service        | 7043 non-null: object |    uses phone service Yes or No |
| multiple_lines       | 7043 non-null: object |    Yes, No, or No phone service |
| online_security        | 7043 non-null: object |    Yes, No, No internet service |
| online_backup       | 7043 non-null: object |    Yes, No, No internet service |
| device_protection        | 7043 non-null: object |    Yes, No, No internet service |
| tech_support       | 7043 non-null: object |    Yes, No, No internet service |
| streaming_tv        | 7043 non-null: object |    Yes, No, No internet service |
| streaming_movies       | 7043 non-null: object |    Yes, No, No internet service |
| paperless_billing        | 7043 non-null: object |    uses paperless billing Yes or No |
| monthly_charges       | 7043 non-null: float64 |    monthly bill amount in USD |
| total_charges        | 7043 non-null: object |    lifetime total charged to customer in USD  |
| contract_type       | 7043 non-null: object |    One Year, Two Year, Month-to-month |
| payment_type        | 7043 non-null: object |    Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)|
| internet_service_type       | 7043 non-null: object |    Fiber optic, DSL, None |

### Questions I have of the Data
- What features are most strongly correlated to churn?
    - Are any of these correlated to one another? Are there confounding variables? Not truly independent?
- Does a high monthly bill push customers to churning?

### Initial hypotheses
**Question 1:** Is there a difference in tenure between customers who churned and customes who didn't?

**Hypothesis 1:**
alpha = .05
$H_{0}$ There is no difference in tenure between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in tenure between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in tenure between customers who churned and customers who didn't churn.

**Question 2:** Is there a difference in monthly_charges between customers who churned and customes who didn't?

**Hypothesis 2:**

$H_{0}$ There is no difference in monthly_charges between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in monthly_charges between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in monthly_charges between customers who churned and customers who didn't churn.

**Question 3:** Is there a difference in total_charges between customers who churned and customes who didn't?

**Hypothesis 3:**

$H_{0}$ There is no difference in total_charges between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in total_charges between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in total_charges between customers who churned and customers who didn't churn.

## Project Plan and Pipeline 

#### Plan
- Acquire data from the Codeup Database. Create an acquire.py file containing a function to automate the process.
- Initial inquiry into the data to see the shape and layout of things. This will help inform initial cleaning and prep of data.
- Clean and prepare data for the explore phase. Create an acquire.py to store functions I create to automate the cleaning and preperation process. This will involve an encoding step for all categorical data before moving on to exploring the data.
- Begin exploring the data and ask questions leading to clarity of what is happening in the data. Clearly define at least three hypotheses, set an alpha, run any statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways. Automate as much as possible and put all functions into an explore.py file
- After thoroughly exploring the data, do any final preparation necessary to begin modeling. Automate this function and put it into a model.py file
- Train at least three different classification models.
- Evaluate models on train and validate datasets. Do further hyperparamter iteration to find the best performing models. Save all iteration functions to be automated in the model.py file.
- Choose the model with that performs the best and do final hyperparameter tuning feature selection.
- Evaluate that single model on the test dataset.
- Create a csv file containing customer_id, probability of churn, and prediction of churn by using my final model on the test dataset.
- Construct a Final Report Notebook wherein I show how I arrived at the MVP model by using my created modules. Throughout the notebook,document conclusions, takeaways, and next steps.
- Create README.md with data dictionary, project and business goals, initial hypothesis and an executive summary.



## Executive Summary
- Of all the classification models I created DecisionTree and RandomForest performed the best.
- I chose RandomForest as my best performing model and achieved a 80.9% for predicting my target value, churn. This model outperformed the baseline accuracy score of 73.4% so it has predictive value.
- There were some clear drivers of churn in the dataset. The overwhelming majority of customers who churned were:
    - **Month-to-Month** contracts
    - Electronic check payment customers
    - Fiber optic internet customers
- Given further time, I would like to experiment with engineering some more valuable features using the data available to see if I can improve the model.
- Additionally it would be nice to have some specific information surrounding how a customer churned, e.g.:
    - Date of Churn (around any specific days?)
    - Did the customer just not renew a contract? Or did they actively cancel?
    - Was the customer on a promotion that ended right before they churned?
    - For fiber customers who left, were there any major isp problems (outages, slow speed, high latency?) that contributed to them leaving?