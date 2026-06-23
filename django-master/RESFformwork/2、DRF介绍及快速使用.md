# 一、REST framework

## 1.1 介绍

### **1、特点**

- 提供了定义序列化器serializer的方法,可以快速根据Django ORM或者其他库自动序列化/反序列化。
- 提供了丰富的类视图、Mixin扩展类、简化视图的编写。
- 丰富的定制层级: 函数视图、类视图、视图集合到自动生成API,满足各种需求。
- 多中身份认证和权限认证方式的支持。
- 内置了限流系统。
- 直观的API web界面
- 可扩展性, 插件丰富

### **2、官方文档**

```
https://www.django-rest-framework.org/
```

### **3、源码地址**

```
https://github.com/encode/django-rest-framework/tree/master
```





## 1.2 项目搭建快速使用

### **1、安装**

```
#根据版本
pip install -i https://pypi.douban.com/simple djangorestframework==3.8.2
#直接安装
pip install -i djangorestframework

# 安装完后一定要在settings.py中配置
```

### **2、 settings.py配置**

```python
INSTALLED_APPS =[  
    ''''''
    'rest_framework'
]
```

### 3、可浏览 API

如果您打算使用可浏览 API，您可能还想添加 REST 框架的登录和注销视图。将以下内容添加到您的根`urls.py`文件中。

```
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

### **4、快速入门**

#### 4.1 目录结构

```python
-drf_test   #项目名
    -app01
        ...
        -models.py    #存放模型类
        -
        -serializers.py  #!!!新建，序列化我们的模型类（为了规范新建一个专门存放序列化的文件）
        -tests.py
        -views.py   #存放视图
    -drf_test
        -__init__.py
        -settings.py   # INSTALLED_APPS = [...,'rest_framework',...]
        -urls.py   #注册路由
        -wsgi.py
    -manage.py
```

#### 4.2 基本使用步骤

##### 1、初始化模型类

models.py

```python
from django.db import models
 
class Group(models.Model):
    name = models.CharField(verbose_name='小组名字', max_length=100)
　　
　　def __str__（self）:
　　　　return self.name
 
class Student(models.Model):
    name = models.CharField(verbose_name='学生名字', max_length=100)
    age = models.IntegerField(verbose_name='学生年龄')
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)  #小组和学生之间是 一对多关系
```

```python
# 迁移模型类
python manage.py makemigrations
python manage.py migrate
```

##### 2、序列化模型类

新建一个serializers.py

序列化：把模型数据转成可传输的数据，叫序列化。（输出）

反序列化：把可传输的数据转成模型数据，叫反序列化。（输入）

```python
from .models import Student,Group
from rest_framework import serializers
 
class StudentSerializer(serializers.HyperlinkedModelSerializer):  #HyperlinkedModelSerializer 用的是超链接的序列化
    class Meta:
        model = Student #需要序列化类
        fields = ('id', 'name', 'age', 'group')  #需要序列化的属性，属性是在 序列化类中的，这里就是Student中的字段，group是外键，一样可以加。
 
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
```

##### 3、编辑视图

views.py

````python
```
from .models import Student, Group   #导入模型
from rest_framework import viewsets
from .serializers import StudentSerializer, GroupSerializer  #导入序列化类
 
 
class StudentViewSet(viewsets.ModelViewSet):  #ModelViewSet是最终版，这边我们先认识一下
    queryset = Student.objects.all()  #告诉我们序列化哪些数据，这边就是说吧查出来的学生信息先给我序列化掉
    serializer_class = StudentSerializer  #告诉人家序列化哪个模型类
 
 
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()   #需要序列化的数据
    serializer_class = GroupSerializer   #要哪个序列化类
````

##### 4、路由url

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app01 import views
 
router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)   #访问：http://127.0.0.1:8000/api/students/
router.register(r'groups', views.GroupViewSet)  #访问：http://127.0.0.1:8000/api/groups/
 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),   # => 返回http://127.0.0.1:8000
    path('api/', include(router.urls)), #=> 返回http://127.0.0.1:8000/api
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  #认证
]
```

