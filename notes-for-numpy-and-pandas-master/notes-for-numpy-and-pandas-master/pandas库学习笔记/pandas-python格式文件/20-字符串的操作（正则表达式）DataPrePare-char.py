#!/usr/bin/env python
# coding: utf-8

# ## Pandas-字符串的操作

# 内容介绍:处理获取数据中的字符串。

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1.常用的字符串对象方法。python本身的字符串方法。

# In[4]:


s = 'a, b,   c'


# In[5]:


#分割字符串
s.split(',')


# In[6]:


# 删除字符串中的空格，包括\n
l_s = [x.strip() for x in s.split(',') ]
l_s


# In[7]:


a,b,c=l_s
a,b,c


# In[9]:


a+'::'+b+'::'+c


# In[10]:


#列表中的字符串的合并
'::'.join(l_s)


# In[11]:


#检测字符串是否包含使用in关键字
'c' in l_s


# In[12]:


#获取某个字符在字符串中的索引下标。如果元素没有，那么会返回异常。
s.index(',')


# In[13]:


#在字符串中查找某个字符。如果没查到返回值-1。查找到时，返回索引值。
s.find(':')


# In[14]:


#字符串的替换。替换不改变原始值。
s.replace('a','k')


# In[17]:


#替换目标值为空字符串时，表明去除某个字符串。
s.replace(',','')


# ### 2.正则表达式

# In[18]:


import re


# In[19]:


text = 'foo   bar\t  bat   \tqq'


# In[20]:


#直接使用正则表达式对象
#\s表示空格和\t换行符号，+号表示匹配0-n次
re.split('\s+', text)


# In[21]:


#使用编译后的正则表达式对象
#可以重复使用编译后的正则表达式对象
res = re.compile('\s+')
res.split(text)


# In[22]:


#字符串中查找，返回所有的匹配结果，返回这些结果的列表
res.findall(text)


# In[23]:


#findall函数的另一种写法，等效函数
re.findall(res,text)


# In[26]:


#match函数的使用。需要从字符串的开头匹配。可以用于匹配整个单词。
m1 = re.match('o',text)
print(m1)


# In[25]:


#match函数查看具体值
m1.group()


# In[28]:


#使用serch进行匹配，只能找到一个匹配项
s1 = re.search('b',text)


# In[29]:


s1.group()


# ### 3.pandas矢量化字符串函数

# In[34]:


dic = {
    'a':'asdf@qq.com',
    'b':'sdwtr@lso.com',
    'c':'qlop@gmailcom',
    'd':'qpx@gmail.com',
    'e':np.nan
}
s30 = pd.Series(dic)
s30


# In[36]:


s30.isna()


# In[38]:


# 获取邮箱名称的部分
#由于存在nan为浮点数类型，不能使用split进行分割
s30.map(lambda x :x.split('@'))


# In[40]:


#使用Series.str方法进行分割。此种方法的分割，可以忽略一些错误值。
s30.str.split('@')


# In[41]:


#Series.str检测是否包含某个字符
s30.str.contains('gmail')


# In[44]:


#查找特定字符
s30.str.findall('@')


# In[46]:


#批量截取字符串
s30.str[:5]


# ### pandas字符串的方法汇总:

# pandas字符串方法总体上使用方法同python一致，但python面对的是单个字符串，pandas字符串方法面对的是批量的字符串
#  * 具体各方法的说明可以参照：
#  * http://www.pypandas.cn/docs/user_guide/text.html#%E6%96%B9%E6%B3%95%E6%80%BB%E8%A7%88
