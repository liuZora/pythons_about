#!/usr/bin/env python
# coding: utf-8

# ## numpy,DataFrame通过索引的基本操作-删除操作

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ser1 = pd.Series(range(3))
ser1


# In[3]:


df1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
df1


# ## 3. 删除索引

# ### 3.1使用del删除

# In[4]:


#del删除Series数据，改变原数据。删除没有索引的数据会报错。
del ser1[3]


# In[ ]:


ser1


# In[5]:


#del删除dataframe数据，改变原数据,并且只能删除列数据。删除没有索引的数据会报错。
del df1['C']
df1


# ### 3.2使用drop()方法删除-默认删除行

# In[6]:


#使用drop方法删除，不会改变原数据。
ser2 = ser1.drop(1)
ser2


# In[7]:


#也可以使用此方法删除多条数据，参数为一个表示行标签的数组
ser3 = ser1.drop([0,1])
ser3


# In[8]:


#由于不会改变原数据，那么重复执行删除代码时，不会报错。默认给定的变量为行。
df2=df1.drop('a')
df2


# In[9]:


#也可以使用此方法删除多条数据，参数为一个表示行标签的数组
df3=df1.drop(['a','b'])
df3


# ### 3.3使用drop()方法删除列，需要指定轴axis参数

# In[10]:


#定轴axis参数，可以给定轴对应的数字。列轴数字为1,行为0.
df331 = df1.drop('A',axis=1)
df331


# In[11]:


#定轴axis参数，列名称，'columns'
df332=df1.drop('A',axis='columns')
df332


# ### 3.3使用drop()方法删除，指定inplace参数后可以在原对象中删除

# In[12]:


df1.drop('c',inplace=True)
df1


# In[ ]:




