#!/usr/bin/env python
# coding: utf-8

# ## Pandas-离散化和面元划分

# 内容介绍:
#  * 离散化：通过数据处理，得到数据在整体中的相对大小
#  * 面元划分：分阶段

# In[3]:


import numpy as np
import pandas as pd


# In[18]:


# 示例数据
s0 = pd.Series(np.random.randint(18,70,size=(10)))
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# In[24]:


arr = np.random.randint(18,100,size=(20))
arr


# ### 1.1面元划分-cut函数
# 
# 面元划分及相关操作

# In[8]:


# 划分数据的阶段
bins = [18,25,35,60,100]


# In[25]:


#获取对应数据的面元。理解为返回的是表示不同面元名称的字符串。
cats = pd.cut(arr,bins)
cats


# In[26]:


#针对Series不能显示此属性。python数组和numpy ndarry数组可以使用此属性。
cats.categories


# In[28]:


#显示数组对应的阶段
cats.codes


# In[30]:


# 分类数据统计
pd.value_counts(cats)


# In[33]:


#默认的左开右闭。修改这种方式如下：
cat2 = pd.cut(arr,bins,right=False)
cat2


# In[35]:


# 分类数据统计
pd.value_counts(cat2)


# In[38]:


#自定义面元名称。让面元(数据分区)有可理解的意义。
names=['青少年','青年','中年','老年']
cat3 = pd.cut(arr,bins,labels=names)
cat3


# In[40]:


#统计数据出现时，按照标签显示各阶段的数量
pd.value_counts(cat3)


# In[41]:


#不输入设定的阶段值，按照数量划分阶段
arr2 = np.random.rand(20)
arr2


# In[48]:


#在cat函数中传入阶段数量，函数会根据传入的数据自动划分。precision=2是返回结果为两位小数。
# 数值所在的区间四等分。即数值区间在0-100，四块均等分为25.
cat4 = pd.cut(arr2,4,precision=2)
cat4


# In[49]:


pd.value_counts(cat4)


# ### 1.2面元划分qcut函数
# 
# 得到每个面元数据量相等的划分

# In[50]:


arr12 = np.random.rand(1000)


# In[52]:


# 可以实现按照数量的四等分。即总体为100个数据，那么每份分为25个数据。
cat12 = pd.qcut(arr12,4)
cat12


# In[53]:


pd.value_counts(cat12)


# In[54]:


#qcut自己设定范围的划分
cat121 = pd.qcut(arr12,[0,0.1,0.5,0.9])
cat121


# In[55]:


pd.value_counts(cat121)


# ### 2.检测和过滤异常值

# In[4]:


df2 = pd.DataFrame(np.random.randn(1000,4))
df2


# In[5]:


np.abs(df2)>2


# In[10]:


#找到绝对值大于三的数值。筛选异常值。
df2[(np.abs(df2)>2).any(1)]


# In[11]:


#针对某些异常值的设置
df2[(np.abs(df2)>3)] = 3


# In[12]:


df2.describe()


# ### 3.排列和随即采样

# In[13]:


df3 = pd.DataFrame(np.arange(5*4).reshape(5,4))
df3


# In[17]:


#获取包含随机数的数组
sam = np.random.permutation(5)
sam


# In[18]:


#使用随即数组，获取行随机排列的数据
#随即数组的生成是根据np.random.permutation函数进行
df3.take(sam)


# In[20]:


#随机选取数行
df3.sample(3)


# In[21]:


#随机选取数行
df3.sample(n=1)


# In[22]:


ch = pd.Series([5,8,1,3,0])
ch


# In[24]:


#选取大于数据量本身的随机数据
ch.sample(n=10,replace=True)

