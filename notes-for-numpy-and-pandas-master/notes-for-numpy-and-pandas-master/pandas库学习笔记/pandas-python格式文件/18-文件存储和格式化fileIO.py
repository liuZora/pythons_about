#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据加载文件存储和格式化

# 内容介绍:Pandas库自带的读取本地文本文件、网络文件及数据库文件的主要方法

# In[1]:


import numpy as np
import pandas as pd
import json


# In[3]:


# 示例数据
s0 = pd.Series(range(5),index=['d','b','c','a','e'])
print(s0)
df0 = pd.DataFrame(np.random.randint(-9,9,size=(4,3)),index=['d','b','c','a'],columns=['B','A','C'])
df0


# ### 1-1.读取文本格式的文件
# 
# 更详细的教程见:https://blog.csdn.net/u010801439/article/details/80033341

# In[36]:


# 使用read_csv读取csv逗号分隔符文件。默认的分隔符为逗号。
df0 = pd.read_csv('pandas_function.csv')
df0.head(3)


# In[37]:


#读取时index和columns的修改
df01 = pd.read_csv('pandas_function.csv',names=list('abcd'))
df01.head(3)


# In[38]:


#index_col指定列变成行索引。index_col=[column1,column2]，接收两列时，两列变为层次化索引。
df02 = pd.read_csv('pandas_function.csv',index_col=0)
df02.head(3)


# In[39]:


#默认的分隔符为制表符。因此读取csv文件时，不能正确分隔。
df1 = pd.read_table('pandas_function.csv')
df1.head(3)


# In[40]:


#默认的分隔符为制表符。因此读取csv文件时，不能正确分隔。可以设置sep参数为逗号，即可读取csv文件
df2 = pd.read_table('pandas_function.csv',sep=',')
df2.head(3)


# In[47]:


#使用read_excel读取excel文件:xls格式
df31 = pd.read_excel('pandas_function.xls',index_col=0)
df31.head(3)


# In[49]:


#使用read_excel读取excel文件:xlsx格式
df32 = pd.read_excel('pandas_function.xlsx',index_col=0)
df32.head(3)


# ### 1-2.写入文本文件

# In[51]:


#写入csv文件
df02.to_csv('fuc.csv')


# ### 1-3.Json文件的读写
# 
# 详细教程见:https://www.runoob.com/pandas/pandas-json.html

# In[6]:


# 需要规律的json文件，即包含的数据需要等长，过于复杂的无法读取。
df13 = pd.read_json('szse_stock.json')
df13.head(3)


# In[12]:


# 返回值是DataFrame
type(df13)


# In[38]:


# 第一次读取时，由于完整的json值存在stockList键下，我们不能以DataFrame的方式读取出来
# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来


'''
错误的意思是：Unicode的解码（Decode）出现错误（Error）了，以gbk编码的方式去解码（该字符串变成Unicode），
但是此处通过gbk的方式，却无法解码（can’t decode ）。“illegal multibyte sequence”意思是非法的多字节序列，
即没法（解码）了。

    此种错误，可能是要处理的字符串本身不是gbk编码，但是却以gbk编码去解码 。比如，字符串本身是utf-8的，
    但是却用gbk去解码utf-8的字符串，所以结果不用说，则必然出错。

    通过查阅资料，有提出在读取文本的时候加入参数‘b’,不会提示错误，通过输出读取的数据显示。
————————————————
版权声明：本文为CSDN博主「静而守道」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lqzdreamer/article/details/76549256
'''

# 使用 Python JSON 模块载入数据
with open('szse_stock.json','rb') as f:
    data = json.loads(f.read())

# 展平数据
df131 = pd.json_normalize(data, record_path =['stockList'])
print(df131.head())


# In[43]:


# 使用set_index将某一列设置为行索引
df132=df131.set_index('code')


# In[48]:


df132.loc['000001']


# In[50]:


#网络上的http://www.cninfo.com.cn/new/data/szse_stock.json
#需要规则的网络数据，否则报错
URL = 'http://www.cninfo.com.cn/new/data/szse_stock.json'
pd.read_json(URL)


# In[53]:


# 使用python自带的json库读取json文件。
# 任何格式的json文件都可以读取。
import json
with open('szse_stock.json','rb') as f:
    j = json.loads(f.read())
print(j)


# ### 1-4分块读取大文件
# 
# 如何读取大文件的方法

# In[3]:


# 使用chunksize参数，让read_csv分块读取大的文件内容
df=pd.read_csv(r'D:\data\12-2016_yw.csv',chunksize=10,encoding='GB2312')


# In[70]:


# 读取的返回值是一个可迭代的对象
print(df)


# In[73]:


#使用get_chunk()函数，获取每一部分的数据
print(df.get_chunk())


# In[74]:


#返回的数据块类型是DataFrame
print(type(df.get_chunk()))


# In[75]:


df14 = df.get_chunk()


# In[4]:


df14['凭证来源']


# In[80]:


# 使用chunksize参数，让read_csv分块读取大的文件内容
df=pd.read_csv(r'D:\data\12-2016_yw.csv',iterator=True,encoding='GB2312')


# In[5]:


df.get_chunk(5)


# ### 2.二进制格式的数据

# ### 3. Web APIs交互

# ### 4.数据库交互

# ### 5.主要的函数

# In[43]:


# 使用read_html函数获取pandas官网上的文件存取函数
fuctxt = pd.read_html('https://pandas.pydata.org/docs/user_guide/io.html')


# In[7]:


fuctxt[0]


# In[10]:


fuctxt.to_csv('pandas_function.csv')


# * pd.read_csv函数：
# 作用：将csv文件读入并转化为数据框形式。
# 
# pd.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, ...)
# 
# 下面来看常用参数：
# 1.filepath_or_buffer:（这是唯一一个必须有的参数，其它都是按需求选用的）
# 文件所在处的路径
# 
# 2.sep：
# 指定分隔符，默认为逗号','
# 
# 3.delimiter : str, default None
# 定界符，备选分隔符（如果指定该参数，则sep参数失效）
# 
# 4.header：int or list of ints, default ‘infer’
# 指定哪一行作为表头。默认设置为0（即第一行作为表头），如果没有表头的话，要修改参数，设置header=None
# 
# 5.names：
# 指定列的名称，用列表表示。一般我们没有表头，即header=None时，这个用来添加列名就很有用啦！
# 
# 6.index_col:
# 指定哪一列数据作为行索引，可以是一列，也可以多列。多列的话，会看到一个分层索引
# 
# 7.prefix:
# 给列名添加前缀。如prefix="x",会出来"x1"、"x2"、"x3"酱纸
# 
# 8.nrows : int, default None
# 需要读取的行数（从文件头开始算起）
# 
# 9.encoding:
# 乱码的时候用这个就是了，官网文档看看用哪个：
# https://docs.python.org/3/library/codecs.html#standard-encodings
# 
# 10.skiprows : list-like or integer, default None
# 需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）。

# * to_csv(path_or_buf,sep,na_rep,columns,header,index)
# 
# 作用：将数据框写入本地电脑，保存起来
# 
# 参数解析：
# 
# 1.path_or_buf：字符串，放文件名、相对路径、文件流等；
# 
# 2.sep：字符串，分隔符，跟read_csv()的一个意思
# 
# 3.na_rep：字符串，将NaN转换为特定值
# 
# 4.columns：列表，指定哪些列写进去
# 
# 5.header：默认header=0，如果没有表头，设置header=None，表示我没有表头呀！
# 
# 6.index：关于索引的，默认True,写入索引

# In[3]:


help(pd.DataFrame.to_csv)

