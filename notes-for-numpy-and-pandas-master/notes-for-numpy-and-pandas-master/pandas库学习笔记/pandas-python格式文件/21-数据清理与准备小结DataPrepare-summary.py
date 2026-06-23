#!/usr/bin/env python
# coding: utf-8

# ## Pandas-数据清理与准备总结

# 内容介绍:前面课程的总结。

# ### 数据不规范的表现及主要处理方式
# 
# * 如果全部在原始数据中进行处理操作的情况下，注意不同操作顺序会改变行序号导致后续操作不能执行

#  * 部分数据缺失，存在大量的空值。处理方式：
#  
# 找到：DataFrame.isnull()函数找到缺失值。(DataFrame.isnull()).sum()获取存在缺失值列的数量汇总。<br>
# 填充:DataFrame.fillna()<br>
# 删除：DataFrame.dropna(subset='列名',replace=Ture)。删除某列的缺失值。<br>

#  * 数据存在重复值
# 
# 找到：DataFrame.duplicated()返回缺失值的Series序列。DataFrame.duplicated().sum()查看缺失值的数量。<br>
# 删除：DataFrame.drop_duplicates(inplace=True)，在元数据上伤处重复数据。<br>

#  * 部分数据包含数值和字符串，数据类型不统一。字符串的处理方式：
# 
# 检测字符串:DataFrame.[某列名].str.contains()，查看是否包含某字符串。<br>
# 字符串替换：DataFrame.[某列名].map(lambda x:x.replace('万',''))<br>
# 字符串替换(第二种方法)：DataFrame.[某列名].map(lambda x:float(x.replace('万','')))  ## 使用python的float函数转换<br>
# 数字类型转换：DataFrame.[某列名].map(lambda x:x.replace('万','')).astype(np.float32) ##使用pandas的astype函数转换<br>

#  * 部分数据存在异常值
# 
# 检测异常值的行：<br>
# 删除异常值的行：Dataframe.drop([行坐标值],replace=True)<br>

#  * 少数数据不利于分析
