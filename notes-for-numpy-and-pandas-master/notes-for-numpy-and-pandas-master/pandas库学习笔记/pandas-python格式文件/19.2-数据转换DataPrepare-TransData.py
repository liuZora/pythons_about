#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据准备-数据转换

# 内容介绍:

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# In[5]:


# 创建重复数据
df0.loc['e'] = df0.loc['a'] 
df0


# ### 1.移除重复数据
# 
#  * 使用duplicated()函数判断重复值
#  * 使用drop_duplicates()函数删除缺失值
#  * drop_duplicates()此种方法不改变原数据
#  * drop_duplicates()传入列标，可以去除某一列的缺失值

# In[6]:


#检查是否存在重复数据，返回布尔型数据
df0.duplicated()


# In[11]:


#删除重复行的方法，返回删除后的数据。此种方法不改变原数据。
# 默认保留第一个出现值的组合
# 不填写任何列参数，表明所有列中出现的行重复值全部删除，保留一项。
df0.drop_duplicates()


# In[12]:


df1 = df0.copy()
df1.loc['d':'b','B'] = df1.loc['a','B']
df1


# In[85]:


#在函数中传入列参数，按照某一列中的值，去除重复项
df1.drop_duplicates('A')


# In[18]:


#由于默认保持第一个出现的重复值。通过设置keep参数，保留以后一个出现的重复值。
df0.drop_duplicates('B',keep='last')


# ### 2.利用函数或映射进行数据转换

# In[91]:


df2 = pd.DataFrame(
{
    'food':['Apple','banana','orange','apple','mango','tomato'],
    'price':[4,3,5,4,3,4],
}
)
df2


# In[44]:


# 添加列，增加数据信息
meat = {
    'apple':'fruit',
    'banana':'fruit',
    'orange':'fruit',
    'mango':'fruit',
    'tomato':'vagetables'
}
    #'Apple':'fruit',


# In[46]:


#获取源数据的映射。注意存在字符串大小写的情况。
df2['food'].map(meat)


# In[47]:


#添加一列，作为分类映射信息
df2['class'] = df2['food'].map(meat)
df2


# In[48]:


#将字符串变为小写。.str.lower()函数直接修改元数据。
low = df2['food'].str.lower()
low


# In[68]:


#将小写数据写入数据源中
df21 = df2.copy()
df21['food'] = low
df21


# In[69]:


#直接只用low序列进行分类列的创建
df21['class'] = low.map(meat)
df21


# In[60]:


df21['class'] = df21['food'].map(meat)
df21


# In[62]:


#利用函数进行创建新的分类列。在map函数中使用匿名函数，将传入在dataframe列中的数据先变为小写再和字典meat中的匹配
df2['food'].map(lambda x :meat[x.lower()])


# In[70]:


df2['class']=df2['food'].map(lambda x :meat[x.lower()])
df2


# ### 3.值替换的普遍方法
# 
#  * 使用replace()函数
#  * 注意区别data.str.replace函数的使用情况

# In[74]:


df3 = pd.Series([1,1000,2,-1444,3])
df3


# In[76]:


#简单的参数为：目标替换的数据和想要替换成的数据
df3.replace(1000,np.nan)


# In[78]:


#使用replace函数，不会改变原数据。函数执行后返回新的数据对象。
df3


# In[80]:


#多数值替换成一个值
df3.replace([1000,-1444],np.nan)


# In[81]:


#多数值替换成对应值
df3.replace([1000,-1444],[np.nan,0])


# In[84]:


#可以使用字典确定替换值和目标值对应的替换结果
df3.replace({1000:np.nan,-1444:0})


# ### 4.重命名轴索引
# 
# 注意和重新索引函数reindex区分

# In[108]:


df4 = df2.copy()
df4


# In[118]:


df4[['ti','d','g']]= np.random.randint(0,9,size=(6,3))


# In[119]:


df4


# In[121]:


# 使用set_index函数，将某一列设置为索引
df41 = df4.set_index('food')
df41


# In[122]:


#重新索引,实际上在原有索引的基础上变化了索引的顺序
df41.reindex(['banana','orange','apple','mango','tomato','Apple'])


# In[123]:


# 重新命名转换
fuc_tran = lambda x:x.upper()
df41.index.map(fuc_tran)


# In[127]:


# 改变索引的方法：直接将索引赋值给原来的索引DataFram.index即可
df41.index = df41.index.map(fuc_tran)
df41


# In[130]:


#也可使用rename函数变更索引
#这种方法变更索引，不会改变原来的数据
df41.rename(index=str.title,columns=str.upper)


# In[135]:


#也可以传入字典函数，将原来的索引变更成对应的数值
#行列的索引都适用这种方式
df41.rename(index={'APPLE':'苹果'},columns={'price':'价格'})


# In[137]:


# 如果需要就地修改dataframe对象，可以添加replace参数进行
df42 = df41.copy()
df42.rename(index={'APPLE':'苹果'},columns={'price':'价格'},inplace=True)
df42


# In[138]:


df41


# In[139]:


df42

