#!/usr/bin/env python
# coding: utf-8

# ## 关于numpy的数组创建等基础知识
# 中文文档网站：
# https://www.numpy.org.cn/user/basics

# 一个 ndarray是具有相同类型和大小的项目的（通常是固定大小的）多维容器。<br> 尺寸和数组中的项目的数量是由它的shape定义， 它是由N个非负整数组成的tuple（元组），用于指定每个维度的大小。 <br>数组中项目的类型由单独的data-type object (dtype)指定， 其中一个与每个ndarray相关联。<br>
# 与Python中的其他容器对象一样，可以通过对数组进行索引或切片（例如，使用N个整数）以及通过ndarray的方法和属性来访问和修改ndarray的内容。

# In[15]:


import numpy as np


# In[16]:


# python的列表(数组)可以保存多种数据类型
a = [1,2,'3']
a


# In[17]:


# numpy的数组只能保存一种数据类型
# 将python数组输入numpy中，会自动统一数据类型
b = np.array([4,5,'6'])
b


# In[18]:


#输入的numpy中存在浮点数，numpy全部转换为浮点数
c = np.array([4,5,6.0])
c


# In[19]:


#创建numpy数组的几种方式
#1.使用np.array
a1=np.array([1,2,3])
#创建出的numpy数组print打印出来通python数组显示不同
print(a1)
print(type(a1))


# In[20]:


#np.arange,创建numpy数组的第二种方法
'''
arange([start,] stop[, step,], dtype=None, *, like=None)
'''
a2=np.arange(0,10,2)
a2


# In[21]:


#创建numpy数组的第三种方法,使用随机函数0-1之间的随机小数
a3=np.random.random((2,2))
a3


# In[22]:


#创建numpy数组的第三种方法,使用随机函数整数之间的随机数
a4=np.random.randint(0,9,size=(4,4,))
a4


# In[23]:


#创建numpy数组第四种方法，生成一些特殊的数组
b1=np.zeros((3,3))
b1


# In[24]:


#创建numpy数组第四种方法，生成一些特殊的数组
b2=np.ones((3,3))
b2


# In[25]:


#创建numpy数组第四种方法，生成一些特殊的数组
b3=np.full((2,3),34)
b3


# In[26]:


#创建numpy数组第四种方法，生成一些特殊的数组
b4=np.eye(4)
b4


# In[27]:


a3[0][0]


# In[28]:


#获取函数帮助--第一种方法
get_ipython().run_line_magic('pinfo', 'np.array')


# In[29]:


#获取函数帮助--第二种方法
help(np.array)


# In[ ]:




