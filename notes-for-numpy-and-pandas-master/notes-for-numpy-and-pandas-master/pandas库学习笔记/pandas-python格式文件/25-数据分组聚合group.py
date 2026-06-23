#!/usr/bin/env python
# coding: utf-8

# ## Pandas:数据的分组和聚合

# 内容介绍:
# 
# 数据分组汇总演示图
# 
#  ![avatar](combine.png)

# In[7]:


import numpy as np
import pandas as pd
import json


# In[11]:


# 示例数据
# 使用 Python JSON 模块载入数据
with open('szse_stock.json','rb') as f:
    data = json.loads(f.read())

# 展平数据
df = pd.json_normalize(data, record_path =['stockList'])
print(df.head())


# In[12]:


df0 = pd.read_csv('directory.csv')
df0.head()


# In[51]:


idx = pd.Index(['小刚','小花','小敏','小强','小明'],name='姓名')
cls = pd.Index(['语文','英语','数学'],name='科目')
df00 = pd.DataFrame(np.random.randint(50,98,size=(5,3)),index=idx,columns=cls)
df00['班级']=['二班','一班','二班','一班','一班']
df00['性别']=['男','女','男','女','男']
df00


# ### 1.groupby()

# In[52]:


#groupby()函数返回迭代对象。包含组名的元组序列
g = df00.groupby(by='班级')


# In[53]:


for i in g:
    print(i)


# In[69]:


for bj,da in g:
    print('组名:{}'.format(bj))
    print('*'*20)
    print(da)
    print(type(da))


# In[73]:


#使用两个条件分组
g2 = df00.groupby(by=['班级','性别']).mean()
g2


# In[74]:


type(g2)


# ### 2.聚合方法
# 
# groupby()形成的对象，本身具有计算聚合值的方法。

# In[62]:


#获取班级的平均分。
g = df00.groupby(by=['班级'])
g.mean()


# In[63]:


#也可以在group对象后面获取单独的列，进行计算
g['语文'].mean()


# In[65]:


#在分组返回值的基础上语法糖的简化写法
df00['语文'].groupby(df00['班级']).mean()


# In[67]:


#as_index参数的使用方法，优化显示结果的索引
df00.groupby(by=['班级'],as_index=False).mean()


# In[ ]:





# ### 3.自定义聚合函数的方法???

# In[68]:


#计算每个人的分数同班级平均分的差
def my_diff(arr):
    return arr.max()-arr.min()

#agg/aggregate
df00.groupby(by=['班级']).agg(my_diff)


# ### 4.数据处理拓展
# 
# 针对星巴克门店数据的初步分析

# In[87]:


g4 = df0.groupby('Country').count()
g4


# In[88]:


g4.iloc[:20]


# In[79]:


type(g4)


# In[116]:


g4.loc[['US','CN']]


# In[119]:


g4.size

