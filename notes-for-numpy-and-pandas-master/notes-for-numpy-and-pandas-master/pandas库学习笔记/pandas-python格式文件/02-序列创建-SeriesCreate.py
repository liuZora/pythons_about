#!/usr/bin/env python
# coding: utf-8

# ## Series数据结构简介，序列的创建

# 1. Series数据结构简介
# 
#  * Series是一种一维标记型数组结构，
#  * 能保存任何数据类型
#  * 包含数据索引，索引自动创建。也可使用index参数手动添加。
#  * 类似于python的字典dict数据结构

# 2. Series序列的创建
# 
# 三种方法：python列表创建，numpy列表创建，python字典创建

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#1.通过列表创建，包含元组序列等python数据列表
s1 = pd.Series([1,2,3,4,5])
s1


# In[3]:


#2. 传入numpy数组
s2 = pd.Series(np.arange(6))
s2


# In[4]:


# 为序列传入索引，使用index参数。索引长度必须和数据长度相同。
s2 = pd.Series(np.arange(6), index=['a','b','c','d','e','f'])
s2


# In[5]:


# 获取Series值，返回python数组
print(s2.values)
print('*'*20)
print(s2.index)


# In[6]:


print(s1.values)
print('*'*20)
print(s1.index)


# In[7]:


# 3. 通过字典创建
d = {
    'name':'虾米',
    'age':20,
    'class':'三版'
}
d


# In[8]:


#字典是无序数据输出顺序不固定
s3 = pd.Series(d)
s3


# In[9]:


# 按照顺序指定索引。指定顺序时的索引需要大于等于原字典的索引。此处与列表创建不同。
s4 = pd.Series(d,index=['name','age','class'])
s4


# In[10]:


# 如果传入的字典和索引大于字典数据长度，会产生一个NAN数据。
s5 = pd.Series(d,index=['name','age','class','sex'])
s5


# In[11]:


# 字符串作为列表，创建Serise列表时并不分开
pd.Series('小名是个小学生')

