#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


sns.set_style('whitegrid')


# In[4]:


titanic = sns.load_dataset('titanic')


# In[5]:


titanic.head()


# In[9]:


sns.jointplot(x='fare',y='age',data=titanic,kind='scatter')


# In[15]:


sns.distplot(titanic['fare'],kde=False, bins=30, color='red')


# In[24]:


sns.set_context('notebook')
sns.boxplot(x="class", y="age", data=titanic, palette='rainbow')


# In[28]:


sns.set_context('notebook')
sns.swarmplot(x="class", y="age", data=titanic)


# In[33]:


sns.countplot(x='sex',data=titanic, palette='rainbow')


# In[36]:


sns.heatmap(titanic.corr(),cmap='coolwarm',linecolor='white',linewidths=1)


# In[40]:


g = sns.FacetGrid(titanic, col="sex")
g = g.map(plt.hist, "age")


# In[ ]:




