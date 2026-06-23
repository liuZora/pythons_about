#!/usr/bin/env python
# coding: utf-8

# ## pandas介绍

# 1. numpy能够帮助我们处理数值型数据，包括以下的主要方法：
# 
#  * 高级特性，广播功能对不同线形状的数据计算
#  * 依托c语言底层计算模块提升速度
#  * 优化计算过程
#  * 同时numpy能够集合matplotlib进行绘图
# 
# 但是存在以下缺点：
# * numpy对除数值型数据之外的数据支持不够，如文本数据和时间序列数据

# 2. pandas的特点
# 
# pandas是一个强大的分析结构化数据的工具集，基于numpy构建，提供了：
# 
# * 高级数据结构
# * 操作数据工具
# 
# 优点：
# 
# * 基于numpy构建，运算速度快,提供高性能的矩阵运算
# * 提供了大量的便捷使用的函数和方法
# * 应用数据挖掘和数据分析
# 
# pandas相当于python版本的excel表格。

# 3. pandas的安装:
# 
# pip install pandas
# 
# 验证是否安装成功，进入python环境后，导入pandas，看是否成功

# In[2]:


import pandas as pd


# In[3]:


si = pd.Series([1,2,3])
si

