## 一、Django基础--Web框架

### MVC和MTV框架

#### MVC

把Web应用分为模型（M）、视图（V）、控制器（C）三层，他们之间以一种插件式的，松耦合的方式联系在一起。模型负责业务对象与数据库的映射（ORM），视图负责与用户的交互（页面），控制器接收用户的输入调用模型和视图完成用户的请求。

![MVC](E:\Django设计图\MVC.png)

#### MTV

Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：

- M 代表模型（Model）： 负责业务对象和数据库的关系映射(ORM)。
- T 代表模板 (Template)：负责如何把页面展示给用户(html)。
- V 代表视图（View）： 负责业务逻辑，并在适当时候调用Model和Template。

除了以上三层之外，还需要一个URL分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，View再调用相应的Model和Template，MTV的响应模式如下所示：

![MTV](E:\Django设计图\MTV.png)

一般是用户通过浏览器向我们的服务器发起一个请求(request)，这个请求回去访问视图函数，（如果不涉及到数据调用，那么这个时候视图函数返回一个模板也就是一个网页给用户），视图函数调用模型，模型去数据库查找数据，然后逐级返回，视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。



### Django下载与安装

#### 1. Dango下载

- 命令行
  - pip install Django: 最新版本
  - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11.28 (指定版本)
- 在pycharm中下载(和下载第三方一样)

#### 2.创建项目

- 命令行
  - Django-admin startproject 项目名称
- pycharm
  - File à new project -> 左侧选择django ->选择目录 ->选择解释器->create按钮

#### 3.目录介绍

![image-20200802122257561](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200802122257561.png)

- Settings.py:

  - BASE_DIR：项目的根目录

  - DEBUG=true: 当前是调试模式 

    ​    如果DEBUG=False  ALLOWED_HOSTS=[“*”] 表示所的用户可以访问

  - TEMPLATES=[ “DIRS”:当前文件的地址] :模板

  - **'DIRS': [os.path.join(BASE_DIR, 'templates')]****：指定当前目录的文件夹。**

    ​     **Templates****文件夹是存放html****文件的**

#### 4.运行Django项目

- 命令行
  - python manage.py runserver #默认启动127.0.0.1:8000
  - python manage.py runserver 80 #更改默认端口127.0.0.1:80
  - python manage.py runserver 0.0.0.0:80 #更改Ip和端口
- pycharm
  - ​    不能用右键点击,直接选择项目，点绿三角

#### 5.Django简单示例

1. URL控制器

```python
from App import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^login/$", views.login, name="login") # 对应到views视图，name是一个别名
]
```

2. 在templates模板里写html

```html
<div class="frame">
    <form action="" method="post" >
        {% csrf_token %}
        <h1>欢迎来到我的博客</h1>
        <input type="text" name="user">请输入用户名
        <br>
        <input type="password" name="password">请输入密码
        <br>
        <input type="submit" value="提交">
    </form>
</div>
```

3. views视图

```python
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        user_obj = models.User.objects.filter(username=user, password=password)
        if user_obj:
            return render(request, "index.html")
    return render(request, "login.html")
```

4. 直接访问本地http://127.0.0.1:8000/login/

```
1.创建项目
2.创建app
3.url.py
4.templates
5.views.py
```



#### 6. get，post请求

1. **get请求获取数据**

```
Get请求通常没有请求体,会放到url中
```

2. **post请求获取数据**

```python
POST获取数数会进行安全检验（跨站请求），为了避免有三种方法

1. 在form中添加 {% csrf_token %}
    <form action="" method="post" >
        {% csrf_token %}
    </form>
2. 在form中添加novalidate属性（表示不进行格式验证）
	<form action="" method="post" novalidate>
    
    </form>
3. 在settings.py中注释中间键
	MIDDLEWARE = [ #中间键
    # 'django.middleware.csrf.CsrfViewMiddleware',  注释掉了可以提交POST请求
	]
```



### 登录页面-静态文件的引入

主是要在settings.py中设置STATIC_URL,STATICFILES_DIRS

配置settings.py:

```python
#重要的是settings.py文件的设置（表示找到static文件）
STATIC_URL = '/static/' #静态文件的别名(static是可以修改的)指的是引入文件
# <img src="/static/images/1.jpg"> STATIC_URL里面的static是和引入文件对应的！！！！如果这里是xx那src="/xx/images/1.jpg
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),# 指的是创建的文件夹static,可以有1个或多个(和下面创建的相对应的)
    os.path.join(BASE_DIR,'static1')
]
```

![image-20200802174311380](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200802174311380.png)

步骤: 1.先在bootcss.com网站找到对应的框架，2.把里面需要的内容copy过来 3.下载对应的css文件。4.创建static文件夹 5.在settings.py里面编写对应文件夹的位置 STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static') 6.写html
]

**实例操作**

1. 在项目文件夹下建立一个文件夹存放静态文件，比如叫cctv
2. 在cctv文件夹下再建立一个css文件夹
3. 在css文件夹下建立一个das.css文件

在settings.py文件下写入

```python
STATIC_URL = '/static/' # 别名,一般都起static
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'cctv'),
]
```

```html
  	{% load static %}
	{#这样写了不用管STATIC_URL = '/static/' 叫什么名称了  会自己识别#}
    <link rel="stylesheet" href="{% static 'pulies/bootstrap-3.3.7-dist/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/das.css' %}">

STATIC_URL = '/xxx/' 都可以自动识别
```

```html
{% get_static_prefix %}  这个是就识别当前的 STATIC_URL = '/xxx/ 名字  返回它的名字/xxx/
所有以可以这样写：<link rel="stylesheet" href="{% get_static_prefix %}css/das.css">
```



### app的创建和注册

创建app：

1. 命令行：
   - python manage.py startapp startapp(名称)
2. 通过 run manage.py task
   - tools -> run manage.py task -> 出现窗口 输入命令即可 startapp startapp(名称)

此时新建了一个应用文件startapp，它的里面也创建了一些py文件和包：

　　![img](https://images2018.cnblogs.com/blog/1319275/201806/1319275-20180607120540094-1298179213.png)

　　**migrations** : 用于在之后定义引用迁移功能。

​        admin.py ：管理站点模型的声明文件，默认为空。

　　 **apps.py**   ：应用信息定义文件。在其中生成了类Appconfig，类用于定义应用名等Meta数据。app

　　**models.py**  : 添加模型层数据类的文件。ORM

　　 **test.py**    ：测试代码文件。

　　 **views.py**   ：定义URL响应函数。  函数



注册:

在settings.py文件里面注册：

```
INSTALLED_APPS = [
  	。。。。
    'app01', # 直接写app的名称
    'app01.apps.App01Config' # 推荐写法
]
```



## 二、Django基础--URL路由

### 路由

```python
from django.conf.urls import url

urlpatterns = {  #Django2.0了这里这是path，也可以在settings.py里面查看版本信息
	url(正则表达式,views视图，参数，别名), 
}
```

- 正则表达式：一个正则表达式字符串
- views视图：一个可调用对象，通常为一个视图函数
- 参数：可选的要传递给视图函数的默认参数（字典形式）
- 别名：一个可选的name参数



### **正则表达式**

```
r'^articles/2003/'

r:原生字符串
^:以什么开头
$:以什么结尾
\d:数字  {}:几个数字范围   \w:字母  [0-9][a-z] :0到9的数字和a到z的字符
. 匹配换行符之外的标志
+一个或多个
？0个或1个
*0个或多个
                
```

注意事项

1. urlpatterns中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续。
2. 若要从URL中捕获一个值，只需要在它周围放置一对圆括号（分组匹配）。
3. 不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。
4. 每个正则表达式前面的'r' 是可选的但是建议加上。

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', views.blog),
    # blogs/2012/12/
    url(r'^blogs/[0-9]{4}/\d{2}/$', views.blogs),  #如果不写$的时候，我们访问blog/2002就会被blog给截胡了，因为是从上向下查找的
    url(r'^blogs/[0-9]{4}/$', views.blogs), # blogs/2012/
]
```



```python
# 是否开启URL访问地址后面不为/跳转至带有/的路径的配置项
APPEND_SLASH=True      #就是设置这个为False了django就不会默认加‘/’这个了
```



```python
DEBUG = False  为True表示的是测试环境，上线的是时候要改成这样

ALLOWED_HOSTS = ["*"]
```



### 分组

url地址上捕获的参数会按照 位置传参 方式传递给视图函数

```python
位置传参：()
url(r'^blogs/([0-9]{4})/(\d{2})/$', views.blogs),  
url(r'^blogs/([0-9]{4})/$', views.blogs), # blogs/2012/

    # views.py
def blogs(request,x,y): #一个括号，表示一个参数(位置传参),接送匹配到的数据
	print(x,type(x))
	print(y,type(y))
    return HttpResponse("blogs")
```



### 命名分组

url地址上捕获的参数会按照 关键字传参 方式传递给视图函数

```python
关键字传参:(?P<名称>) (?P<名称>)
    url(r'^blogs/(?P<year>[0-9]{4})/(?P<month>\d{2})/$', views.blogs), 
    
def blogs(request,year,month): # 这里的名称一定要和关键字对应
    print(year,type(year))
    print(month,type(month))
    return HttpResponse("blogs")
    
def blogs(request,*args,**kwargs): #元组，和字典，这样也可以
	print(args)
    print(kwargs)
```

分组和命名分组，不能混合用。捕获的参数永远都是字符串



### 视图函数中指定默认值

```python
# urls.py中
urlpatterns = [
    url(r'^blog/$', views.page),  #没有捕获取到东西的话，将会使用默认值 num=1
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# views.py中，可以为num指定默认值
def page(request, num="1"):
    pass;)
```

在上面的例子中，两个URL模式指向相同的view - views.page - 但是第一个模式并没有从URL中捕获任何东西。

如果第一个模式匹配上了，page()函数将使用其默认参数num=“1”,如果第二个模式匹配，page()将使用正则表达式捕获到的num值。



### 传递额外的参数给视图函数

```python
url(r'^blogs/([0-9]{4})/$', views.blogs,{"k1":"v1"}), # blogs/2012/

def blogs(request,*args,**kwargs):
    print(args)  #('2012',)
    print(kwargs)   #{'k1': 'v1'}
    return HttpResponse("blogs")
```



### include路由分发

1. 在app下重新创建一个urls.py

```python
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^blog/$', views.blog),
    url(r'^blogs/([0-9]{4})/$', views.blogs,{"k1":"v1"}), # blogs/2012/
]
```

2. 改原本项目下的urls.py里面的内容加上include

```python
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^app01/', include("app01.urls")),# http://127.0.0.1:8000/app01/blogs/2002/
    url(r'^', include("app01.urls")),# http://127.0.0.1:8000/blog/  如果为空的话
]
```

里面参数可以为空（其实就是把原来urls.py里面的参数封装到app下，让在用include()调用app下的urls.py）的内容



### url的命名和反向解析

```
其实就是和函数中的as一样 设置一个别名
```

#### 静态路由

```python
命名：name=""

url(r'^blogs/$', views.blogs, name="bloogs"),  # 设置一个别名 bloogs
```

反向解析:  模板  生成的地址

```html
<a href="{% url 'bloogs' %}">测试url的命名和反向解析</a>     --> blogs - bloogs 获取的就是blogs  
其实就是访问了别名为bloogs对应的url
```

py

```python
from django.shortcuts import reverse  #有两种导入的方法
from django.urls import reverse

print(reverse("bloogs"))  #/blogs/
```



#### 动态路由

1. 分组:

```python
    url(r'^blogs/([0-9]{4})/(\d{2})$', views.blogs, name="bloogs"),
```

```python
反向解析：模板

<a href="{% url 'bloogs' '2002' '02' %}">测试url的命名和反向解析</a>
#要给上参数，还要参数对应，不然就会出错.其实就是访问了别名为bloogs对应的url
```

```python
py

print(reverse("bloogs",args=(2002,99)))  # /blogs/2002/99
```



2. 命名分组

```python
    url(r'^blogs/(?P<year>[0-9]{4})/(?P<method>\d{2})$', views.blogs, name="bloogs"),
```

```python
反向解析：模板

{#<a href="{% url 'bloogs' '2002' '02' %}">测试url的命名和反向解析</a>#}  #这个要对应参数
<a href="{% url 'bloogs' method='99' year='2000' %}">测试url的命名和反向解析</a> #这个不用对应参数
其实就是访问了别名为bloogs对应的url
```

```python
py

print(reverse("bloogs",args=(2002,99)))  # /blogs/2002/99
print(reverse("bloogs",kwargs={"year":"2009","method":99}))  # /blogs/2009/9
```



### 命名空间 namespace

```python
app01 urls.py:

urlpatterns = [
    url(r'^home/$', views.home, name='home')
]


app02 urls.py:
urlpatterns = [
    url(r'^home/$', views.home, name='home')
]

#app01和app02我们写了一样的别名
#我们用app01调用html的时候{% url 'home' %}，app02的home会覆盖了app01里面的home
```

为了避免以上操作：我们就要加namespace

```python
# 在项目的urls.py下
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app01/', include("app01.urls", namespace="app01")),
    url(r'^app02/', include("app02.urls", namespace="app02")),
]
```

光加了命名空间，也不行。我们在用反向解析和py的时候，也要在对应的地方区分并添加

```
反向解析：
模块
{% url 'app01:home' %}
{% url 'app02:home' %}
py
 print(reverse("app01:home"))  # /app01/home/
 print(reverse("app02:home"))  # /app02/home/
```



## 三、Django基础--views视图函数

### 视图 CBV和FBV

#### FBV  

```
function based view ,平常用函数写的就是FBV
```

#### CBV 

```
class based view ，用面试对象的方式就是CBV
```

```python
from django.views import View

class xxx(View):
    def dispatch(self, request, *args, **kwargs):
    	return super().dispatch(request, *args, **kwargs)#其实
    
    def get(self,request):
    	#专门处理get请求
        return response
    
    def post(self,request):
    	#专门处理post请求 
        return response
```

```python
url(r"xx/",xxx.as_view()) # 类名.as_view()执行
```



##### as_view()的流程

	1. 项目运行时加载urls.py文件,执行类,as_view()方法
	2. as_view()执行后,内部定义了一个view函数,并且返回.
	3. 请求到来的时候,执行view函数
		1. 实例化类--> self
	    2. self.request = request
		3. 执行self.dispath(request,*args,**kwargs)方法
	        1. 判断请求方式是否被允许
	            1. 允许: - 通过反射获取请求方式对应的请求方法--->handler f.html_method_not_allowed -->handler
				2. 不允许:- self.http_method_not_allowed -->handler
	         2. 执行hanlder,返回结果 

```python
# http_method_names = ['get'] #只允许提交的请求方法，内部执行View这个函数的时候，就会先访问这个类，这个http_method_names就会覆盖内部的这个方法
def dispatch(self, request, *args, **kwargs):
    print("dispatch执行前的操作")
    ret = super().dispatch(request, *args, **kwargs)#其实就是执行View里面内部的dispatch方法
    print("dispatch执行后的操作")
    return ret
```

**CBV执行get和post方法前会,先执行dispatch方法**

使用过程CBV

```
1. 写url url(r"^books/$", views.books.as_view()),
2. 在视图函数写方法
```

```python
# url.py
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r"^books/$", views.books.as_view()),
]

# views.py
from django.views import View


class books(View):

    def dispatch(self, request, *args, **kwargs):
        print("1")
        func = super().dispatch(request, *args, **kwargs)
        print("2")
        return func

    def get(self, request):
        # 专门处理get请求
        return render(request, "login.html")

    def post(self, request):
        # 专门处理post请求
        user = request.POST.get("user")
        password = request.POST.get("password")
        user_obj = models.User.objects.filter(username=user, password=password)
        if not user_obj:
            return render(request, "login.html")
        return render(request, "index.html")
```



#### FBV,CBV加装饰器

##### FBV加装饰器

```
直接加在函数上就行了
```

##### CBV加装饰器

需要使用一个装饰器,导入包method_decorator

```
from django.utils.decorators import method_decorator
@method_decorator 是将函数装饰器转换成方法装饰器。
```

1. 加在方法上

```python
@method_decorator(timer)
def get(self, request):   #这样就只能get方法可以用
```

	2. 加在dispatch方法上

```python
 @method_decorator(timer)  #里面的定义的请求方法都可以用
    def dispatch(self, request, *args, **kwargs):
        print("dispatch执行前的操作")
        ret = super().dispatch(request, *args, **kwargs)#其实就是执行View里面内部的dispatch方法
        print("dispatch执行后的操作")
        return ret
```

	3. 加在类上

```python
@method_decorator(timer,name="get")
@method_decorator(timer,name="post")
@method_decorator(timer,name="dispatch")
class PublishersAdd(View):	#加在类上,可以指定对应的方法
```

装饰器:timer

```python
# 统计时间的装饰器
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """
        inner内部函数
        """
        start = time.time()
        ret = func(*args, **kwargs)
        print("执行一共用时:{}".format(time.time() - start))
        return ret

    return inner

@timer
def func():
    """
    我是func函数
    """
    time.sleep(0.5)
    print("aaaa")

func()
print(func.__name__)  #打印函数名 inner （只有加 @wraps(func)，才可以输出func,自己的函数名）
print(func.__doc__) #打印函数中的注释
```

```python
from functools import wraps
@wraps(func) #加wraps才可以输出自己的函数,和注释,不然会输出内部函数里面的
```



### request（请求）

```Python
常用属性:
request.method  请求方法 GET POST
request.GET  URL上携带的参数  ?k1=v1$k2=v2 {}
request.POST post请求提交的数据 {} 编码方法是URLencode
request.path_info  路径信息 不包含IP和端口 也不包含参数    /publisher_list/
request.body 请求体，byte类型 request.POST的数据就是从body里面提取到的(获取的是post请求提交的内容)
request.COOKIES cookies
request.session session类似于字典的对象
request.FILES  上传的文件
request.META  头的信息   小写-->大写  HTTP_开头

不常用属性:
request.scheme() http或https
request.path() 表示请求的路径组件（不含域名）
```

```python
常用方法:
request.get_full_path()    完整的路径信息 不包含IP和端口 ,包含参数
request.is_ajax()  请求是否是ajax请求
```



### response（响应）

```python
from django.shortcuts import render, HttpResponse, redirect

HttpResponse("字符串")  #返回字符串
render(request,"模板的文件名",{'k1':v1})  #返回一个HTML页面
redirect('地址') #重定向  其实就是给了 Location '地址'和状态码 301 302
```

```python
from django.http import JsonResponse

def text_json(request):
    a = {"a":"b"}
    b = ["aa","bb"]
    return JsonResponse(b,safe=False)  #加safe=False了可以传递列表
```



## 四、Django基础--模板语法

### 模板常用语法

return render(request,"模板的文件名",{"k1":"xxx"})  #返回一个HTML页面

1. Django模板中只需要记两种特殊符号：

   ​	1.1 {{ }}和 {% %}

   ​	1.2 {{ }}表示变量，在模板渲染的时候替换成值，{% %}表示逻辑相关的操作。

2. 点（.）在模板语言中有特殊的含义，用来获取对象的相应属性值

```html
数字:{{ num }}
<br>
字符串:{{ string }}
<br>
字典:{{ name_dict }} --> {{ name_dict.keys }} --> {{ name_dict.values }} --> {{ name_dict.name }}
<br>
列表:{{ name_list }} --> {{ name_list.2 }}
<br>
集合:{{ set }} --> {{ set.1 }}
<br>
元组:{{ tup }}  --> {{ tup.0 }}
<br>
类:{{ person }} --> {{ person.name }} --> {{ person.talk }}
```

```
.
.索引   .key   .属性   .方法(方法后面不加括号)
优先级:
.key > .属性   .方法 > .索引
```



### 过滤器

过滤器的语法： {{ value|filter_name:参数 }}   

使用管道符"|"来应用过滤器。

1. 过滤器：Filters

```python
 return render(request,"template_text.html",{"new_num":""})
 
{{变量|过滤器:"参数"}}
default:
变量不存在或者为空时使用默认值 ,如果value值没传的话就显示nothing
{{ new_num|default:"2" }}
```

2. filesizeformat

```python
# 将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等）

return render(request, "template_text.html", {"value": 1024 * 1024 * 1024})

{{ value|filesizeformat }}  # filesizefomrat:1.0 GB
```

3. add +

```python
给变量加参数
数字的加法，字符串和列表的拼接
add:{{ value2|add:"2" }} --> 列表相加:{{ name_list|add:name_list }}  #add:4 --> 列表相加:['张三', '李四', '王五', '张三', '李四', '王五']
```

4. lower,upper,title

```python
小写:{{value|lower}}
大写:{{value|upper}}
标题:{{value|title}} #首字母大写

可以写在一起:{{value|upper|lower|title}}
```

5. length

```python
{{ value|length }}

返回value的长度，如 value=['a', 'b', 'c', 'd']的话，就显示4.
```

6. slice 切片

```python
{{ name_list|slice:"0:2" }} #和python一样就是没有[]号 [0:2]
```

7. first,last

```python
{{value:first}}  #取第一个元素  和 {{value.0}}一样
{{value:last}}	 #取最后一个元素
```

8. join 字符串拼接

```python
使用字符串拼接列表。同python的str.join(list)。

{{ value|join:" __ " }}  #张三__李四__王五
```

9. truncatechars 字符串截取

```python
如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。
参数：截断的字符数
{{ long_str|truncatechars:9 }} #包括3个省略号  Django...
truncatewords ：根据单词截断
```

10. date 日期格式化

```python
import datetime
    now = datetime.datetime.now()
   
{{ now|date:"Y-m-d H:i:s" }}2020-08-08 10:17:14 

或者直接在settings.py里面定义格式
	1. USE_L10N = False
	2. 设置格式:
		DATETIME_FORMAT = 'Y-m-d H:i:s'
		TIME_FORMAT = 'H:i:s'
		DATE_FORMAT = ‘Y-m-d
		
	然后直接：{{ now }},就和上面一样的
```

11. safe

```python
Django的模板中会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全
比如：
 "safe_text":"<a href='https://www.baidu.com'>点我</a>",
{{ safe_text}} 
我们就会在页面上获得字符串:<a href='https://www.baidu.com'>点我</a>

有时候我们不想这样，我们就可以加个safe
{{safe_text|safe}}  # 点我
```

12. mark_safe

```python
from django.utils.safestring import mark_safe

@register.filter
def show_b(name,url):

    return mark_safe('<a href="{}">{}</a>'.format(url,name))  #直接这样写就不用在用的时候加safe了
    
{{ '百度'|show_b:"http://www.baidu.com" }}
```



### 自定义过滤器 filter

1. 在**app**下创建一个名为templatetags的python包（包的名字不能错，必须叫templatetags）

 2. 创建一个python文件，文件名自定义(mytags.py)

 3. 创建自定义过滤器:

    ```python
    from django import template
    
    register = template.Library()  # register的名字不能错
    
    @register.filter
    def add_arg(value, arg): #只能写二个参数，一个是变量，一个是过滤器的参数
        # 功能
        return "{}__{}".format(value, arg)
    ```

    4. 在html中使用

    在模板中:

    ```html
    {% load mytags %}  #先用load加载 mytags这个文件
    {{ person.name|add_arg:"我爱你" }} 
    ```



### 母版和继承

母版:

	1. 一个包含多个页面的公共部分

   	2. 定义多个block块，让子页面进行覆盖

继承:

```html
1. {% extends "母版的名字" %}  # xx.html
{#    留着模板的内容#}
{{ block.super }}
```

   	2. 重新复写block块 （就是覆盖了母版的block块）

注意点： 

1. {% extends "母版的名字" %} 母版的名字带引号
2. {% extends "母版的名字" %} 写在第一行，上面不在写内容
3. 要显示的内容要写到block块里面
4. 多写一个css\js的block块（因为每一个页面的css\js不可能完全一样）

**例**

```html
创建母版：

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>母版</title>
    <style>
        div{
            width: 500px; height: 500px; border: 2px solid red;
        }
    </style>
     {% block css %} {% endblock %}  {# css#}
</head>
<body>
    <div>
        <a href="">你要干什么？</a>
    </div>
    {% block content %} {# 内容#} {% endblock %}

{% block js %} {# js#} {% endblock %}
</body>
</html>

```

```html
使用母版：

{% extends "Master.html" %}

{% block css %}
    <style>
        div{
            background-color: blueviolet;
        }
    </style>
{% endblock %}

{% block content %}
    <h1>123321</h1>
{% endblock %}

{% block js %}

{% endblock %}
```



### 组件 include

```
可以将常用的页面内容如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方，文件的任意位置按如下语法导入即可。
```

 1. 把一小段公用的HTML文本写入一个HTML文件，nav.html

 2. 在需要该组件的模版中导入

    ```
    {% include 'nav.html' %}
    ```

**示例**

```html
创建组件
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>组件</title>
    <style>
        *{
            list-style: none; margin: 0; padding: 0;
        }
        div{
            height: 50px; border: 1px solid red;
        }
        div ul li{
            width: 100px; height: 35px; border: 1px solid green; margin-left: 50px; float: left;
        }
    </style>
</head>
<body>
    <div>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>
    </div>
</body>
</html>
```

```html
使用组件
{% extends "Master.html" %}

{% block css %}
    <style>
        div{
            background-color: blueviolet;
        }
    </style>
{% endblock %}

{% block content %}
    {% include "nav.html" %}
    <h1>123321</h1>
{% endblock %}

{% block js %}

{% endblock %}
```



### 标签tags

1. **for**

```
<ul>
    {% for name in name_list %}
        <li>{{ forloop.counter }}-{{ name }}</li>
    {% endfor %}
</ul>
```

for循环可用的一些参数：

| Variable              | Description                          |
| --------------------- | ------------------------------------ |
| `forloop.counter`     | 当前循环的索引值（从1开始）          |
| `forloop.counter0`    | 当前循环的索引值（从0开始）          |
| `forloop.revcounter`  | 当前循环的倒序索引值（到1结束）      |
| `forloop.revcounter0` | 当前循环的倒序索引值（到0结束）      |
| `forloop.first`       | 当前循环是不是第一次循环（布尔值）   |
| `forloop.last`        | 当前循环是不是最后一次循环（布尔值） |
| `forloop.parentloop`  | 本层循环的外层循环                   |

**for ...empty**

```
{% for name in name_list2 %}
    <li>{{ name }}</li>
{% empty %}
    为空了   #如果循环的对象为空的话，就输出它
{% endfor %}
```



2. **if**

```
{% if value2 > 2 %}
    可以
{% elif  value2 == 2 %}
    不错
{% endif %}
```

if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断。

注意：

 1. 条件中不支持算术运算

 2. 不支持连续判断

    ```
    {% if 5 > 4 > 1 %}  这样会报错  只有改成{% if 5 > 4 and 4 > 1 %}
        ok
    {% else %}
        no
    {% endif %}
    ```

**with**

就是重命名

```
{% with name_list as name%}
    {{ name }}
    {{ name }}
{% endwith %}

或者
{% with name = name_list %}
    {{ name }}
    {{ name }}
{% endwith %}
```



### 自定义标签 simple_tag

1. app应用文文件夹中创建templatetags文件夹，必须是这个名字；

2. templatetags文件夹中创建一个xx.py文件，名字可以随便起。    

3. 创建自定义标签
	
```python
   from django import template
   
    register = template.Library()  # register固定的名字
    @register.simple_tag
    def mytag(v1):
     s = v1 + '我爱你'
        return s
   
    @register.simple_tag
    def mytag2(v1, v2, v3):
        s = v1 + v2 + v3
        return s
```

4. 使用 html文件中的 {%  load 文件名  %}
    {% load te %}
    <h>
        {% mytag s1 %}
        {% mytag2 s1 'yyz' 'lt' %}
    </h> 
    
5. 注意：参数可以有多个。        


### inclusion_tag

filter， simple_tag，inclusion_tag

没有参数限制的

1. 在**app**下创建一个名为templatetags的python包（包的名字不能错，必须叫templatetags）

 2. 创建一个python文件，文件名自定义(mytags.py)

 3. 在python包中写:

    ```python
    from django import template
    
    register = template.Library()  # register的名字不能错
    ```

    4. 写函数+加装饰器

    ```python
    filter：
    def add_arg(value,arg): #只能接受一个参数和值 
        return "xx"
    
    simple_tag:
    @register.simple_tag  # 可以接受多个参数和值
    def str_join(*args, **kwargs):
        return "{}_{}".format("---".join(args), "***".join(kwargs))
    
    inclusion_tag：
    @register.inclusion_tag("page.html") #把值返回到page.html页面上
    def pagination(num):
        return {'num': range(1, num + 1)}  # 需要返回的是一个字典
    
    ```

    5. 使用

    ```html
    filter:
    {% load mytags %}
    {% "alex"| add_arg:"我爱你" %}
    
    simple_tag:
    {% load mytags %}
    {% str_join "a" "b" "c" k1="aa" k2="bb" %}
    {#a---b---c_k1***k2#}
    
    inclusion_tag：
    {% load mytags %}
    {% pagination 6 %}
    ```



### 实例(分页)

```python
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 方法一
@register.simple_tag
def pagination(num):
    page_list = ['<li><a href="#">{}</a></li>'.format(i) for i in range(1,num+1)]
    print(page_list)
    return mark_safe("""
    <nav aria-label="Page navigation">
      <ul class="pagination">
    <li>
      <a href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    {}
    <li>
      <a href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>""".format(''.join(page_list)))


```

```python
# 方法二：
@register.inclusion_tag("page.html")
def pagination(num):
    return {'num': range(1, num + 1)}  # 需要返回的是一个字典

<nav aria-label="Page navigation">
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        {% for page in num %}
            <li><a href="#">{{ page }}</a></li>
        {% endfor %}
        <li>
            <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>
```



