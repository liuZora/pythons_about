#!/usr/bin/env python
# coding: utf-8

# # DataFrame的基本用法

# In[1]:


from decimal import Decimal, getcontext

# 设置全局精度为小数点后两位
getcontext().prec = 2

# 使用Decimal进行运算
result = Decimal('1.2345') + Decimal('2.3456')
print(result)  # 输出：3.58


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#实际上，针对二维的numpy数组，行列同dataframe的行列是一致的。
arr1 = np.arange(12).reshape(3,4)
print(arr1)
df1 = pd.DataFrame(arr1,index=['A','B','C'],columns=['a','b','c','d'])
df1


# ### 1.T转置

# In[4]:


#转置不改变原有的数据
df2 = df1.T
df2


# In[5]:


df1


# ### 2.通过索引获取列数据

# In[14]:


df2['A']


# In[17]:


#获取的每一列属于Series数据类型
print(type(df2['B']))


# In[18]:


df1['a']


# ### 3.增加列数据

# In[20]:


#增加列是直接赋值即可。赋值时使用列索引。
df1['e']=[7,8,9]


# In[21]:


df1


# ### 4.删除列

# In[22]:


#使用del命令删除
del(df1['e'])


# In[23]:


df1

