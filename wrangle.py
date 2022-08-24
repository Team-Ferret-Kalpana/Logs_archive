#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import env


# In[2]:


''' function to connect to CodeUp SQL database'''
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'


# In[3]:


def get_logs():
    ''' function to acquire the curriculum logs data from MySQL server with the columns i wanted to be dataframe.
    And renamed the columns in the  SQL querry for convienience'''
    query = '''
       SELECT logs.date,  logs.time,
       logs.path as endpoint,
       logs.user_id as user,
       logs.ip as source_ip,
       cohorts.name as cohort_name,
       cohorts.start_date as start_date,
       cohorts.end_date as end_date,
       cohorts.program_id as program_id
       FROM logs
       JOIN cohorts ON logs.cohort_id= cohorts.id;
         '''
    
    
    df= pd.read_sql(query, get_connection('curriculum_logs'))
    
    return df


# In[7]:


def prepare_log(df):
    ''' This prepare function set the date column as index, drop unwanted columns    and set the start date and end date to date time format'''
    #change the date column to datetime
    df['date']=pd.to_datetime(df.date)
    # set date column to index
    df = df.set_index(df.date)
    #set the start_date and end_date column to datetime format
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    #split the endpoint into 4 different sections using / as sepeartor and concatenate to the dataframe
    df= pd.concat([df, df.endpoint.str.split('/',3, expand = True)], axis=1)
    # renaming the columns created after the split of endpoint columns as page 1, page 2,page 3, page 4 respectively
    df.rename(columns={0:'page_1',1:'page_2',2:'page_3',3:'page_4'}, inplace = True)
    # data science program dataframe
    ds_df= df[df.program_id == 3]
    # web developers dataframe
    web_df = df[(df.program_id != 3) & (df.cohort_name != 'Staff')]
    #staff only dataframe
    staff_df = df[df.cohort_name == 'staff']
    return df,ds_df, web_df, staff_df


# In[5]:


# test the acquiring function
df=get_logs()
df.head(2)


# In[8]:


# test the prepare function
df, ds_df, web_df, staff_df= prepare_log(df)


# In[9]:


df.head()


# In[10]:


ds_df.head()


# In[ ]:




