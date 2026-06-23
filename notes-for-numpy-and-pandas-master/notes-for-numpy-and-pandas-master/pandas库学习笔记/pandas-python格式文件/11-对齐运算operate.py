#!/usr/bin/env python
# coding: utf-8

# ## Pandas-对齐运算

# 内容介绍:pandas数据类型的基础运算方法

# |序号|方法|说明|
# |----|----:|----:|
# |01|add/radd|加法（+）,radd代表可以反转参数，即倒数|
# |02|sub/rsub|减法（-）|
# |03|div/rdiv|除法（/）|
# |04|floordiv/rfloordiv|整除（//）|
# |05|mul/rmul|乘法（\*）|
# |06|pow/rpow|幂次方(\*\*)|

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 示例数据
s0 = pd.Series(range(4),index=['a','b','c','d'])
print(s0)
s1 = pd.Series(range(5),index=['a','f','g','d','e'])
print(s1)
df0 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','D','C'])
print(df0)
df1 = pd.DataFrame(np.arange(12).reshape(4,3),index=['a','b','f','d'],columns=['A','B','C'])
df1


# ### 1. 算数运算与数据对齐
# 
# 普通运算会使相同的索引标签运算，不同标签会出现缺失值。<br>
# 运算不改变原有的数据

# In[3]:


# 针对Series进行的运算
# 对齐运算：两个series进行运算的时候，相同标签的数据可以运算；不同标签的数据运算会形成缺失值。
s0+s1


# In[4]:


# 针对DataFrame进行的对齐运算
# 相同标签的数据可以运算；不同标签的数据运算会形成缺失值。
df0+df1


# ### 2. 使用填充值的算数方法
# 
# 可以解决不对应的标签出现缺失值的情况<br>
# 运算不改变原有的数据

# In[5]:


# 默认情况下，与+相同。
s1.add(s0)


# In[6]:


# 修改fill_value参数，可以改变缺失值的设置
# 当参数设置为0时，源数据在相加的对应数据找不到对应的标签，那么元数据被设置为0
s1.add(s0,fill_value=0)


# In[7]:


#DataFrame使用fill_value参数时，当一方df有数另一方没数时，没数的一方会被填充为fill_value的值。
#当两方都没有数时，那么两方不会被填充，运算结果为NaN
df0.add(df1,fill_value = 0)


# In[8]:


# rdiv
print(1/df0)
print('*'*20)
df0.rdiv(1)


# In[9]:


# 先统一列标签之后再运算
df1.reindex(columns=df0.columns,fill_value=9)


# In[10]:


df0


# ### 3. DataFrame和Series混合运算
# 
# 一维和多维数据运算，存在广播特性<br>
# 这一点同numpy的广播运算相同<br>
# Series的索引，匹配的是DataFrame的列索引

# In[18]:


# 由于没有匹配到相应的索引，运算会出现缺失值。但包含两者行列集合(当然Series没有行的概念)。
# Series的索引，匹配pandas的列索引即可。
print(df0)
print(s0)
df0-s0


# In[19]:


s2 = pd.Series(np.arange(2,5),index=['A','B','F'])
s2


# In[20]:


# 由于两者只匹配到列'A',因此运算只显示A
print(df0);print(s2)
df0-s2


# In[25]:


#两种数据格式不同的情况，不能使用fill_value参数
print(df0);print(s2)
df0.sub(s2,fill_value=0)


# In[26]:


# 使用运算函数，并指定axis轴为0(index)，则Series匹配各行的数据，沿着行广播运算
print(df0);print(s0)
df0.sub(s0,axis=0)  # axis = 'index'


# In[ ]:




