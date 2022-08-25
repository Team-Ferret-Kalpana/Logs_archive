# Anomaly Detection Project

# Project Goals
    Analyze the curriculum access logs to answer the questions presented by leaders.

# Project description

# Deliverables
- Github Repository
    i. README file
    ii. Final Notebook
    iii. .py modules with all the necessary functions to reproduce the notebook
- Email with answers for questions asked by the leaders

# Key Questions 
1. Which lesson appears to attract most traffic consistently across cohorts(per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? 
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?


# Data Dictionary
    - Date       : date when curriculum was accessed, set as index
    - Time       : time when curriculum was accessed
    - endpoint   : path used to access curriculum lessons
    - user       : unique user id number
    - source_ip  : IP Address
    - cohort_name: Name of the cohort at Codeup
    - start_date : cohort start date
    - end_date   : cohort end date
    - program_id : Identifying number for Data science and Web Developer program
    - page_1     : 1st part after splitting the endpoint
    - page_2     : 2nd part after splitting the endpoint
    - page_3     : 1rd part after splitting the endpoint
    - page_4     : 4th part after splitting the endpoint

# Steps to Reproduce the Notebook
    - envy.py file with credentials for successful connection with CodeUp DB Server.
    - clone the project repo(including wrangle.py,fun_4.py)
    - import pandas, matplotlib, seaborn, numpy, sklearn libraries 
    - finally you should be able to run Anomaly_Detection_Report

# Pipeline

## Wrangle Data
    - Wrangling process includes both data acquisition and data preparation(data cleaning) process

### Acquire Data
    - wrangle.py module has all necessary functions to to connect to SQL database and generate the curriculum_logs dataframe.

### Data preparation
    wrangle.py module has function that cleans the acquired data
        1. Convert the date to datetime format and set it as index
        2. Split the endpoint into 4 parts and rename it to as 'page_1','page_2','page_3','page_4' and concatenate to the dataframe itself
        3. create a separate dataframe for data science  and web developer program only excluding the staff
    fun_4.py module has functions targeted for question 4. It has functions to plot and calculate all the necessary parameters.

# Exploration
Goal: Address the initial questions through visualizations 


# Conclusion
## Summary
From  data exploration we came with key takeaways for each question
    1. Key Takeaways for Question-1:
        - creating-files-and-directories from Comand Line Interface(cli) in Appendix was most visited lessons by Data Ccience Program
        - working with data types operators and variables from javascript -i Introduction was most visited lessons by Web Dev Program
    2. Key Takeaways for Question-2:
        - 
        - 
    3. Key Takeaways for Question-4:
        -
    4. Key Takeaways for Question-5:
        - access to both curriculum s were not shut off
        - it is evident that there is cross referencing between the cohorts
    5. Key Takeaways for Question-6:
    6. Key Takeaways for Question-7:


    5. Key Takeaways for Question-6:

    6. Key Takeaways for Question-7:
        - The least visited lessons by Data Science Cohort :
        - The least visited lessons by Web Development cohort :
## Recommendations


## Next Steps