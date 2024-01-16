#!/usr/bin/env python
# coding: utf-8

# # How to Import Data in Python

# ## Learning Objectives
# One of the reasons why Python is such a popular programming language for machine learning is because it supports some very powerful and easy to use packages which are purpose-built for data analysis. One of these packages is the **pandas** package. In this exercise, you will get a brief introduction to the pandas package and how to import data using functions provided by the pandas package. By the end of this tutorial, you will have learned:
# 
# + what a pandas Series is
# + what a pandas DataFrame is
# + how to import data from a CSV file
# + how to import data from an Excel file

# ## The pandas Package

# In[1]:


import pandas as pd


# ## The pandas Series

# In[2]:


members = ["Brazil", "Russia", "India", "China", "South Africa"]
brics1 = pd.Series(members)
brics1


# In[3]:


type(brics1)


# ## The pandas DataFrame

# In[4]:


members = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
        "gdp": [2750, 1658, 3202, 15270, 370],
        "literacy":[.944, .997, .721, .964, .943],
        "expectancy": [76.8, 72.7, 68.8, 76.4, 63.6],
        "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]}
brics2 = pd.DataFrame(members)
brics2


# In[6]:


type(brics2)


# In[7]:


members = [["Brazil", "Brasilia", 2750, 0.944, 76.8, 210.87],
                     ["Russia", "Moscow", 1658, 0.997, 72.7, 143.96],
                     ["India", "New Delhi", 3202, 0.721, 68.8, 1367.09],
                     ["China", "Beijing", 15270, 0.964, 76.4, 1415.05],
                     ["South Africa", "Pretoria", 370, 0.943, 63.6, 57.4]]
labels = ["country", "capital", "gdp", "literacy", "expectancy", "population"]
brics3 = pd.DataFrame(members, columns = labels)
brics3


# ## How to import data from a CSV file

# In[8]:


brics4 = pd.read_csv("brics.csv")
brics4


# ## How to import data from an Excel file

# In[9]:


brics5 = pd.read_excel("brics.xlsx")
brics5


# In[11]:


brics6 = pd.read_excel("brics.xlsx", sheet_name = "Summits")
brics6

