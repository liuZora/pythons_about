#!/usr/bin/env python
# coding: utf-8

# ## Pandas-Dask基本数据处理速度比较

# 内容介绍:

# In[2]:


import numpy as np
import pandas as pd
import dask.dataframe as dd


# In[4]:


get_ipython().run_cell_magic('time', '', "# pandas获取数据\ndf = pd.read_csv('/home/ubuntu/Documents/12-2016_yw.csv',encoding='GB18030')#,encoding='utf-8'\ndf.head(3)\n")


# In[5]:


get_ipython().run_cell_magic('time', '', "#使用Dask模块读取csv数据\nddf = dd.read_csv('/home/ubuntu/Documents/12-2016_yw.csv',encoding='GB18030')#,encoding='utf-8'\nddf.head(3)\n")


# In[ ]:





# In[ ]:




