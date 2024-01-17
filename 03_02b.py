#!/usr/bin/env python
# coding: utf-8

# # How to Summarize Data in Python

# ## Learning Objectives
# When exploring data, one of the most important things we can do is summarize it so we can better understand it. A common way to summarize data is by computing aggregations such as mean, median, maximum and minimum. These aggregations or statistical measures (as they are commonly referred to) describe the general and specific characteristics of our data. This is why these types of aggregations are sometimes referred to as **descriptive statistics** or **summary statistics**. The pandas DataFrame provides several methods for computing descriptive statistics. By the end of this tutorial, you will have learned:
# 
# + how to describe a DataFrame
# + how to get simple aggregations
# + how to get group-level aggregations

# ## How to Describe a DataFrame

# In[2]:


import pandas as pd
washers = pd.read_csv("washers.csv")
washers.info


# In[3]:


washers.head()


# ## How to get Simple Aggregations
# The `describe()` method returns a statistical summary for each of the columns in a DataFrame. It's important to note that the descriptive statistics returned by the `describe()` method depends on the data type of a column. For non-numeric columns, the descriptive statistics returned by the method are as follows:
# 
# |Name      |   Description  |
# |-----------------|---------------------|
# | `count`         | Number of non-missing values                       |
# | `unique`       | Number of unique non-missing values                   |
# | `top`       | Most commonly occuring value   |
# | `freq`        | Frequency of the most commonly occuring value                   |
# 

# In[7]:


washers[['BrandName']].describe()


# For numeric columns, the `describe()` method returns the following descriptive statistics:
# 
# |Name      |   Description  |
# |-----------------|---------------------|
# | `count`         | Number of non-missing values                       |
# | `mean`       | Average of the non-missing values                   |
# | `std`       | Standard deviation of the values   |
# | `min`        | Smallest value                  |
# | `25%`         | 25th percentile                       |
# | `50%`       | 50th percentile (same as the median)                   |
# | `75%`       | 75th percentile   |
# | `max`        | Largest value                   |
# 

# In[8]:


washers[['Volume']].describe()


# In[9]:


washers[['BrandName']].value_counts()


# In[10]:


washers[['BrandName']].value_counts(normalize = True)


# In[11]:


washers[['Volume']].mean()


# ## How to get Group-level Aggregations

# In[12]:


washers.groupby('BrandName')[['Volume']].mean()


# In[13]:


washers.groupby('BrandName')[['Volume']].mean().sort_values(by = 'Volume')


# In[14]:


washers.groupby('BrandName')[['Volume']].agg(['mean', 'median', 'max', 'min'])

