#!/usr/bin/env python
# coding: utf-8

# ## numpt,DataFrame通过索引的基本操作-重新索引和增加

# In[31]:


import numpy as np
import pandas as pd


# In[32]:


ser1 = pd.Series(range(5))
ser1


# In[33]:


df1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
df1


# ### 1. 重新索引。
# 
# pd.DataFrame.reindex(labels=None,index=None,columns=None,axis=None,method=None,copy=True,<br>level=None,fill_value=nan,limit=None,tolerance=None,)
# 
#  * reindex()方法用于将原来的数据重新排列。用于dataframe时可以针对行或列重新排列，变换index或columns参数即可。
#  * 重新排列后有利于按照正常顺序查看数据
#  * 行或列的index参数需要是原行列索引的范围内。
#  * fill_value参数用于在重新索引中填充缺失位置的值
#  * method,缺失值填充方法。向前填充：缺失值后面的值向前填充。也有向后填充的方法。
#  * copy,默认为True,生成新的对象。为False时，新旧相等不复制。

# In[34]:


# 创建一个符合新索引的新对象
# 由于原来数据中并没有下述参数的索引值，因此，返回值都为NaN
ser2 = ser1.reindex(['a','b','d','c','e'])
ser2


# In[35]:


# dataframe行索引重建。默认指向行索引。建议明确指定index或columns参数。或使用axis参数指定轴。

df2 = df1.reindex(['a','b','c','d'])
df2


# In[36]:


df3 = df1.reindex(['c','b','a','d'])
df3


# In[37]:


#通过新增索引的方式增加数据
#首先通过索引的insert()方法，在形成一个新的索引，增加了索引'F'
#再通过reindex()方法中的填充参数，变更原来的索引和增加了填充数据。
newc = df1.columns.insert(3,'F')
df_n = df1.reindex(columns=newc,fill_value=8)
df_n


# In[38]:


df_n.index


# ### 2. 通过 索引增加数据

# ### 2.1Series增加数据方法

# In[39]:


ser1


# In[40]:


#使用索引增加数据项，此方法会修改原数据
ser1['g']=8
ser1


# In[41]:


#使用append()方法，在原有的数据基础上添加。不修改原有数据。
ser2 = pd.Series({'f':45})
print(ser2)
ser3 = ser1.append(ser2)
ser3


# In[42]:


ser1


# ### 2.2 DataFrame的列 增加数据索引-使用索引

# In[43]:


# 使用索引的方式给dataframe增加数据
df1


# In[44]:


# 使用索引的方式默认增加列
# 只给一个数值的时候，所有的行增加的数值相同
df1['D']=5
df1


# In[45]:


# 增加列：如果增加的每行数值不同，可以给一个数组赋值
df1['F'] = [6,7,9]
df1


# ### 2.3 DataFrame的行 增加数据索引-使用insert函数

# In[46]:


# 增加列，时选择增加的位置。使用insert()函数
# insert函数:pd.DataFrame.insert(loc,column,value,allow_duplicates: 'bool' = False,)
# loc:增加的列位置；column:增加的列名称；value:增加列的值。
df1.insert(0,'J',[9,6,3])
df1


# ### 2.4 DataFrame的行 增加数据索引-使用高级索引标签

# In[47]:


# dataframe增加行的操作,需要使用高级标签索引loc
# 增加数据的列数需和原数组数据相同
#df1.loc['l'] = [1,2,3,4,6]
df1.loc['l'] = [1,2,3,4,5,6]
df1


# ### 2.5 DataFrame的行 增加数据索引-使用append函数

# In[48]:


# 通过append()函数添加数据
# 添加的数据是本身没有行索引的情况下，通过此方式会忽略原来的索引，自动添加数字索引。
# 在列方向上，添加的数据会自动找到对应的列；而没有找到的列会成为Nan值。
row = {'E':3,'A':4,'B':2,'C':8,'D':9}
print(row)
df5 = df1.append(row,ignore_index=True)
df5


# In[49]:


np.random.rand(2,3)


# In[50]:


#如果在dataframe上增加一个dataframe数据，那么默认索引会叠加
df8 = pd.DataFrame(np.random.rand(2,3),index=['A','B'],columns=['A','B','C'])  #,index=['A','B','C']
df8


# In[51]:


df9 = df1.append(df8)
df9


# In[52]:


get_ipython().run_line_magic('pinfo', 'pd.DataFrame.reindex')

