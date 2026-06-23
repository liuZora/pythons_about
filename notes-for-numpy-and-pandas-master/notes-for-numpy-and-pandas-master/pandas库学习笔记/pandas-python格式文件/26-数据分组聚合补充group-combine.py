#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据分组聚合的补充知识

# 内容介绍:灵活的分组方式

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


idx = pd.Index(['李小刚','小花','张小敏','小强','小明'],name='姓名')
cls = pd.Index(['语文','英语','数学'],name='科目')
df00 = pd.DataFrame(np.random.randint(50,98,size=(5,3)),index=idx,columns=cls)
df00['班级']=['二班','一班','二班','一班','一班']
df00['性别']=['男','女','男','女','男']
df00


# ### 1.通过列的字典分组:

# In[5]:


km = {'语文':'主科','数学':'主科','英语':'副科','物理':'副科'}


# In[6]:


#按照列的字典（主科副科）的方式分组
#字典对应的列名才能统计出数据。字典不对应，或者字典对应的列名比数据中的多，不影响计算。
g5 = df00.groupby(km,axis=1).sum()
g5


# ### 2.类字典的Series数据进行分组:

# In[7]:


#通过类似字典的Series数据进行分组
s5 = pd.Series(km)
s5


# In[8]:


g51 = df00.groupby(s5,axis=1).sum()
g51


# ### 3.通过函数进行分组：

# In[10]:


#实际上传入的函数，针对行索引进行了长度计算，得出2个字和三个字两类进行分组
df00.groupby(len).sum()

