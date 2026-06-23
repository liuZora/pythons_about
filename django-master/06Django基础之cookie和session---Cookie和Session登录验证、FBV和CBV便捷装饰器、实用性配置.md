## cookie

cookie：保存状态信息

保存在浏览器本地上的一组组键值对

特性：

1. 由服务器让浏览器进行设置的
2. cookie信息保存在浏览器本地的，可以浏览器有权不保存
3. 浏览器再次访问时自动携带对应的cookie

**为什么要使用cookie**?

​	Http协议是无状态协议，每次请求之间都是相互独立，没有办法保存状态，使用cookie保存状态。

**Cookie规范**

在响应头中加cookie，维持会话

- Cookie大小上限为4KB；
- 一个服务器最多在客户端浏览器上保存20个Cookie；
- 一个浏览器最多保存300个Cookie，因为一个浏览器可以访问多个服务器。
- 一个浏览器只能有一个用户在同一时间登录同一个网站。

**django中操作cookie**

```python
# 设置cookie:
response.set_cookie(key,value)	#普通cookie (也在Headers添加了响应头Set-Cookie:is_login=1)
response.set_signed_cookie("key",value,salt="s28")	#加密cookie和session一样

设置cookie的参数
# max_age = 5 #超时时间为5秒  (像7天免登录就是设置这个，单位为秒)
# expires=None, 超时时间(IE requires expires, so set it if hasn’t been already.)
# path  cookie生效的路径 ’/’, Cookie生效的路径，/ 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
# domain=None, Cookie生效的域名
# secure=True  https进行传输
# httponly=True  只能http进行传输，无法被js传输（不是绝对，底层抓包可以获取到也可以被覆盖）


# 获取cookie
request.COOKIES  {}  #获取普通cookie(请求头Cookie:is_login=1)
request.get_signed_cookie("key", salt="s28",defalut=" ")  #获取加密的cookie


# 删除cookie 设置cookie 值为空 超时时间为0
response.delete_cook(key)

# 更多参数和资料：https://www.cnblogs.com/maple-shaw/articles/9502602.html
```

**实例一**

```python
# 登录
def login(request):
    if request.method == "POST":
        # 获取用户输入的内容
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "abc" and pwd == "123":  # 登录成功后保存登录状态到cookie中

            # 获取url.返回地址参数，原来是什么，登录以后就会，返回到原来的地方，没有参数就公返回主页面
            url = request.GET.get("url")
            if url:
                return_url = url
            else:
                return_url = reverse("publisher")
            ret = redirect(return_url)
            ret.set_cookie("is_login", "1")  # 设置cookie登录后的信息为1（!!!没有s）
            return ret
        else:
            error = "用户名密码输入有误！"

    return render(request, "login.html", locals())

# 注销 其实就是设置cookie为空 超时时间为0
def logout(request):
    # 清除cookie（某个键值对）
    ret = redirect("/login/")
    ret.delete_cookie("is_login")
    # 重定向到登陆页面
    return ret
```

```python
#设置装饰器
# 判断cookies信息的装饰器
def is_cookies(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        print(request.COOKIES)
        is_login = request.COOKIES.get("is_login")
        if is_login != "1":  # 1表示为登录了(如果清除了cookies也会返回login)
            # 没有登录
            print(request.path_info) # 获取请求参数 /publishers_list/
            return redirect("/login/?url={}".format(request.path_info))  # 拼接成对应的url，好进行返回
        ret = func(request, *args, **kwargs)
        return ret

    return inner
```

set_cookie("is_login", "1")：如果登录成功了就给cookie传值为一个字典 ("is_login", "1")

然后给每一个需要判断的地方加上装饰器，判断，如果传递的cookies是不是为1，不为1就返回login页面

还设置了一个返回原页面的操作：1.先它拼接成url,然后在登录的时候获取参数，就可以返回原来的url



**实例二**

```python
# 不带装饰器
# views.py逻辑
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    # ret = HttpResponse('ok')
    # ret.set_cookie('k1', 'v1')
    is_login = request.COOKIES.get('is_login')
    if is_login == '0':
        return render(request, 'index.html')

    return redirect('login')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        print(name, pwd)
        if name == 'laowang' and pwd == '123':
            ret = redirect('/home/')
            ret.set_cookie('is_login', 0)
            return ret
        else:
            return redirect('login')

def home(request):

    # print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    if is_login == '0':
        return render(request, 'home.html')
    else:
        return redirect('login')
```

```python
# 带装饰器
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# 装饰器
# def wrapper(f):
#     def inner(*args, **kwargs):
#         """添加额外的功能：执行被装饰函数之前的操作"""
#         ret = f(*args, **kwargs)
#         """添加额外的功能：执行被装饰函数之后的操作"""
#         return ret
#     return inner


def wrapper(f):

    def inner(request, *args, **kwargs):
        is_login = request.COOKIES.get('is_login')
        if is_login == '1':
            return f(request, *args, **kwargs)
        else:
            return redirect('login')

    return inner


@wrapper
def index(request):

    return render(request, 'index.html')


@wrapper
def home(request):

    return render(request, 'home.html')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        print(name, pwd)
        if name == 'laowang' and pwd == '123':
            ret = redirect('/home/')
            ret.set_cookie('is_login', 1)
            return ret
        else:
            return redirect('login')

def logout(request):
    rep = redirect("/login/")
    rep.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值
    return rep
```



## session

### 原理

```
cookie可以验证状态，但是你的cookie键和值在浏览器的开发者模式中都是可见的，当然，你也可以在设置cookie时把键值对进行加密处理后发送给浏览器。那么session就是这样的一个类似机制，它在浏览器发出登录请求的时候，随机设置一个字符串cookie值回给浏览器，这个随机字符串叫做session_id，同时会和把你请求带来的数据（session_data）一起作为键值对存储在本地数据库中（| django_session表中），下次浏览器带着session_id来时，去库中查找对应值即可。
```

​	保存在服务器上的一组组的键值对，依赖于cookie使用

为什么要使用session?

	1. cookie是保存在浏览器本地，不太安全。

   	2. 浏览器会对cookie的大小和个数有一定限制的



过程：

1. 第一个请求，没有cookie，设置键值对，根据浏览器生成一个唯一标识，给一个字典设置键值对。
2. 字典转成字符串(序列化)，进行加密，将唯一标识和字符串保存在数据库中(django_session)
3. 返回给浏览器唯一标识(sessionid)的cookie
4. 下次请求携带session_id，服务器根据session找到对应的数据(session_data),进行解密，进行返序列化，根据key获取对应的值。



工作流程：

(1)、当用户来访问服务端时,服务端会生成一个随机字符串；

(2)、当用户登录成功后 把 {sessionID :随机字符串} 组织成键值对加到cookie里发送给用户；

(3)、服务器以发送给客户端 cookie中的随机字符串做键，用户信息做值，保存用户信息；

(4)、再访问服务时客户端会带上session_id，服务器根据session_id来确认用户是否访问过网站



session的默认超时时间是2周

### django中session的相关方法

```python
# 设置session
request.session[key] = value
# 获取
request.session[key]  request.session.get(key)
#删除
del request.session[key]  request.session.pop(key)

# 会话session的key
request.session.session_key

# 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()

# 检查会话session的key在数据库中是否存在
request.session.exists("session_key")

# 删除当前会话的所有Session数据
request.session.delete()
　　
# 删除当前的会话数据并删除会话的Cookie。
request.session.flush() 
    这用于确保前面的会话数据不可以再次被用户的浏览器访问
    例如，django.contrib.auth.logout() 函数中就会调用它。

# 设置会话Session和Cookie的超时时间
request.session.set_expiry(value)
    * 如果value是个整数，session会在些秒数后失效。
    * 如果value是个datatime或timedelta，session就会在这个时间后失效。
    * 如果value是0,用户关闭浏览器session就会失效。
    * 如果value是None,session会依赖全局session失效策略

```



### django中session的相关配置

```
from django.conf import global_settings  # 全局配置
点击global_settings查看所有的配置信息
```



```python
1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置

3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir() 

4. 缓存+数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎

5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎

其他公用设置项：
SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）浏览器关系时就失效
SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```



**实例一**

```python
#装饰器
def is_cookies(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        print(request.COOKIES)
        # is_login = request.COOKIES.get("is_login")  #获取 cookie信息
        is_login = request.session.get("is_login")
        print(is_login,type(is_login))
        if is_login != 1:  # 1表示为登录了(如果清除了cookies也会返回login) ,session返回的是一个整数
            # 没有登录
            print(request.path_info) # 获取请求参数 /publishers_list/
            return redirect("/login/?url={}".format(request.path_info))  # 拼接成对应的url，好进行返回
        ret = func(request, *args, **kwargs)
        return ret

    return inner
    
#login
def login(request):
    if request.method == "POST":
        # 获取用户输入的内容
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "abc" and pwd == "123":  # 登录成功后保存登录状态到cookie中

            # 获取url.返回地址参数，原来是什么，登录以后就会，返回到原来的地方，没有参数就公返回主页面
            url = request.GET.get("url")
            if url:
                return_url = url
            else:
                return_url = reverse("publisher")
            ret = redirect(return_url)
            # ret.set_cookie("is_login", "1")  # 设置cookie登录后的信息为1（!!!没有s）
            request.session["is_login"] = 1  # 设置session
            return ret
        else:
            error = "用户名密码输入有误！"

    return render(request, "login.html", locals())
```



**实例二**

```python
# session
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
    request.session.flush()  # 清楚所有的cookie和session
    return redirect("/login/")

def home(request):

    print(request.session)
    is_login = request.session.get('is_login')
    print(is_login, type(is_login))  # bool
    if is_login:
        return render(request, 'home.html')
    else:
        return redirect('login')
    # return render(request, 'home.html')

def index(request):

    # ret = HttpResponse('ok')
    # ret.set_cookie('k1', 'v1')
    is_login = request.session.get('is_login')
    print(is_login, type(is_login)) # bool
    # 1.从cookie中那session_id
    # 2. 去django_session表中查到对应的值
    # 3. 反解加密的用户数据，并获取需要的数据
    if is_login:
        return render(request, 'index.html')

    return redirect('login')
    # return render(request, 'index.html')

```



session资料网站：https://www.cnblogs.com/maple-shaw/articles/9502602.html



## cookie和session的区别与联系

- 区别
  - session将数据存储与服务器端 cookie存储在客户端
  - cookie 存储在客户端，不安全，sess存储在服务器端，客户端只存sesseionid,安全
  - cookie在客户端存储值有大小的限制，大约几kb。session没有限制
- 联系
  - session 基于cookie