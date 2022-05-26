# <center>Surging Churn an Urgent Concern </center>

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
- Creation of python modules to assist in the entire process and make it easily repeatable
    - acquire.py
    - prepare.py
    - explore.py
    - model.py
- Ask exploratory questions of the data that will give an understanding about the attributes and drivers of customers churning    
    - Answer questions through charts and statistical tests
- Construct the best possible model for predicting customer churn
    - Make predictions for a group of customers
- Adequately document and annotate all code
- Give a 5 minute presentation to a group of collegues and managers covering the final notebook deliverable with a walkthrough of work I did, why, goals, what you found, your methdologies, and my conclusions
- Field questions from instructors and peers about my specific code, approach to the project, findings and model

### Business Goals
- Identify features from the dataset which may be driving churn. **Why are customers churning?**
- Construct a ML classificationmodel which accurately predicts which customers will churn
- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and the resulting outcome

### Audience
- My target audience for my notebook walkthrough is my direct manager and their manager
- Codeup Data Science instructors and students

### Project Deliverables
- A github readme explaining the project
- A jupyter notebook containing my final report (properly documented and commented)
- All modules containing functions created to achieve the final report notebook
- A csv file containing customer_id, probability of churn, and prediction of churn by using my final model on the test dataset
- 1+ non-final notebook (s) created while working on the project, containing exploration & modeling work (and other work)
- A presentation of final report notebook

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
alpha = .05<br>
$H_{0}$ There is no difference in tenure between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in tenure between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in tenure between customers who churned and customers who didn't churn.

**Question 2:** Is there a difference in monthly_charges between customers who churned and customes who didn't?

**Hypothesis 2:**
alpha = .05<br>
$H_{0}$ There is no difference in monthly_charges between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in monthly_charges between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in monthly_charges between customers who churned and customers who didn't churn.

**Question 3:** Is there a difference in total_charges between customers who churned and customes who didn't?

**Hypothesis 3:**
alpha = .05<br>
$H_{0}$ There is no difference in total_charges between customers who churned and customers who didn't churn.

$H_{a}$ There is a statistically significant difference in total_charges between customers who churned and customers who didn't churn.

- I rejected the Null Hypothesis; There is a statistically significant difference in total_charges between customers who churned and customers who didn't churn.

## Project Plan and Data Science Pipeline

#### Plan
- Acquire data from the Codeup Database. Create an acquire.py file containing a function to automate the process.
- Initial inquiry into the data to see the shape and layout of things. This will help inform initial cleaning and prep of data.
- Clean and prepare data for the explore phase. Create an acquire.py to store functions I create to automate the cleaning and preperation process. This will involve an encoding step for all categorical data before moving on to exploring the data.
- Begin exploring the data and ask questions leading to clarity of what is happening in the data. Clearly define at least three hypotheses, set an alpha, run any statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways. Automate as much as possible and put all functions into an explore.py file
- After thoroughly exploring the data, do any final preparation necessary to begin modeling. Automate this function and put it into a model.py file
- Train at least three different classification models.
- Evaluate models on train and validate datasets. Do further hyperparamter iteration to find the best performing models. Save all iteration functions to be automated in the model.py file.
- Choose the model with that performs the best and do final hyperparameter tuning feature selfection.
- Evaluate that single model on the test dataset.
- Create a csv file containing customer_id, probability of churn, and prediction of churn by using my final model on the test dataset.
- Construct a Final Report Notebook wherein I show how I arrived at the MVP model by using my created modules. Throughout the notebook,document conclusions, takeaways, and next steps.
- Create README.md with data dictionary, project and business goals, initial hypothesis and an executive summary

#### Plan &rarr; Acquire
- Create acquire.py to store all functions needed to acquire dataset
- Retrieve data from Codeup Database by running an SQL query to pull requisite Telco data, and put it into a usable Pandas dataframe
- Do cursory data exploration/summarization to get a general feel for the data contained in the dataset
- Use the acquire.py file to import and do initial exploration/summarization of the data in the Final Report notebook

#### Plan &rarr; Acquire &rarr; Prepare
- Explore the data further to see where/how the data is dirty and needs to be cleaned. This is not EDA. This is exploring individuals variables so as to prepare the data to undergo EDA in the next step
- Create prepare.py to store all functions needed to clean and prepare the dataset
    - A function which cleans the data:
        - Convert datatypes where necessary: objects to numerical; numerical to objects
        - Deal with missing values and nulls
        - Drop superfluous or redundant data columns
        - Handle redudant categorical variables that can be simplified
        - Change names to snake case where needed
        - Drop duplicates
    - A function which encodes the cleaned dataframe's categorical variables into numerical variables using one-hot encoding
    - A function which splits the dataframe into 3 subsets: Train, Validate, and Test to be used for modeling later
- Use the prepare.py file to import and do initial cleaning/preperation of the data in the Final Report notebook

#### Plan &rarr; Acquire &rarr; Prepare &rarr; Explore
- Do Exploratory Data Analysis of using bivariate and multivariate stats and visualizations to find interactions in the data
- Explore my key questions and discover answers to my hypotheses by running statistical analysis on data
    - Must include at least 4 visualizations and 2 statistical tests
- Find key features to use in the model. Similarly find unecessary features which can be dropped
    - Look for correlations, relationships, and interactions between various features and the target
    - Understanding how features relate to one another will be key to understanding if certain features can or should be dropped/combined
- Document all takeaways and answers to questions/hypotheses
- Create an explore.py file which will store functions made to aid in the data exploration
- Use explore.py and stats testing in the final report notebook to show how I came to the conclusions about which data to use

#### Plan &rarr; Acquire &rarr; Prepare &rarr; Explore &rarr; Model
- Do any final pre-modeling data prep (drop/combine columns) as determined most beneficial from the end of the Explore phase
- Find and establish baseline accuracy. This will give me an accuracy level to beat with my models
- Create at least three classification models to predicate target of churn.
    - Given time attempt other models. I would like to try Support Vector Machines and Naive Bayes
- For all models made, compare accuracy results from train to validate
    - If possible iterate through small hyperparameters to see if default values are getting us the best results
- Compare results from models to determine which is best. Chose the final model to go forward with
- Vary the algorithm hyperparameters for the final model to find the best performing settings for predicting the target of churn
    - Create an iteration function to cycle through several thousand possible combinations
- Put all iteration functions and other created functions into a prepare.py file
- Use model.py in the final report notebook to show how I reached the final model
- Having determind the best possible hyperparameters, create the final model and test it on out of sample data (the test subset created in prepare) to determine accuracy
- Summarize the results using a confusion matrix. Document results and takeaways

#### Plan &rarr; Acquire &rarr; Prepare &rarr; Explore &rarr; Model &rarr; Deliver
- After introduction, briefly summarize (give an executive summary) the project and goals before delving into the final report notebook for a walkthrough
- Do not talk through my entire process in the initial pipeline. This is only the "good stuff" to show how I arrived at the model I did
- Detail my thought process as I was going through the though process to explain the reasons for my choices

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

## Reproduce this project
- In order to run through this project yourself you will need your own env.py file that acquire.py will import to be able to access the Codeup database. You must have your own credentials to access the Codeup database
- All other requisite files for running the final project notebook (python files, images, csv files) are contained in this repository.
