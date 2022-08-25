#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


def one_user_df_prep(df, user):
    '''
    This function returns a dataframe consisting of data for only a single defined user
    '''
    #filters data frame to only show one user at a time
    df = df[df.user == user]
    #counts how many pulls per day for the single user mentioned above
    # note 'endpoint' has no meaning. just needed a column to resample and count by
    # the real meaning is pulls per day per user which is df.user==user and resample('d').count()
    pages_one_user = df['endpoint'].resample('d').count()
    return pages_one_user


# In[3]:


def compute_pct_b(pages_one_user, span, weight, user):
    ############# single user, ewm(span), weight = K, user #
    '''
    This function adds the %b of a bollinger band range for the page views of a single user's log activity
    '''
    # Calculate upper and lower bollinger band-these are just standard equations
    midband = pages_one_user.ewm(span=span).mean()
    stdev = pages_one_user.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    
    # Add upper and lower band values to dataframe-combining data succinctly into a dataframe
    bb = pd.concat([ub, lb], axis=1)
    
    # Combine all data into a single dataframe - keep comibining
    my_df = pd.concat([pages_one_user, midband, bb], axis=1)
    my_df.columns = ['pages_one_user', 'midband', 'ub', 'lb']
    
    # Calculate percent b and relevant user id to dataframe
    # eqn for %b
    my_df['pct_b'] = (my_df['pages_one_user'] - my_df['lb'])/(my_df['ub'] - my_df['lb'])
    # add column to display user id
    my_df['user'] = user
    return my_df


# In[4]:


def find_anomalies(df, user, span, weight, plot=False):
    '''
    This function returns the records where a user's daily activity exceeded the upper limit of a bollinger band range
    '''
    
    # Reduce dataframe to represent a single user-see earlier function
    pages_one_user = one_user_df_prep(df, user)
    
    # Add bollinger band data to dataframe
    my_df = compute_pct_b(pages_one_user, span, weight, user)
    
    # Plot data if requested (plot=True)
    if plot:
        plot_bands(my_df, user)
    
    # Return records that sit outside of bollinger band upper/lower limit
    #note: we don't expect any below the lower limit based on what we saw in the overall graph
    # the lower limit is 2(sigma) which happens to result in '-' values
    # but you can't have '-' of pulls
    return my_df[(my_df.pct_b>1) | (my_df.pct_b<0)]


# In[5]:


def plot_bands(my_df, user):
    '''
    This function plots the bolliger bands of the page views for a single user
    '''
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(my_df.index, my_df.pages_one_user, label='Number of Pages, User: '+str(user))
    ax.plot(my_df.index, my_df.midband, label = 'EMA/midband')
    ax.plot(my_df.index, my_df.ub, label = 'Upper Band')
    ax.plot(my_df.index, my_df.lb, label = 'Lower Band')
    ax.legend(loc='best')
    ax.set_ylabel('Number of Pages')
    plt.show()


# In[6]:


def plot_bands_two(my_df, users):
    '''
    This function plots the bolliger bands of the page views for a single user
    '''
    for user in users:
        temp_df = my_df[my_df.user == user]
        plt.figure()
        plt.plot(temp_df.index, temp_df.pages_one_user, label='Number of Pages, User: '+str(user))
        plt.plot(temp_df.index, temp_df.midband, label = 'EMA/midband')
        plt.plot(temp_df.index, temp_df.ub, label = 'Upper Band')
        plt.plot(temp_df.index, temp_df.lb, label = 'Lower Band')
        plt.legend()
        plt.show()


# In[7]:


def one_user_df_prep_ip(df, user):
    '''
    This function returns a dataframe consisting of data for only a single defined user
    '''
    #filters data frame to only show one user at a time
    df = df[df.source_ip == user]
    #counts how many pulls per day for the single user mentioned above
    # note 'endpoint' has no meaning. just needed a column to resample and count by
    # the real meaning is pulls per day per user which is df.user==user and resample('d').count()
    pages_one_user = df['endpoint'].resample('d').count()
    return pages_one_user


# In[8]:


def compute_pct_b_ip(pages_one_user, span, weight, user):
    ############# single user, ewm(span), weight = K, user #
    '''
    This function adds the %b of a bollinger band range for the page views of a single user's log activity
    '''
    # Calculate upper and lower bollinger band-these are just standard equations
    midband = pages_one_user.ewm(span=span).mean()
    stdev = pages_one_user.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    
    # Add upper and lower band values to dataframe-combining data succinctly into a dataframe
    bb = pd.concat([ub, lb], axis=1)
    
    # Combine all data into a single dataframe - keep comibining
    my_df = pd.concat([pages_one_user, midband, bb], axis=1)
    my_df.columns = ['pages_one_user', 'midband', 'ub', 'lb']
    
    # Calculate percent b and relevant user id to dataframe
    # eqn for %b
    my_df['pct_b'] = (my_df['pages_one_user'] - my_df['lb'])/(my_df['ub'] - my_df['lb'])
    # add column to display user id
    my_df['source_ip'] = user
    return my_df


# In[9]:


def find_anomalies_ip(df, user, span, weight, plot=False):
    '''
    This function returns the records where a user's daily activity exceeded the upper limit of a bollinger band range
    '''
    
    # Reduce dataframe to represent a single user-see earlier function
    pages_one_user = one_user_df_prep_ip(df, user)
    
    # Add bollinger band data to dataframe
    my_df = compute_pct_b_ip(pages_one_user, span, weight, user)
    
    # Plot data if requested (plot=True)
    if plot:
        plot_bands_ip(my_df, user)
    
    # Return records that sit outside of bollinger band upper/lower limit
    #note: we don't expect any below the lower limit based on what we saw in the overall graph
    # the lower limit is 2(sigma) which happens to result in '-' values
    # but you can't have '-' of pulls
    return my_df[(my_df.pct_b>1) | (my_df.pct_b<0)]


# In[1]:


def plot_bands_two_ip(my_df, users):
    '''
    This function plots the bolliger bands of the page views for a single user
    '''
    for user in users:
        temp_df = my_df[my_df.source_ip == user]
        plt.figure()
        plt.plot(temp_df.index, temp_df.pages_one_user, label='Number of Pages, User: '+str(user))
        plt.plot(temp_df.index, temp_df.midband, label = 'EMA/midband')
        plt.plot(temp_df.index, temp_df.ub, label = 'Upper Band')
        plt.plot(temp_df.index, temp_df.lb, label = 'Lower Band')
        plt.legend()
        plt.show()


# In[ ]:




