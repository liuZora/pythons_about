#!/usr/bin/env python
# coding: utf-8

# ## Pandas-层级索引

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd


# In[9]:


# 示例数据
s0 = pd.Series(range(8),index=[['a','a','b','b','c','c','d','d'],[1,2,1,2,1,2,1,2]])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1.什么是层级索引
# 
#  * 创建数据时index指定两个索引，形成层级索引

# In[10]:


# 索层级引的数据类型
print(type(s0.index))
print(s0.index)


# ### 2.层级索引的选取

# In[13]:


#(1)外层选取
s0['b']


# In[16]:


# (2)内层索引获取。两层索引在选取框中使用[:]分隔，前面是外层索引，后面是内层索引。
s0[:,2]


# In[19]:


#同时使用内层和外层索引
s0['b',2]


# ### 3.交换-内外层索引的交换

# In[21]:


#(1)使用swaplevel进行交换
s0.swaplevel()


# In[24]:


# 讲座中有此方法。但实际已被废弃的方法。
#(2)交换内外层索引并进行排序(先排序外层，再排序内层，默认升序)
s0.swaplevel().sortlevel()

