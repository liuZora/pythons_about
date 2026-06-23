#!/usr/bin/env python
# coding: utf-8

# ## Serise的使用方法

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s = pd.Series(np.arange(1,5))
s


# In[3]:


d = {
    'name':'虾米',
    'age':20,
    'class':'三版'
}
s2=pd.Series(d,index=['name','age','class','sex'])
s2


# ### 1.isnull 函数和notnull  函数检查缺失值
# '''
# isnull函数：
# This function takes a scalar or array-like object and indicates
# whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
# in object arrays, ``NaT`` in datetimelike).
# '''

# In[4]:


s.isnull()


# In[5]:


s2.isnull()


# In[7]:


arr = [0,1,2,None]
print(arr)
#针对python序列如果使用arr.isnull会报错；但使用pd.isnull()可以检验python列表中是否存在缺失值。
pd.isnull(arr)
#arr.isnull


# In[8]:


# 判断是否不为缺失值。返回值是numpy数组。
pd.notnull(arr)


# ### 2. 通过索引获取数据。使用.values和.index函数单独获取数值和索引值。

# In[9]:


# 由于pandas是基于numpy构建的，因此返回值为numpy数据。
print(s.values)
print(type(s.values))
print('*'*20)
print(s.index)
print(type(s.index))


# In[10]:


#使用索引获取一个单独一行的数据。此处索引为默认索引0
print(s[0])
print(type(s[0]))


# In[11]:


s3 = pd.Series(np.arange(6),index=[1,2,3,4,5,6])
s3


# In[18]:


#指定标签后，Series序列就会变成标签名，原有的默认索引失效。
#s3[0]
s3[6]


# In[19]:


#还可以使用切片的形式获取Serise部分的数据，返回Serise格式的数据
print(s[0:2])
print(type(s[0:2]))


# In[20]:


#多个标签名时需要双层的[]
s2[['name','class']]


# In[21]:


#下标数字切片(与双层的[]标签切片一致)和标签切片存在区别。
print(s2[0:2])
print('*'*20)
print(s2['name':'class'])


# In[22]:


#布尔索引
s>2


# In[23]:


#布尔索引获取数据，原理同numpy相同
s[s>2]


# ### 3.索引与数据的对应关系不被运算结果影响。
# 
# 索引得出的数据是一种视图。这与numpy相同。

# In[24]:


#实际上运算得出的结果是一种视图，不改变原数据。
print(s*2)


# In[25]:


s


# ### 4. Serise对象的name属性。及其他常用的行数。

# In[26]:


s.name = 'temp'  # 序列对象名
s.index.name='year'  #对象索引名
s


# In[27]:


#获取前几行的数据函数。默认前五行。也可指定行数。
s.head(3)


# In[28]:


#获取数据的后几行。默认后五行。也可指定行数。
s.tail(2)


# In[30]:


get_ipython().run_line_magic('pinfo', 'pd.isnull')


# In[ ]:




