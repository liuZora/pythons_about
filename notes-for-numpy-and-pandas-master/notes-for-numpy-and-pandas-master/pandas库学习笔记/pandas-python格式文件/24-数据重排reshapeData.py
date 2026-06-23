#!/usr/bin/env python
# coding: utf-8

# ## Pandas:重塑层次化索引和重排

# 内容介绍:

# In[3]:


import numpy as np
import pandas as pd


# In[11]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# In[13]:


#使用pandas的索引类创建带有名称的索引
idx = pd.Index(['小刚','小花','小敏','小强'],name='姓名')
cls = pd.Index(['语文','英语','数学'],name='科目')
df2 = pd.DataFrame(np.random.randint(50,98,size=(4,3)),index=idx,columns=cls)
df2


# ### 1.DataFrame对象、Series对象互相转变

# In[34]:


# 使用stack()函数将DataFrame数据对象，变为一维的Series对象。
# 转换成的Series对象有一个层次化索引。
s1 = df2.stack()
s1


# In[36]:


#使用外层索引从Series对象获取数据
xgs = s1['小刚']
xgs


# In[37]:


#此种方法获取的数据，表面上看和直接从DataFrame中相同，但缺失了有用的类属性
xgs.name


# In[32]:


#直接从DataFrame中获取数据
xg = df2.loc['小刚']
xg


# In[33]:


#从DataFrame中获取的数据返回Series类，有类属性
xg.name


# In[28]:


#使用内层索引从Series对象获取数据
s1[:,'数学']


# In[29]:


#直接从DataFrame中获取数据
df2['语文']


# In[38]:


#将Series对象转换为DataFrame数据对象
s1.unstack()


# In[41]:


#指明层次索引序号进行转换。可以使用level参数或直接传入数值。
s1.unstack(level=0)


# In[44]:


#指明行名称、列名称进行转换
s1.unstack('姓名')


# In[46]:


#指明行名称、列名称进行转换
s1.unstack('科目')


# ### 2.转化过程中的注意事项

# In[48]:


#不是所有级别在层级中能找到
a1 = pd.Series(np.arange(4),index=list('asdf'))
a1


# In[49]:


a2 = pd.Series([4,5,6],index=list('ldf'))
a2


# In[55]:


s2 = pd.concat([a1,a2],keys=['data1','data2'])
s2


# In[56]:


#二级索引不一致时，转换过程中会存在Nan值
s2.unstack()


# In[58]:


#将DataFrame数据转换为Series时，默认过滤缺失数据
s2.unstack().stack()


# In[1]:


#转换过程中不过滤Nan值的情况
s2.unstack().stack(dropna=False)


# ### 3.数据的轴向转换

# In[4]:


# pivot方法是一种结合reindex和stack方法的综合方法。
df3 = pd.DataFrame(np.random.randint(50,90,size=(4,3)),columns=['B','A','C'])
df3['nm'] = ['d','b','c','a']
df3['A'] = [1,3,4,5]
df3


# In[6]:


df3.pivot('nm','A','B')

