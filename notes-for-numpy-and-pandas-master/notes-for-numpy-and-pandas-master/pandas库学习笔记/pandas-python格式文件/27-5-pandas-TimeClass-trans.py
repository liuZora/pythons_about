#!/usr/bin/env python
# coding: utf-8

# ## Pandas-时期极度频率转换，时期时间戳转换

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd
import datetime
import pandas.tseries.offsets as offset


# ### 1.季度时期频率的转换
# 
# 许多季度数据会涉及“财年末”的概念，通常是一年12个月中某月的最后一个工作日或日历日。
# 
# * pandas支持12种可能的季度频率，即Q-JAN到Q-DEC

# In[32]:


# （1）财政年度和季度年度
# 以1月结束的2018财政年度(对应日历年度的2017.2-2018.1)的每个季度最后一个月的最后公历日
# 这个时期的范围2017-2到2018-1，每三个月一个季度，这里的Q4代表第四季度
p3 = pd.Period('2018Q4',freq='Q-JAN')
p3


# In[33]:


#p3是2018财政年度的第四季度，转换为月度计量，数据显示开始月份
p3.asfreq('M',how='S')


# In[35]:


#p3是2018财政年度的第四季度，转换为月度计量，数据显示结束月份(默认)
p3.asfreq('M')


# In[38]:


# （2）该季度倒数第二个工作日的下午4点时间戳
# p.asfreq('B','e')得出该季度最后一个月的最后一个工作日
# 'B'：日期-工作日频率；'E'：时期的结尾(how参数)
# 'T':时间频率的分钟；'S':开始(how参数)
p4pm = (p3.asfreq('B','E')-1).asfreq('T','s')+16*60
p4pm


# In[40]:


#转成时间戳
p4pm.to_timestamp()


# In[42]:


# （3）相同的运算可以应用到TimeSeries
rng = pd.period_range('2017Q3','2018Q4',freq='Q-Jan')
ts = pd.Series(np.arange(len(rng)),index=rng)
ts


# In[44]:


new_rng = (rng.asfreq('B','E')-1).asfreq('T','s')+16*60
ts.index = new_rng.to_timestamp()
ts


# ### 2.TimeStamp与Period互相转换
# 
# * 通过to_period方法，可以将时间戳(timestamp)索引的Series和DataFrame对象转换为以时期(period)索引
# * 也可以将timestamp转换为period出现重复时期
# * to_timestamp转换为timestamp

# In[59]:


# (1)通过to_period方法，可以将时间戳(timestamp)索引的Series和DataFrame对象转换为以时期(period)索引
rng4 = pd.date_range('2018-01-01',periods=3,freq='M')
ts4 = pd.Series(np.arange(len(rng4)),index=rng4)
ts4


# In[60]:


ts4.index


# In[55]:


# 使用to_period函数转换成时期索引
pts = ts4.to_period()
pts


# In[58]:


pts.index


# In[62]:


# (2)将timestamp转换为period出现重复时期
rng42 = pd.date_range('12/29/2018', periods=6, freq='D')
ts42 = pd.Series(np.arange(len(rng42)),index=rng42)
ts42


# In[67]:


temp = ts42.to_period('M')
temp


# In[68]:


temp.index


# In[69]:


# (3)to_timestamp可以将period转换为timestamp
# 时期数据转换回来时会失真
temp.to_timestamp(how='E')


# In[5]:


help(pd.Period.asfreq)

