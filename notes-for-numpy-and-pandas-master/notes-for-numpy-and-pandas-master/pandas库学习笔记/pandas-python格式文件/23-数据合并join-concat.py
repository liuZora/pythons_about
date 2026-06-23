#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据便捷的连接方式

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


# 示例数据
df01 = pd.DataFrame(np.random.randint(0,9,size=(4,3)),columns=['D','E','F'])
df01['key'] = ['yy','xx','mm','snn']
df01


# In[8]:


df02 = pd.DataFrame(np.random.randint(0,9,size=(4,3)),columns=['B','A','C'])
#df02['key'] = ['xx','yy','mm','nn']
df02


# ### 1.join函数的使用
# 
# * join(self, other, on=None, how='left', lsuffix='', rsuffix='', sort=False) -> 'DataFrame'
#     Join columns of another DataFrame.
# * 与merge函数的使用方法很类似。
# * 此方法直接按照索引合并
# * 合并数据的各列
# * 此种情况下，如果有重叠的列，则会报错。即两个数据集都有key列即会报错。

# In[10]:


# 此种情况下，如果有重叠的列，则会报错。即两个数据集都有key列即会报错。
df01.join(df02,how='outer')


# ### 2.另一种数据合并方式：concate
# 
# 沿轴方向合并数据

# ### 2.1复习numpy中数据的合并方式

# In[12]:


#示例数据
arr1 = np.random.randint(0,9,size=(5,3))
arr2 = np.random.randint(0,9,size=(5,3))


# In[15]:


arr1


# In[16]:


arr2


# In[19]:


#numpy默认的合并方式，按照0轴合并
np.concatenate([arr1,arr2,])


# In[20]:


#主动设置axis参数，按照1轴合并
np.concatenate([arr1,arr2,],axis=1)


# ### 2.2 pandas中的concate合并方式

# * 注意指定轴方向，默认为axis=0
# * join指定合并方式，默认为outer
# * Series合并时查看行索引有无重复

# In[21]:


df01


# In[23]:


df02


# In[24]:


#默认按照列合并(即列方向上相加),默认的axis=0,即0轴合并
pd.concat([df01,df02])


# In[26]:


#指定合并方向
pd.concat([df01,df02],axis=1)


# In[31]:


#使用列数据相同时的情况
df03 = pd.DataFrame(np.random.randint(0,9,size=(5,3)),columns=df02.columns)
df03


# In[34]:


#默认连接行
pd.concat([df02,df03])


# In[35]:


#axis=1,连接列
pd.concat([df02,df03],axis=1)


# In[ ]:





# In[ ]:





# ### 3.

# In[11]:


help(pd.DataFrame.join)

