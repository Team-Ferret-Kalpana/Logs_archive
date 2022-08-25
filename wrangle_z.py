#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import env


# In[15]:


print('new_logs_data()' '\n' 'get_logs_data()' "\n" 'prepare(df)')


# In[2]:


url = f'mysql+pymysql://{env.username}:{env.password}@{env.host}/curriculum_logs'


# In[ ]:


def prepare(df):
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date)
    df = df.drop(columns = ['cohort_id', 'id', 'deleted_at', 'date', 'slack', 'created_at', 'updated_at'])
    df.rename(columns = {'path':'endpoint', 'user_id':'user', 'ip':'source_ip', 'name':'cohort_name'}, inplace =True)
    return df


# In[16]:


def new_logs_data():
    return pd.read_sql('''select * FROM logs LEFT JOIN cohorts ON logs.cohort_id = cohorts.id;

''', url)


import os

def get_logs_data():
    filename = "logs.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=0)
        df.index = pd.to_datetime(df.index)
        return df
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        # read the SQL query into a dataframe
        df_logs = new_logs_data()
        
        #prepare new logs
        df_logs_p = prepare(df_logs)
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df_logs_p.to_csv(filename)

        # Return the dataframe to the calling code
        return df_logs_p


# In[4]:


#df = new_logs_data()


# In[5]:


#df.to_csv('logs_unprepared.csv')


# In[6]:


#df.head()


# In[ ]:


#df = prepare(df)


# In[ ]:


#df.head()


# In[ ]:


#df.to_csv('logs.csv')


# In[ ]:





# In[12]:


#df = get_logs_data()


# In[13]:


#df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




