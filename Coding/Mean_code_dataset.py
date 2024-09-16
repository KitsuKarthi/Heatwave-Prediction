#!/usr/bin/env python
# coding: utf-8

# In[127]:


import pandas as pd
from statistics import mean


# In[128]:


data = pd.read_csv('Modified_Final_Dataset.csv')
df = pd.DataFrame()


# In[110]:


def calculate_rounded_mean(time):
    int_list = []

    for item in time:
        try:
            num = float(item)
            int_list.append(num)
        except ValueError:
            print(f"Skipping invalid entry: {item}")

    rounded_mean = round(mean(int_list), 7)
    return rounded_mean


# In[115]:


def TenU():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['10u'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
            date.append(data['datetime'][i].split(' ')[0])

    df['datetime'] = date
    df['10u'] = final

    return df


# In[119]:


def TenV():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['10v'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['10v'] = final

    return df


# In[120]:


def msl():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['msl'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['msl'] = final

    return df


# In[121]:


def msnlwrf():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['msnlwrf'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['msnlwrf'] = final

    return df


# In[122]:


def r():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['r'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['r'] = final

    return df


# In[123]:


def ssr():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['ssr'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['ssr'] = final

    return df


# In[124]:


def maxtemp():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['maxtemp'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['maxtemp'] = final

    return df


# In[125]:


def rainfall():
    time = []
    date = []
    final = []
    length = len(data)


    for i in range(length):
        time.append(data['rainfall'][i])
        if(i%24 == 0):
            final.append(calculate_rounded_mean(time))
            time = []
    df['rainfall'] = final

    return df


# In[126]:


TenU()
TenV()
msl()
msnlwrf()
r()
ssr()
#maxtemp()
#rainfall()


# In[ ]:


df.to_csv('Mean_Dataset')

