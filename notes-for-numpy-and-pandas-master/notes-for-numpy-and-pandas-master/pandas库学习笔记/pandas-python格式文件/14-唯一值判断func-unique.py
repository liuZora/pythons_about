#!/usr/bin/env python
# coding: utf-8

# ## Pandas-唯一值和成员属性的判断函数

# 内容介绍:<br>
# 针对Series:<br>
# unique()、index.is_unique、value_counts()、isin<br>
# 针对DataFrame:
# isin

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 示例数据.创建数据时，标签可以重复。
s0 = pd.Series(np.random.randint(0,9,size=(7)),index=['d','b','c','a','e','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1. unique()函数返回数组的唯一值

#  * Series的应用

# In[3]:


#返回的一个一维数组
s0.unique()


# In[4]:


#求索引的唯一值。由于索引可以不唯一。
s0.index.unique()


# In[5]:


#判断是否全部为唯一值
s0.index.is_unique


# In[6]:


#返回值出现的个数
s0.value_counts()


# In[7]:


#判断成员是否存在。传入的参数为一个数组。返回一个bool类型的数组。
s0.isin([8])


# In[8]:


#也可判断多个值
s0.isin([8,1])


#  * dataframe的应用-成员属性

# In[25]:


# 返回一个布尔型的数组
df0.isin([8])

