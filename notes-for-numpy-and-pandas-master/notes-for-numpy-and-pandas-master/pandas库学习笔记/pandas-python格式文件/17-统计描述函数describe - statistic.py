#!/usr/bin/env python
# coding: utf-8

# ## Pandas-统计计算和描述

# * 内容介绍:pandas具有一组常用的统计方法
# * 官网中关于基本函数的介绍:https://pandas.pydata.org/docs/user_guide/basics.html

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(40,100,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# In[10]:


df0.loc['a','C']=None
df0.loc['c','A']=None
df0.loc['c']=None
df0


# ### 1.求和运算及其他统计基本运算
# 
# 主要的参数如下：

# 
# |序号|参数|说明|
# |----|----|----|
# |01|axis|约简的轴。DataFrame的行用0,列用1|
# |02|skipna|排除缺失值，默认值为True，即计算时排除缺失值|
# |03|level|如果轴是层次化索引的(即MultiIndex)，则根据level分组简约|

# In[8]:


#sum()函数默认求dataframe列的和
df0.sum()


# In[12]:


#如果求行的和，可以设置axis参数为1
df0.sum(axis=1)


# In[14]:


#涉及缺失值的情况，可以使用skipna参数
# skipna参数，默认为Ture即排除缺失值。当为False时，不排除缺失值，那么求和出现了NaN
df0.sum(axis=1,skipna=False)


# In[18]:


#inxmax返回最大值的索引
df0.idxmax()


# In[19]:


#cumsum()样本值的累计求和公式
df0.cumsum()


# ### 2.综合统计结果describe
# 
# 使用比较广泛，获取数据后可以先使用此方法查看数据的综合情况

# In[21]:


# 常用的数据综合统计表示方法
df0.describe()


# In[23]:


s2 = pd.Series(['a','d','g','e','f']*4)
s2


# In[24]:


# describe可以根据数据的情况自动选择显示结果
s2.describe()


# In[26]:


# describe可以根据数据的情况自动选择显示结果
s0.describe()


# ### 3.主要函数

# |NO.|Function|Description|说明(中文)|
# |----|----|----|----|
# |01|count|Number of non-NA observations|非空数值的统计|
# |02|sum|Sum of values|求和|
# |03|mean|Mean of values|求平均值|
# |04|mad|Mean absolute deviation|返回所请求轴的值的平均绝对偏差|
# |05|median|Arithmetic median of values|求中值|
# |06|min|Minimum|求最小值|
# |07|max|Maximum|求最大值|
# |08|mode|Mode|获取沿所选轴的每个元素的模式|
# |09|abs|Absolute Value|求绝对值|
# |10|prod|Product of values|返回所请求轴的值的乘积。|
# |11|std|Bessel-corrected sample standard deviation|求标准差|
# |12|var|Unbiased variance|求方差|
# |13|sem|Standard error of the mean|返回所请求轴上的平均值的无偏标准误差|
# |14|skew|Sample skewness (3rd moment)||
# |15|kurt|Sample kurtosis (4th moment)|使用Fisher的峰度定义（正常的峰度== 0.0）在请求的轴上返回无偏峰度。|
# |16|quantile|Sample quantile (value at %)||
# |17|cumsum|Cumulative sum|返回数据轴上累计求和|
# |18|cumprod|Cumulative product|返回数据轴上累计乘积|
# |19|cummax|Cumulative maximum|返回数据轴上累计最大值|
# |20|cummin|Cumulative minimum|返回数据轴上累计最小值|
