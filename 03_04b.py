#!/usr/bin/env python
# coding: utf-8

# # How to Visualize Data in Python

# ## Learning Objectives
# When exploring data, one of the most important things we can do is visualize it so we can better understand it. Like the popular saying "*A picture is worth a thousand words*”, visualizations are sometimes more useful than summary statistics in helping us understand our data. This is because visualizations are a great tool for asking and answering questions about data. Depending on the type of question we are trying to answer, there are four major types of visualizations we could use. They are relationship, distribution, comparison and composition. By the end of this tutorial, you will have learned: 
# 
# + how to create a relationship visualization
# + how to create a distribution visualization
# + how to create a comparison visualization
# + how to create a composition visualization

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# Let's import and preview the data we will use to illustrate how to visualize data.

# In[2]:


import pandas as pd
vehicles = pd.read_csv("vehicles.csv")
vehicles.head()


# ## How to create a Relationship Visualization

# In[3]:


vehicles.plot(kind = 'scatter', x = 'citympg', y = 'co2emissions')


# ## How to create a Distribution Visualization

# In[5]:


vehicles['co2emissions'].plot(kind= 'hist')


# ## How to create a Comparision Visualization

# In[6]:


vehicles.pivot(columns = 'drive', values = 'co2emissions')


# In[7]:


vehicles.pivot(columns = 'drive', values = 'co2emissions').plot(kind = 'box', figsize = (10,6))


# ## How to create a Composition Visualization

# In[8]:


vehicles.groupby('year')['drive'].value_counts()


# In[9]:


vehicles.groupby('year')['drive'].value_counts().unstack()


# In[10]:


vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind = 'bar', stacked= True, figsize = (10,6))

