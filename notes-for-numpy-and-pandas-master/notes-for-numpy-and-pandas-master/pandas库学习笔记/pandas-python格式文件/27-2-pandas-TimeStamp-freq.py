#!/usr/bin/env python
# coding: utf-8

# ## Pandas:日期的范围、频率以及移动

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd


# ### 1.日期的范围及序列生成

# * 生成日期范围：根据指定的频率生成指定长度的DatatimeIndex
# 
# 函数语法:<br>
# date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs) -> pandas.core.indexes.datetimes.DatetimeIndex
# 
# * start:开始日期
# * end:结束日期。如果没有结束日期，则生成从开始到现在的日期序列。
# * period:固定时期，取值为整数或None
# * freq:日期偏移量(频率)，取值为string或DateOffset,默认为'D'
# * name:生成索引对象的名称，取值为string或None

# In[3]:


#产生开始日期、结束日期的日期范围，频率默认为天
times11 = pd.date_range('2018-1-1','2018-1-15')
times11


# In[4]:


#指定开始日期，和生成的时期。默认按照天生成数据，即freq='D'。默认的第一个时间参数是start,可以指定end和periods
times12 = pd.date_range('2018-1-1',periods=20)
times12


# In[6]:


#指定开始日期，和生成的时期，修改为月数据。
times13 = pd.date_range('2018-1-1',periods=10,freq='M')
times13


# In[10]:


#产生带时间信息的数据
times14 = pd.date_range('2018-1-1 10:20:01',periods=10,freq='M')
times14


# In[11]:


#使用规范化参数产生日期的范围
#默认情况下保留开始日期时间参数的时间戳。当normalize=True时，产生日期不带时间。
times15 = pd.date_range('2018-1-1 10:20:01',periods=10,normalize=True)
times15


# ### 2.频率组合
# 
# freq参数使用比较灵活，能够控制更大范围的频率
# 
# **频率**
# * 产生日期范围时，各个日期之间的间隔
# * 由一个基础频率和一个乘数组成,基础频率h和乘数4,组成4h
# * 基础频率使用字符串别名表示，如'D':天，'M':月
# * 每个基础频率都有一个对应的日期偏移量对象(data oddset),如H对应hour
# 
# **举例:**
# * 4h :每4小时
# * 2H30min:2小时30分钟
# * B表示工日的每天
# * M日历月末
# * BM月内最后工作日
# * 时间序列频率较为复杂，建议查看文档，应用时详细研究

# In[13]:


#每间隔4小时
times21 = pd.date_range('2018-1-1','2018-1-5',freq='4h')
times21


# In[3]:


#每间隔2小时30分钟
times22 = pd.date_range('2018-1-1','2018-1-3',freq='2h30min')
times22


# In[5]:


#月中某星期：'WOM'，每个月的第三个星期五：'WOM-3FRI'
#获取一段日期中每个月的第三个星期五
fri3 = pd.date_range('2021-1-1','2021-10-10',freq='WOM-3FRI')
fri3


# ### 3.日期偏移量
# 
# * 可以使用日期偏移量方法生成日期连续索引数据
# * 可以生成同频率组合相同的数据

# In[6]:


# 具体见2中的相关示例。


# In[2]:


help(pd.date_range)

