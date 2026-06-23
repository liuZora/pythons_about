#!/usr/bin/env python
# coding: utf-8

# ## Pandas-时间及算数运算

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd
import datetime
import pandas.tseries.offsets as offset


# ### 1.时期Period_Index

# 使用period_range生成时间范围的PeriodIndex
# 
# * 使用语法同date_range()基本相同
# * 语法说明:<br>
# period_range(start=None, end=None, periods=None, freq=None, name=None) -> pandas.core.indexes.period.PeriodIndex
# * 时间范围可以作为轴索引
# * 通过时间数据或者字符串创建

# In[10]:


prng = pd.period_range('2000-1-1','2000-6-30',freq='M')
prng


# In[48]:


#(1)时间范围作为序列索引
ts = pd.Series(np.random.randn(len(prng)),index=prng)
ts


# In[49]:


#(2)字符串数组，也可以使用Period_Index
values = ['2018Q3','2018Q2','2018Q1']
index2 = pd.PeriodIndex(values, freq='Q-DEC')
index2


# In[13]:


# (3)通过表示时间信息的数组创建PeriodIndex
# 结合年度和季度信息为参数生成时间范围
year = np.array(list(('2017',)*4+('2018',)*4)).astype(np.int32)
quarter = np.array(list(('1','2','3','4')*2)).astype(np.int32)
index3 = pd.PeriodIndex(year=year,quarter=quarter,freq='Q-DEC')
index3


# In[26]:


# （4）通过dataframe中的列数据结合生成期间
df = pd.read_csv('macrodata.csv')  # 获取美国部分年度的宏观经济数据，包含年份和季度的数据标签列
df.head()


# In[21]:


index4 = pd.PeriodIndex(year=df.year,quarter=df.quarter,freq='Q-DEC')
index4


# In[22]:


df.index=index4


# In[24]:


df.cpi


# ### 2.时期的频率转换一般讲解
# 
# * 通过period.asfreq函数可以转换频率
# * 从高频率转换为低频率时，超时期(较大的时期)是由子时期(较小的时期)的位置决定的
# * PeriodIndex和TimeSeries的频率抓换方式相同

# asfreq(...)
#     Convert Period to desired frequency, at the start or end of the interval.
#     
#     Parameters
#     ----------
#     freq : str
#         The desired frequency.
#     how : {'E', 'S', 'end', 'start'}, default 'end'
#         Start or end of the timespan.
#     
#     Returns
#     -------
#     resampled : Period

# In[7]:


# 创建一个时期对象
# 以12月结束的2018年度每个月的最后一个日历日
p = pd.Period(2018,freq='A-DEC')
p


# In[6]:


#转换成年初的一个月度时期
p.asfreq('M',how='S')


# In[27]:


#转换成年末的一个月度时期
p.asfreq('M')


# **频率转换涉及重要的概念是，财政年度**<br>
# **即美国(或部分国家)的财政年度是从公历年的7月到第二年的6月结束**<br>
# **2018美国财年为公历年度的2017.7-2018.6月**
# 
# * A-JUN:表明财政年度的结尾是JUN，即6月，类似于美国的财政年度2017.7-2018.6
# * A-DEC:表明财政年度的结尾是DEC，即12月,财政年度同公历年度2017.1-2017.12

# In[12]:


#不以12月结束的财政年度，月度时期的归属情况
p2 = pd.Period('2018',freq='A-JUN')#以6月结束2018年度的每个月最后一个日历日，从2017-7到2018-6为一个时期
p2


# In[14]:


#2017-7这个时期开始的
p2.asfreq('M',how='S')


# In[15]:


#2018-6这个时期的结束。asfreq函数默认的how='E'或'end'即时期的最后一个月
p2.asfreq('M')


# In[20]:


#从高频转换为低频时，超时期(较大的时期)是由子时期（较小的时期）的位置决定的
p21=pd.Period('201803','M')
#2018-3返回2018财年
p21.asfreq('A-JUN')


# In[22]:


#从高频转换为低频时，超时期(较大的时期)是由子时期（较小的时期）的位置决定的
p22=pd.Period('201809','M')
#2018-9返回2019财年
p22.asfreq('A-JUN')


# In[24]:


#对于PeiodIndex和TimeSeries的频率转换方式相同
rng = pd.period_range('2016','2019',freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
ts


# In[25]:


#频率转换成一个月度时期索引
ts.asfreq('M',how='start')


# In[26]:


#默认how的方式是end,为日历年度的最后一个月
ts.asfreq('M')


# In[5]:


help(pd.Period.asfreq)

