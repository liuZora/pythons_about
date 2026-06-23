#!/usr/bin/env python
# coding: utf-8

# ## Pandas-沿时间轴移动数据

# 内容介绍:
# 
# * 移动指的是沿时间轴将数据前移或后移
# * 使用shift方法进行移动
# * Series和DataFrame都有shift方法
# * 作用：用于执行单纯的前移或后移操作，保持索引不变
# * 语法如下：
# 
# shift(self, periods=1, freq=None, axis=0, fill_value=None) -> 'Series'

# In[1]:


import numpy as np
import pandas as pd
import datetime
import pandas.tseries.offsets as offset


# ### 1.沿时间轴移动数据

# In[2]:


# 示例数据
ts = pd.Series(np.random.randn(4),index=pd.date_range('2018-1-1',periods=4,freq='M'))
ts


# In[3]:


#单纯前后移动
#不加其他参数是数据移动，产生缺失数据
ts.shift(2)


# In[4]:


#数据向上移动
ts.shift(-2)


# **时间序列数据移动的应用：可以计算时间序列的百分比**

# In[7]:


#计算ts数据的环比增长率
(ts/ts.shift(1)-1)*100


# **移动索引，而不是数据的方法:**

# In[15]:


#设置freq参数后，索引移动，数据不动
ts.shift(2,freq='M')


# In[16]:


#设置freq参数后，索引移动，数据不动
ts.shift(2,freq='D')


# ### 2.通过偏移量对日期进行移动
# 
# 需要使用偏移量模块进行处理

# In[ ]:


# 需要进一步学习


# ### 3.时期的数字运算
# 
# 时期表示时间的区间，比如数日、数月或数年等。Period类表示时期数据类型。

# In[21]:


# 创建时期数据对象。'A-DEC'代表每年度12月31日
p = pd.Period(2018,freq='A-DEC')
p


# In[20]:


#也可以传入字符串
p2 = pd.Period('2018',freq='A-DEC')
p2


# 时期的数字运算
# 
# * 通过加减整数可以实现对Period的移动
# * 相同频率的Period对象的差，是他们之间的单位数量

# In[22]:


p+2


# In[27]:


p3 = p-2


# In[29]:


# 相同的频率可以进行减法
p2-p3


# In[30]:


help(pd.period_range)

