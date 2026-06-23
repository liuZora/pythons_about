#!/usr/bin/env python
# coding: utf-8

# ## 第二讲 pandas库主要内容介绍和Pandas一般命令测试

# 第二讲 pandas库主要内容介绍:
# 
# | 内容简介 | 函数名称 | 简要介绍 | 简单代码案例 |
# | --- | --- | --- | --- |
# | Pandas数据结构 | `pd.Series()` | 一维数组，类似一列Excel表格 | `import pandas as pd; s = pd.Series([1, 3, 5, np.nan, 6, 8]); print(s)` |
# | Pandas数据结构 | `pd.DataFrame()` | 二维表格数据结构 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df)` |
# | Series和DataFrame数据创建和索引选择数据 | `df.loc[]` | 基于标签的索引 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['row1', 'row2']); print(df.loc['row1'])` |
# | Series和DataFrame数据创建和索引选择数据 | `df.iloc[]` | 基于位置的索引 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.iloc[0])` |
# | Series和DataFrame基本功能属性或方法 | `.shape` | 返回DataFrame的形状 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.shape)` |
# | Series和DataFrame基本功能属性或方法 | `.describe()` | 提供描述性统计信息 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.describe())` |
# | Pandas检查缺失值及其处理 | `df.isnull()` | 检查数据中的空值 | `df = pd.DataFrame({'A': [1, np.nan], 'B': [3, 4]}); print(df.isnull())` |
# | Pandas检查缺失值及其处理 | `df.dropna()` | 删除包含缺失值的行或列 | `df = pd.DataFrame({'A': [1, np.nan], 'B': [3, 4]}); print(df.dropna())` |
# | 排序和排序算法 | `df.sort_values()` | 根据值排序 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.sort_values(by='A'))` |
# | 排序和排序算法 | `df.sort_index()` | 根据索引排序 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[2, 1]); print(df.sort_index())` |
# | 数据转化和过滤 | `df.apply()` | 对DataFrame应用函数 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.apply(lambda x: x * 2))` |
# | 日期时间数据处理 | `pd.to_datetime()` | 转换字符串为日期时间对象 | `dates = pd.to_datetime(['2023-01-01', '2023-01-02']); print(dates)` |
# | Pandas数据合并与连接 | `pd.concat()` | 连接多个DataFrame | `df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']}); df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']}); print(pd.concat([df1, df2]))` |
# | Pandas数据合并与连接 | `df.merge()` | 根据一个或多个键合并DataFrame | `left = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']}); right = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']}); print(left.merge(right, on='key'))` |
# | Pandas统计函数及应用 | `df.corr()` | 计算相关系数矩阵 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); print(df.corr())` |
# | Pandas 的逻辑运算符 | `df[df > 0]` | 应用条件过滤 | `df = pd.DataFrame({'A': [1, -1], 'B': [-1, 1]}); print(df[df > 0])` |
# | Pandas IO工具 | `pd.read_csv()` | 读取CSV文件 | `df = pd.read_csv('data.csv'); print(df.head())` |
# | Pandas IO工具 | `df.to_csv()` | 将DataFrame写入CSV文件 | `df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}); df.to_csv('output.csv', index=False)` |
# 

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1.

# In[10]:


help(map)


# ### 2.

# In[ ]:


- 111
- 22
- 44


**python资料可自寻去官网以及github查找**
**开源心态**

`
print('hello world!')
`


# ### 3.

# In[ ]:




