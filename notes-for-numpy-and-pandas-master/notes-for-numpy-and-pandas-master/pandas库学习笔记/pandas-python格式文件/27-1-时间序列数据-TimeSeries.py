#!/usr/bin/env python
# coding: utf-8

# ## Pandas-针对时间序列的操作

# 内容介绍:针对山东大学《Python大数据分析(2020春)》课程中时间序列的笔记<br>
# 地址见：https://www.bilibili.com/video/BV115411Y7UX?p=57

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime


# ## 1.将时间序列作为索引

# In[3]:


# 示例数据
dates = [
    datetime(2018,10,2),datetime(2018,10,5),
    datetime(2018,10,7),datetime(2018,10,8),
    datetime(2018,10,10),datetime(2018,10,12),
    datetime(2017,10,3),datetime(2017,10,12),
    datetime(2017,9,10),datetime(2017,9,12),
    datetime(2017,8,10),datetime(2017,8,12),
    datetime(2017,10,9),datetime(2017,10,8),
]
df = pd.Series(np.random.randn(14),index=dates)
df


# In[4]:


#查看索引类型
df.index


# ## 2.通过时间序列索引获取数值的方法
# 
# * 传入的日期参数较为灵活，可以是日期字符串，日期数据和其他可以解释为日期的数值。
# * 由于pandas使用了第三方库dateutil包的parser.parse，可以自动解析人类可读日期字符串为日期数据，因此传入日期<br>
# 字符串后会自动识别并获取数值（但需要注意这个包的缺陷，即将某些数字自动识别为日期）
# * 获取的数据为原时间序列的视图(类似于numpy数组)，在视图上的修改会反应在原始数据上。

# In[5]:


#使用原始的序号索引，查看索引其中的一项
df.index[0]


# In[39]:


#使用可以理解的日期字符串索引获取数据。
df['2018-10-2']


# In[42]:


#使用日期型数据值索引获取值
df[datetime(2018,10,2)]


# In[44]:


#使用另一种可以理解的日期字符串索引获取值
df['2018/10/2']


# In[49]:


#获取数据时，也可以按照年获取，或者按照月获取
df['2018-10']


# In[6]:


#按整年获取数据
df['2017']


# In[9]:


#由于时间序列数据大部分是按照时间排序，因此可以使用不在索引中的时间戳切片
df['2017-8-15':'2017-10-5']


# In[14]:


#另一种切片的等价函数，但需要数据排序
df2 = df.sort_index()
df2.truncate(after='2017-9-11')


# In[56]:


#创建较长数据
df_long = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2017',periods=1000))
df_long


# In[60]:


#使用时间切片的方法获取数据
df_long['2017-5-4':'2017-5-8']


# ## 3.带有重复索引的时间序列

# In[69]:


# 示例数据
dates = [
    datetime(2018,10,2),datetime(2018,10,5),
    datetime(2018,10,7),datetime(2018,10,8),
    datetime(2018,10,10),datetime(2018,10,12),
    datetime(2017,10,3),datetime(2017,10,12),
    datetime(2017,9,10),datetime(2017,9,12),
    datetime(2017,8,10),datetime(2017,8,12),
    datetime(2017,10,9),datetime(2017,10,8),
]
df3 = pd.Series(np.random.randint(0,15,size=(28)),index=dates*2)
df3


# In[71]:


#检查是否存在重复索引
df3.index.is_unique


# In[72]:


#使用索引聚合,level=0
df3.groupby(level=0).count()


# In[73]:


#使用索引聚合,level=0
df3.groupby(level=0).sum()

