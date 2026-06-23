#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据清洗和准备

# 内容介绍:

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1.缺失值处理
# 
# 笔记15#针对缺失值的处理流程:（1）发现缺失值、（2）丢弃缺失值、（3）填充/替换缺失值。

# ### 1-(2)丢弃缺失值
# 
# dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)

# In[5]:


df0.loc['c','A'] = None
df0.loc['b'] = None
df0


# In[6]:


#关于丢弃缺失值的补充方法：丢弃整行为Nan的行
# how : {'any', 'all'}, default 'any'
df0.dropna(how='all')


# In[7]:


#按照列删除全是nan值的列
#由于没有全是nan的列，那么没有删除任何列
df0.dropna(axis=1,how='all')


# In[8]:


#针对某一列去除nan值使用，subset参数
df0.dropna(subset=['A'])


# In[5]:


df1=pd.DataFrame(np.random.rand(7,3))
df1.loc[:4,1]=np.nan
df1.loc[:2,2]=np.nan
df1


# In[24]:


# thresh : int, optional
#        Require that many non-NA values.
# 指定达到缺失值的数量才能删除
df1.dropna(thresh=2)


# In[25]:


#dropna函数，不改变原数据的索引号
df1.dropna()


# In[7]:


#drop()函数不改变元数据
df1


# ### 1-（3）缺失值填充

# In[23]:


#不添加其他参数的填充方法
df1.fillna(0)


# In[13]:


#针对某个列空缺值填充不同的数值的方法
df1.fillna({1:0.9,2:0.8})


# In[14]:


df1


# In[11]:


# fillna函数默认操作时不对原数据进行更改。需要针对源数据更改添加参数inplace=True
df2=df1.copy()
df2.fillna({1:0.9,2:0.8})


# In[15]:


df2


# In[19]:


df3 = pd.DataFrame(np.random.randn(6,3))
df3.iloc[2:,1] = np.nan
df3.iloc[4:,2] = np.nan
df3


# In[22]:


# 按照列的缺失值最上面一个有效值填充
df3.fillna(method='ffill')


# In[23]:


#按照列上的缺失值上最后一个有效值填充，设置向下填充的个数
df3.fillna(method='ffill',limit=2)


# In[ ]:





# In[11]:


help(pd.DataFrame.dropna)

