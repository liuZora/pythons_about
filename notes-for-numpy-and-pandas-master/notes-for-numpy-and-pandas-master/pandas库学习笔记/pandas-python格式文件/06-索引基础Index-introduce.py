#!/usr/bin/env python
# coding: utf-8

# ## Pandas的索引的基础知识及操作

# |序号|方法|说明|
# |----|----:|----:|
# |01|.append(idx)|连接一个index对象，产生新的index对象|
# |02|.diff(idx)|计算差集，产生新的index对象|
# |03|.intersection(idx)|计算交集|
# |04|.union(idx)|计算并集|
# |05|.delete(loc)|删除位于loc位置的元素|
# |06|.insert(loc,c)|在loc位置增加元素c|

# 索引操作的主要方法是，在数据原有索引的基础上，使用索引函数修改索引形成新的索引，再形成新的数据。<br>
# 通过操作索引，可以操作对应的数值。<br>
# pandas通过索引的操作数据比numpy更加便捷。numpy中是通过维度进行操作数据，比较复杂。这是两者的区别。

# In[3]:


import numpy as np
import pandas as pd


# 1. Series和DataFramede的索引都是Index对象

# In[4]:


ser1 = pd.Series(range(5))
ser1


# In[5]:


ser2 = pd.Series(range(5),index=['a','b','c','d','e'])
ser2


# In[6]:


df1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
df1


# In[7]:


df2 = pd.DataFrame(np.arange(9).reshape(3,3))
df2


# In[8]:


print(type(df1.index))


# 2. 索引对象不可变，保证了数据安全
# 
#  * 可以修改后形成新的索引

# In[9]:


df1.index


# In[10]:


# 修改索引时，报错。
df1.index[1]=8


# 3.常见索引的种类

#  * Index,普通索引
#  * Int64Index,整数索引
#  * MultiIndex,层级索引
#  * DatetimeIndex,时间戳索引
