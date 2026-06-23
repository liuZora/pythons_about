#!/usr/bin/env python
# coding: utf-8

# ## 00-第二讲 numpy库主要内容介绍：
# 
# | 内容简介               | 函数名称        | 简要介绍                                               | 简单代码案例                                     |
# |:-----------:|:------------|:-----------------------------------------------------|:---------------------------------------------|
# | Numpy数组的基本属性       | `.ndim`     | 返回数组的维度                                           | `import numpy as np; a = np.array([1, 2, 3]); print(a.ndim)` |
# |                      | `.shape`    | 返回数组的形状                                           | `print(a.shape)`                             |
# |                      | `.size`     | 返回数组中元素的总数                                       | `print(a.size)`                              |
# |                      | `.dtype`    | 返回数组元素的数据类型                                      | `print(a.dtype)`                             |
# | Numpy数组创建           | `np.array`  | 将列表转换为Numpy数组                                     | `a = np.array([1, 2, 3])`                    |
# |                      | `np.zeros`  | 创建一个指定形状和数据类型的全0数组                             | `b = np.zeros((2, 3))`                       |
# |                      | `np.ones`   | 创建一个指定形状和数据类型的全1数组                             | `c = np.ones((2, 3), dtype=int)`             |
# |                      | `np.arange` | 创建一个具有给定间隔的数组                                   | `d = np.arange(10)`                          |
# |                      | `np.linspace`| 创建一个在指定区间内具有均匀间隔的数组                           | `e = np.linspace(0, 10, num=5)`              |
# | Numpy数组对象的切片和索引   | `[]`        | 通过索引和切片操作来获取数组的一部分                             | `print(a[1:3])`                              |
# |                      | `np.newaxis`| 增加一个新的轴来扩展数组的维度                                 | `print(a[:, np.newaxis])`                    |
# |                      | `.flatten`  | 将多维数组降为一维数组                                      | `print(a.flatten())`                         |
# |                      | `.reshape`  | 改变数组的形状而不改变其数据                                   | `print(a.reshape(1, 3))`                     |
# | Numpy函数及其应用         | `np.sum`    | 计算数组元素的和                                          | `print(np.sum(a))`                           |
# |                      | `np.prod`   | 计算数组元素的乘积                                         | `print(np.prod(a))`                          |
# |                      | `np.mean`   | 计算数组元素的平均值                                        | `print(np.mean(a))`                          |
# |                      | `np.std`    | 计算数组元素的标准差                                        | `print(np.std(a))`                           |
# |                      | `np.dot`    | 计算两个数组的点积                                         | `f = np.array([1, 2]); print(np.dot(a, f))`  |
# | Numpy IO工具            | `np.save`   | 将数组保存到.npy文件中                                      | `np.save('array.npy', a)`                    |
# |                      | `np.load`   | 从.npy文件中加载数组                                       | `g = np.load('array.npy')`                   |
# |                      | `np.savetxt`| 将数组保存到文本文件中                                      | `np.savetxt('array.txt', a)`                 |
# |                      | `np.loadtxt`| 从文本文件中加载数组                                       | `h = np.loadtxt('array.txt')`                |
# 请注意，这些函数和代码案例是最基础的示例。在PPT以及实际应用中，有很多可选参数和更高级的用法。
# 

# ## numpy测试函数使用的文档

# In[2]:


import numpy as np


# In[3]:


np.arange(9,dtype=np.float32)


# In[19]:


l=[1,2,3,4]


# In[22]:


l[0:2]


# In[23]:


get_ipython().run_line_magic('pinfo', 'np.random.choice')


# In[ ]:




