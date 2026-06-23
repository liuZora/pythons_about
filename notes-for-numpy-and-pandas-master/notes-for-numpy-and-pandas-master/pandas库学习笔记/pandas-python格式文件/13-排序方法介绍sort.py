#!/usr/bin/env python
# coding: utf-8

# ## Pandas:排序方法介绍

# 内容介绍:分为按照索引排序和按照值排序两种

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


np.random.randint(3,4)


# In[3]:


# 示例数据
s0 = pd.Series(range(4),index=list('dbca'))
print(s0)
df0 = pd.DataFrame(np.random.randint(-5,9,size=(4,3)),index=['d','a','b','c'],columns=['B','A','C'])
df0


# ### 1.按索引排序

# Series排序

# In[4]:


#默认升序排序
s0.sort_index()


# In[5]:


#输入参数指定排序方式,ascending= False降序排序
s0.sort_index(ascending= False)


# In[6]:


#默认按照行排列，升序
df0.sort_index()


# In[7]:


#如果需要按照列排序，那么需要指定axis参数
#升序和降序的参数为ascending= 
df0.sort_index(axis=1)


# ### 2.按值排序

# In[8]:


s1 = s0.reindex(list('abcd'))
s1


# In[9]:


#按照值进行排序。如果数据中有缺失值默认排在最后
#默认升序排列
s1.sort_values()


# In[10]:


# 需要改变排序方式的时候使用参数ascending= 
s1.sort_values(ascending= False)


# In[11]:


# DataFrame的数据排序，必须强制指定行列标签
# 默认升序排列
df0.sort_values(by='A')


# In[12]:


#针对多行排序
df0.sort_values(by=['A','B'])


# In[13]:


#需要改变排序方式的时候使用参数ascending= 
df0.sort_values(by='A',ascending=False)


# In[14]:


#针对行排列时，需要指定axis=1
df0.sort_values(by='a',axis=1)


# In[ ]:




