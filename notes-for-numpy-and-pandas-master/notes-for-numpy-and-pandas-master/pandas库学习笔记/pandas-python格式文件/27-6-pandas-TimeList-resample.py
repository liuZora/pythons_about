#!/usr/bin/env python
# coding: utf-8

# ## Pandas-重采样及频率转换

# 内容介绍:重采样是指将时间序列从一个频率转换到另一个频率的处理过程。

# 分类:
# 
# * 降采样：将高频率数据聚合到低频率(降频率采样，例如将月度数据转换为季度数据)
# * 升采样：将低频率数据转换为高频率（例如将季度数据转换为月度数据）
# * 其他采样。

# 重采样主要使用resample函数：
# 
# resample(self, rule, axis=0, closed: 'Optional[str]' = None, label: 'Optional[str]' = None, convention: 'str' = 'start', kind: 'Optional[str]' = None, loffset=None, base: 'Optional[int]' = None, on=None, level=None, origin: 'Union[str, TimestampConvertibleTypes]' = 'start_day', offset: 'Optional[TimedeltaConvertibleTypes]' = None) -> 'Resampler'
# 
# * rule:重采样规则
# * axis:采样数据的轴，默认为0轴
# * fill_method:升采样如何插值，如ffill,bfill。默认不插值。
# * ohlc:open,high,low,close四种采样方式
# * 其他参数详见：help(pd.DataFrame.resample)
# 
# * how:重采样后以何种方式聚合。以类似于resampe().mean()的形式使用。
# **默认是求平均值，即参数为mean。也可以是first,last,max,min。**

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


# 示例数据
rng = pd.date_range('2018-1-1',periods=100,freq='D')
ts = pd.Series(np.random.randn(len(rng)),index=rng)
ts


# ### 1.resample基本方法的使用

# In[7]:


# 日频率转换为月频率
ts.resample('M').mean()


# In[10]:


# 转换为时期频率
ts.resample('M',kind='period').mean()


# ### 2.降采样

# In[19]:


# 日期范围，频率1分钟
rng2 = pd.date_range('2019-1-1',periods=12,freq='T')
ts2=pd.Series(np.arange(12),index=rng2)
ts


# In[12]:


# 通过求和的方式，将数据聚合到5分钟的块中
# 包含面元的右边界，最终的时间序列是以各面元边界的时间戳进行标记的
# 多一个区间(2018-12-31 23:55:00,2019-01-01 00:00:00)。
# 2019-01-01 00:00:00落不到原来的第一个区间里,所以要往前补足。
ts2.resample('5min',closed='right').count()


# In[14]:


#当参数close=left时，包含面元的左边界
ts2.resample('5min',closed='left').sum()


# In[15]:


#当参数close=left时，包含面元的左边界
ts2.resample('5min',closed='right',label='right').sum()


# In[16]:


#当参数close=left时，包含面元的左边界。
ts2.resample('5min',closed='right',label='right',loffset='-1s').sum()


# ### 3.OHLC采样

# In[18]:


ts2.resample('5min').ohlc()


# ### 4.升采样和插值
# 
# * 将数据从低频率转换为高频率不需要聚合
# * 使用asfreq方法转换为高频，则不经过聚合
# * 使用resample的参数实现填充和插值

# * 使用时期索引的数据进行重采样，与时间戳相似
# * 因为时期指的是时间区间，所以升采样和降采样的规则比较严格
# 
# **基本规则：**

# In[22]:


df4 = pd.DataFrame(np.random.randn(2,4),
                  index=pd.date_range('1/1/2021',periods=2,freq='W-WED'),
                  columns=['北京','广州','上海','深圳']
                  )
df4


# In[24]:


# 数据从低频率到高频率不需要聚合，但是会出现缺失值
# 使用asfreq()方法转换成高频，则不经过聚合
df_daily = df4.resample('D').asfreq()
df_daily


# In[25]:


# 使用resampleing的参数实现填充和插值
df4.resample('D').ffill()


# In[26]:


# 填充部分
df4.resample('D').ffill(limit=2)


# In[27]:


# 变换频率，星期三转换为星期四
df4.resample('W-THU').ffill()


# ### 5.通过时期进行重采样

# In[30]:


df5 = pd.DataFrame(np.random.randn(24,4),
                  index=pd.period_range('1-2020','12-2021',freq='M'),
                  columns=['北京','广州','上海','深圳']
                  )
df5.head()


# In[32]:


# 使用时期索引的数据进行重采样，与时间戳相似
annual_df5 = df5.resample('A-DEC').mean()
annual_df5


# In[33]:


annual_df5.resample('Q-DEC').ffill()


# In[35]:


#convention='end'以原数据的季度中最后一个填充
annual_df5.resample('Q-DEC',convention='end').ffill()


# In[36]:


annual_df5.resample('Q-MAR').ffill()


# In[2]:


help(pd.DataFrame.resample)

