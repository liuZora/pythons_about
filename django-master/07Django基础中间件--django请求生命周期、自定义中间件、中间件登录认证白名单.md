## 中间件

参考：https://www.cnblogs.com/clschao/articles/10480419.html

```python
Django处理浏览器的请求的流程：

a. 请求发送到wsgi，wsgi封装请求的相关数据(request)

b. django去匹配路径，根据路径判断要执行哪个函数

c. 执行函数，函数中处理具体的业务逻辑

d. 函数返回响应，django按照HTTP协议的响应的格式进行返回
```

```
django的中间件是全局范围内处理django的请求和响应的框架级别的钩子

Django中处理请求和相应的框架级别的钩子，本质上是一个类，类定义了5个方法，特定时执行这些方法.
```

```python
settings.py中MIDDLEWARE就是中间件

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### django请求生命周期

![django请求的生命周期](E:\Django设计图\django请求的生命周期.png)



### 创建中间件

	1. 在app01下新建一个文件夹，Middlewares

   	2. 在文件夹下，定义中间件的类My_Middlewares.py
      	3. 编写中间件，一定要继承MiddlewareMixin

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MD1(MiddlewareMixin):
    def process_request(self,request):
        print(id(request))
        print("MD1 request")
        return HttpResponse("如果中间键里面有返回值，就不执行后面的视图函数，连中间键后面的也不执行")
    
```

	4. 注册在settings.py里面的MIDDLEWARE中定义中间件

```
MIDDLEWARE = [
    'app01.Middlewares.My_Middlewares.MD1',
    # 'app01.Middlewares.My_Middlewares.MD2',
]
```



### 5个方法，4个特征

执行时间	执行顺序	参数	返回值

#### process_request

```
process_request(self, request)		#用来处理请求
执行时间：视图函数之前，路由匹配之前
执行顺序：
	按照注册的顺序 顺序执行
参数：
	request请求的对象和视图函数是同一个对象
返回值：
	None 正常流程
	HttpResponse 不执行后面的视图函数，路由匹配，连中间键后面的也不执行，直接返回给浏览器了，直接去执行当前中间件的process_response方法
```

#### process_response

```
process_response(self, request, response)		#用来响应请求
执行时间：视图函数之后(如果里面有具体的返回值，就会覆盖视图函数里面的返回值，)
执行顺序：
	先按照按照注册的顺序执行， 返回process_response的时候就倒序执行
参数：
	request请求的对象和视图函数是同一个对象
	response响应对象
返回值：
	HttpResponse必须返回
```

#### process_view

```
process_view(self,request,view_func,view_args,view_kwargs)		#用来处理视图函数
执行时间：视图函数之前，路由匹配之后
执行顺序：
	按照注册的顺序 顺序执行
	process_view方法是在process_request之后，视图函数之前执行的
参数：
	request请求的对象和视图函数是同一个对象
	view_func视图函数
	view_args视图函数的位置参数 ()元组
	view_kwargs视图函数的关键字参数 {}字典
返回值：
	None 正常流程
	HttpResponse 
		1.如果process_response 里面是return response
			就返回中间件的process_view方法，视图函数都不执行
		2.如果process_response 里面是return HttpResponse
			执行最后一个中间件的process_response方方法
```

#### process_exception

```
process_exception(self, request, exception)		# 视图函数views有异常的时候，才执行
执行时间(触发条件)：视图中有异常才执行
执行顺序：
	按照注册的顺序 倒序执行
参数：
	request请求的对象和视图函数是同一个对象
	exception异常的对象
返回值：
	None 当前的中 间件没有处理异常，交给下一个中间件处理导演，如果 都没有处理导演，django处理异常
	HttpResponse 当前中间件处理了异常，后面的中间件的process_Exception就不执行了，执行最后一个中间件的process_response方法
```

#### process_template_response

```
process_template_response(self, request，response)		#用来处理请求
执行时间(触发条件)：视图函数中返回的对象是TemplateResponse对象

执行顺序：
	按照注册的顺序 倒序执行
参数：
	request 请求的对象和视图函数是同一个对象
	response 返回的TemplateResponse对象
返回值：
	HttpResponse TemplateResponse的对象
	过程处理模板的名字 参数
	response.template_name
	response.context_data
```

process_template_response是在视图函数执行完成后立即执行，但是它有一个前提条件，那就是视图函数返回的对象有一个render()方法（或者表明该对象是一个TemplateResponse对象或等价方法）



### 自定义中间件

中间件顾名思义，是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出

**实例一**

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MD1(MiddlewareMixin):
    def process_request(self, request):
        print("MD1 process_request")
        # ret = HttpResponse("如果中间键里面有返回值，就不执行后面的视图函数，连中间键后面的也不执行")
        # return ret

    def process_response(self, request, response):
        print("MD1 process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(request)  # <WSGIRequest: GET '/index/1'>
        # print(view_func)  # <function index at 0x045FBB68>
        # print(view_args)  # ('1',)
        # print(view_kwargs)  # {'id': '2'}
        print("MD1 process_view")
        # return HttpResponse("MD1 process_view")

    def process_exception(self,request,exception): #视图函数views有异常的时候，才执行
        print("异常")

    def process_template_response(self,request,response):
        print("MD1 process_template_response")
        return response
```

视图函数

```python
from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def index(request,*args,**kwargs):
    print("index")
    # return render(request,"index.html",{"user":"abcdefg"})
    return TemplateResponse(request,"index.html",{"user":"abcdefg"})
```



**实例二**

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MD1(MiddlewareMixin):

    def process_request(self, request):  # 必须定义这个名字的方法，参数必须写的
        print('MD1请求来了')
        print(request.path)  # 请求路径
        if request.path == '/xx/':
            return None
        else:
            return HttpResponse('你有问题，不让你走了！')  # 后边的都不走了
        # return None # 逻辑正常运行完了  不行默认就是return None

    def process_response(self, request, response):  # 必须定义这个名字的方法，两个参数也是必须写的
        print('MD1响应来了')
        return response  # 必须返回response


class MD2(MiddlewareMixin):

    def process_request(self, request):  # 必须定义这个方法
        print('MD2请求来了')

    def process_response(self, request, response):
        print('MD2响应来了')
        return response
# settins文件中配置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义中间件
    'app01.utils.mymiddleware.MD1',
    'app01.utils.mymiddleware.MD2',
]
# 输出
MD1请求来了
/xx/
MD2请求来了
MD2响应来了
MD1响应来了
[20/Nov/2020 09:33:28] "GET /xx/ HTTP/1.1" 200 2
MD1请求来了
/login/
MD1响应来了
[20/Nov/2020 09:33:37] "GET /login/ HTTP/1.1" 200 33
```



### 中间件练习

#### 	实现限制用户访问的频率   5秒只能访问3次

```python
#  1. 设置中间件
# 方法一
"""
  print(request.path_info) # 路径名
  # print(request.META) # 更多参数信息
"""
visit_history = {  #历史时间
    # ip:[time,time]
}
print(visit_history)
class Thorttle(MiddlewareMixin):
    def process_request(self, request):

        ip = request.META['REMOTE_ADDR']  # 127.0.0.1
        history = visit_history.get(ip, [])  # 设置参数  {'127.0.0.1': []}
        print("history:", history)
        # 第一次 history  []
        # 第二次 history  [1597467450]
        # 第三次 history  [1597467450，1597467451]
        # 第四次 history  [1597467450，1597467451，1597467453]

        now = time.time()
        new_history = []  # 每循环一次，让它变为空
        for i in history:
            if now - i < 5:  # 如果新的时间减原来的时间小于5秒就，添加到new_history里
                new_history.append(i)

        visit_history[ip] = new_history
        print(visit_history)
        if (len(new_history)) >= 3:
            return HttpResponse("请稍等一下在访问")
        new_history.append(now)
        
        
# 方法二
visit_history = {  #历史时间
    # ip:[time,time]
}
class Thorttle(MiddlewareMixin):
    def process_request(self, request):

        ip = request.META['REMOTE_ADDR']  # 127.0.0.1
        history = visit_history.get(ip, [])  # 设置参数  {'127.0.0.1': []}

        now = time.time()
        while history and now-history[-1]>5:
            history.pop()
        if (len(history)) >= 3:
            return HttpResponse("请稍等一下在访问")
        history.append(now)
        visit_history[ip] = history
```

2. 在settings.py里面添加

```python
MIDDLEWARE = [
    'app01.Middlewares.My_Middlewares.Thorttle',
]
```





### 中间件认证白名单

就可以用中间件的形式代替装饰器了 ，

```python
# mymiddleware.py
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from django.urls import reverse
# 中间件认证
class SessionAuth(MiddlewareMixin):

    def process_request(self, request):
        # 白名单
        print(request.path)
        white_list = [reverse('login'), ]  # 想让哪个路径过就再列表中加入，一般白名单列表放在settings文件中，然后再这里导入后引用，修改时再settings里改就行了
        print(white_list)
        if request.path in white_list:
            return None

        is_login = request.session.get('is_login')  # session认证
        if is_login:
            return None
        else:
            return redirect('login')

# settins
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义中间件
    # 'app01.utils.mymiddleware.MD1',
    # 'app01.utils.mymiddleware.MD2',
    'app01.utils.mymiddleware.SessionAuth',
]

# views.py
def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        print(name, pwd)
        if name == 'laowang' and pwd == '123':
            # ret = redirect('/home/')
            # ret.set_cookie('is_login', 0)
            # return ret
            request.session['is_login'] = True
            request.session['username'] = 'bo'
            # 1.生成了session_id
            # 2.在cookie里边加上了一个键值对
            # 3.存进django.session表中
            return redirect('/home/')
        else:
            return redirect('login')

def logout(request):
    request.session.flush()  # 清除所有的cookie和session
    return redirect("/login/")

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')
```



### 附：Django请求流程图

![img](https://images2018.cnblogs.com/blog/1168194/201807/1168194-20180719084357413-1778333372.png)

详细资料：https://www.cnblogs.com/maple-shaw/articles/9333824.html

