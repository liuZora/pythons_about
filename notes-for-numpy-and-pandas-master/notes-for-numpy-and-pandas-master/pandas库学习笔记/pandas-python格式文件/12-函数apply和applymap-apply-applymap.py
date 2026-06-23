#!/usr/bin/env python
# coding: utf-8

# ## Pandas:函数apply和applymap

#  *内容介绍:pandas数据(dataframe\series)基于numpy数组构建，因此numpy的函数可以用于处理dataframe数据。
#  
#  * 这是使用apply和applymap的主要场景。
#  * 也可查看：https://www.cnblogs.com/jason--/p/11427145.html
#  * map()是Series对象的一个函数，DataFrame中没有map()，map()的功能是将一个自定义函数作用于Series对象的每个元素。

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 示例数据
s0 = pd.Series(range(3))
print(s0)
df0 = pd.DataFrame(np.arange(-5,4).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
df0


# ### 0.直接使用numpy函数处理

# In[3]:


# 直接使用numpy函数处理
np.abs(df0)


# ### 1.apply函数

# In[7]:


# 通过apply将函数应用到列或者行中
# 默认是针对列进行的计算,axis=0
f = lambda x:x.max()
df0.apply(f)


# In[8]:


# apply需要计算行数据的时候，指定axis参数即可
df0.apply(f,axis=1)


# ### 2.Series的map函数
# 
#  * map()是Series对象的一个函数，map()的功能是将一个自定义函数作用于Series对象的每个元素。
#  * 也可以使用pd.Series.map(list)将python序列作为参数传入进行操作
#  * 返回值为Series对象

# In[9]:


f2 = lambda x: 20*x


# In[10]:


#当选取DataFrame的某一列时，即为Series数据对象
df0['A'].map(f2)


# In[11]:


#也可以直接针对Series数据序列进行函数操作
s0.map(f2)


# In[12]:


#直接使用map函数针对可迭代对象(Series)操作，Python 3.x 返回迭代器
list(map(f2,df0['A']))


# ### 3.applymap函数

# In[13]:


df2 = pd.DataFrame(np.random.rand(3,4))
df2


# In[14]:


# 通过applymap函数针对每个元素进行计算
f2 = lambda x: '%.2f'%x  #数据保留两位小数
df2.applymap(f2)


# In[ ]:




