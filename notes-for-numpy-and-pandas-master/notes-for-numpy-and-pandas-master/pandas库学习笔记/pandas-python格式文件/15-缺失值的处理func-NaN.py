#!/usr/bin/env python
# coding: utf-8

# ## Pandas缺失值的处理

# 内容介绍:如何使用函数处理缺失值

# In[2]:


import numpy as np
import pandas as pd


# In[7]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
s0['b']=None
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0.loc['c','A']=np.nan
df0.loc['b','B']=np.nan
df0


# ### 1.判断是否存在缺失值
# 
# 使用isnull()函数进行判断

# In[9]:


# 返回一个bool数组
df0.isnull()


# ### 2.处理缺失值-丢弃
# 
#  * 使用dropna()函数进行
#  * 过程中不改变元数据

# In[11]:


# 默认丢弃掉出现缺失值的整行数据
df0.dropna()


# In[13]:


#如果需要丢弃列数据时，需要指定axis参数
df0.dropna(axis=1)


# In[14]:


df0


# ### 3.填充缺失数据
# 
#  * 使用fillna()函数进行
#  * 执行方法后不改变元数据
#  * 一般在填充的时候选择0、平均值或直接丢弃掉

# In[15]:


df0.fillna(-1.)


# In[16]:


df0

