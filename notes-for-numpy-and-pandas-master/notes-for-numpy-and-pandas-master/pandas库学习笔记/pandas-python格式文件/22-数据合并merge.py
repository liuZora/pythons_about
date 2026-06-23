#!/usr/bin/env python
# coding: utf-8

# ## Pandas:数据规整

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


# 示例数据
s0 = pd.Series(range(10),index=['d','b','c','a','e','d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1.层次化索引-知识回顾(可以查看06文档详细讲解)

# In[4]:


#添加一个层次化索引
dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
s0_index_2 = s0.index.map(dic)
#构建一个新的带有层次化索引的数据
s = pd.Series(s0.values,index=[s0.index, s0_index_2])


# In[5]:


s0_index_2


# In[ ]:


# 索引排序
s1 = s.sort_index()
s1


# In[29]:


#层次化索引的选取操作
s1['a':'c']


# In[32]:


#离散选取
s1[['b','d']]


# In[34]:


#直接索引内层
s1.loc[:,2]


# In[46]:


#设置新索引
df_idx = df0.index.map(dic)
df0['new_idx'] = df_idx
#set_index()函数中的参数,drop=False时原来转换成索引的列继续保留
df1 = df0.set_index(['new_idx',df0.index])
df1.sort_index


# In[47]:


#将转换成索引的列还原成原来的列
df1.reset_index


# In[51]:


df1.index


# ### 2.数据连接-连接列的方式
# 
# merge(left, right, how: str = 'inner', on=None, left_on=None, right_on=None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes=('_x', '_y'), copy: bool = True, indicator: bool = False, validate=None) -> 'DataFrame'
# 
# * left,需要连接的左方数据
# * right,需要连接的右方数据
# * how:连接方式，包括inner,outer,left,right

# In[80]:


df21 = pd.DataFrame(np.random.randint(0,9,size=(4,3)),columns=['D','E','F'])
df21['key'] = ['yy','xx','mm','snn']
df21


# In[77]:


df22 = pd.DataFrame(np.random.randint(0,9,size=(4,3)),columns=['B','A','C'])
df22['key'] = ['xx','yy','mm','nn']
df22


# In[89]:


#pd.merge根据单个或多个键连接两个表格。默认列明相同的列为连接键。
#需要关键列一致
#也可以使用参数on设定需要连接的键列
#默认：在键列中，两者不一致的数据，不会被连接。即内连接形式。
pd.merge(df21,df22)


# In[90]:


#内连接，指定参数进行。内连接也是默认值。-->交集的概念
pd.merge(df21,df22,how='inner',on='key')


# In[85]:


#左连接
#以前面(即左面的)的参数为主，查找右面的数据，存在相同的则连接数据；如果左边键有数据，右边没有那么不连接数据。
pd.merge(df21,df22,how='left',on='key')


# In[87]:


#右连接，方式同左连接相反。
pd.merge(df21,df22,how='right',on='key')


# In[91]:


#外连接，方式为两者结合最大的范围。-->并集的概念
pd.merge(df21,df22,how='outer',on='key')


# In[96]:


#连接中处理重复的列名
df23 = df21.copy()
df23.loc['4'] = [3,5,6,'yy']
df23.loc['5'] = [3,50,99,'yy']
df23.loc['6'] = [13,22,6,'yy']
df23


# In[98]:


#数据中出现重复的key关键字时，处理方式如下：
#关键字匹配时，没有关键字重复的数据进行多次匹配
pd.merge(df23,df22)


# In[99]:


#按索引连接和关键字key连接。默认使用内连接。
pd.merge(df23,df22,left_on='E',right_index=True)


# In[ ]:





# ### 3.

# In[3]:


help(pd.merge)

