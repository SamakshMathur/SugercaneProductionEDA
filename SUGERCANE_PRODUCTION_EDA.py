#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt 


# In[2]:


df = pd.read_csv('List of Countries by Sugarcane Production.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# # DATA CLEANING

# In[5]:


df['Production (Tons)'] = df['Production (Tons)'].str.replace(".","")
df['Production per Person (Kg)'] = df['Production per Person (Kg)'].str.replace(".","").str.replace(",",".")
df['Acreage (Hectare)'] = df['Acreage (Hectare)'].str.replace(".","")
df['Yield (Kg / Hectare)'] = df['Yield (Kg / Hectare)'].str.replace(".","").str.replace(",",".")


# In[6]:


df.head()


# In[7]:


df.rename(columns = {"Production (Tons)":"Production(Tons)"}, inplace = True)
df.rename(columns = {"Production per Person (Kg)":"Production_per_Person_(Kg)"}, inplace = True)
df.rename(columns = {"Acreage (Hectare)":"Acreage(Hectare)"}, inplace = True)
df.rename(columns = {"Yield (Kg / Hectare)":"Yield(Kg/Hectare)"}, inplace = True)


# In[8]:


df.head()


# In[9]:


df.isna().sum()


# In[10]:


df[df["Acreage(Hectare)"].isnull()]


# In[11]:


df = df.dropna().reset_index()


# In[12]:


df.tail()


# In[13]:


df.drop(["index","Unnamed: 0"], axis = 1, inplace = True)


# In[14]:


df.head()


# In[15]:


df.dtypes


# In[16]:


df["Production(Tons)"] = df["Production(Tons)"].astype(float)
df["Production_per_Person_(Kg)"] = df["Production_per_Person_(Kg)"].astype(float)
df["Acreage(Hectare)"] = df["Acreage(Hectare)"].astype(float)
df["Yield(Kg/Hectare)"] = df["Yield(Kg/Hectare)"].astype(float)


# In[17]:


df.dtypes


# In[18]:


df.nunique()

# OUR DATA SET IS NOW CLEAN
# In[ ]:





# # UNIVARIATE ANALYSIS 

# In[19]:


df.head()


# # HOW MANY COUNTEIS PRODUCE SUGERCANE FROM EACH CONTINENT

# df['Continent'].value_counts()

# In[20]:


df["Continent"].value_counts().plot(kind = "bar")

AFRICA PRODUCES MOST NUMBER OF SUGERCANES
# In[21]:


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.distplot(df["Production(Tons)"])
plt.subplot(2,2,2)
sns.distplot(df["Production_per_Person_(Kg)"])
plt.subplot(2,2,3)
sns.distplot(df["Acreage(Hectare)"])
plt.subplot(2,2,4)
sns.distplot(df["Yield(Kg/Hectare)"])


# In[22]:


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.subplot(2,2,2)
sns.boxplot(df["Production_per_Person_(Kg)"])
plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.subplot(2,2,4)
sns.boxplot(df["Yield(Kg/Hectare)"])


# In[23]:


df.describe()


# In[ ]:





# # BIVARIATE ANALSYSIS

# In[24]:


df.head()


# In[25]:


df_new = df[["Country","Production(Tons)"]].set_index("Country")


# # WHICH COUNTRY PRODUCES MAXIMUM SUGERCANE ?

# In[26]:


df_new["Percentage_production"] = df_new["Production(Tons)"]*100/df_new["Production(Tons)"].sum()


# In[27]:


df_new


# In[28]:


df_new["Percentage_production"].plot(kind = "pie",autopct = "%.2f")


# In[29]:


df_new["Production(Tons)"].plot(kind = "bar")


# In[30]:


ax = sns.barplot(data = df.head(10), x = "Country", y = "Production(Tons)")


# In[31]:


# SINCE THE GRAPH WAS NOT CLEAR AND WAS OVERLAPPING WE WILL TAKE USE OF XTICKLABELS


# In[32]:


ax = sns.barplot(data = df.head(10), x = "Country", y = "Production(Tons)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# In[ ]:





# # WHICH COUNTRY HAS THE HIGHEST LAND

# In[33]:


df_act = df.sort_values("Acreage(Hectare)",ascending = False)
ax = sns.barplot(data = df_act.head(10), x = "Country", y = "Acreage(Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# In[ ]:





# # WHICH COUNTRY HAS HIGHEST YEILD PER KG HECT 

# In[34]:


df_yield = df.sort_values("Yield(Kg/Hectare)",ascending = False)
ax = sns.barplot(data = df_yield.head(10), x = "Country", y = "Yield(Kg/Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# In[ ]:





# # WHICH COUNTRY HAS THE HIGHEST PRODUCTION? 

# In[35]:


df_prod = df.sort_values("Production_per_Person_(Kg)",ascending = False)
ax = sns.barplot(data = df_prod.head(10), x = "Country", y = "Production_per_Person_(Kg)")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.show()


# In[ ]:





# # CORRELATION

# In[36]:


df.corr()   
# as the value is closer to 1 that means the values are more correleated


# In[37]:


sns.heatmap(df.corr(), annot = True, cmap = 'Greens')


# In[ ]:




