#!/usr/bin/env python
# coding: utf-8

# ## Pandas-通过索引修改数据

# 内容介绍:通过索引修改数据，是通过基本的标签索引或者是高级索引修改数据。<br>
# 通过索引修改的数据，会改变原有的基础数据。

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 示例数据
s0 = pd.Series(range(3))
print(s0)
s1 = pd.Series(range(3),index=['a','b','c'])
print(s1)
df0 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
df0


# ### 对Serise的修改

# In[3]:


#默认索引修改
s0[1] = 999
s0


# In[4]:


# 通过标签修改
s1['a'] = 555
s1


# In[5]:


# 也可以通过默认的整数索引修改
s1[1] = 888
s1


# ### 对DataFrame的修改

# In[6]:


# (1)通过标签修改
df0['A'] = 88
df0


# In[7]:


# (2)给dataframe赋值一个序列
df0['B'] = [30,70,90]
df0


# In[8]:


# (3)通过点标签进行修改
df0.C = 666
df0


# In[9]:


# (4)修改行数据，使用高级索引-标签索引进行修改
df0.loc['a'] = 23
df0


# In[10]:


# (5)使用高级索引loc可以单独修改某个元素
df0.loc['a','A'] = 1000
df0


# In[11]:


df0

