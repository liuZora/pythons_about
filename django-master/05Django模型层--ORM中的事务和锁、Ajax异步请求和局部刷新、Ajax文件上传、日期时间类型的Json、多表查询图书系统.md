## 一、ORM中的事务和锁

### 事务

事务要确保原子性

```python
"""
事务
	ACID
		原子性：不可分隔的最小单位
		一致性：跟原子性是相辅相成
		隔离性：事务之间相互不干扰
		持久性：事务一旦确认永久生效
	
	事务的回滚
		rollback
	事务的确认
		commit
"""
# 目前是需要
from django.db import transaction

with transaction.atomic(): 开启事务
    # sql1
    # sql2
    # 的with代码块中写的所有orm操作都是属于同一个事务
print("执行其他操作")
```



```python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()

from app01 import models

from django.db import transaction
from django.db.models import F, Q

# 事务要确保原子性
# 原子性：一个原子事务要么完整执行，要么干脆不执行。这意味着，工作单元中的每项任务都必须正确执行。如果有任一任务执行失败，则整个工作单元或事务就会被终止。
try:
    with transaction.atomic(): # 开启事务
        # 一系列的操作
        models.Book.objects.all().update(kucun=F("kucun") - 10)
        models.Book.objects.all().update(sale=F("sale") + 10)
except Exception as e:
    print(e)
```

下面再说一些设置事务的小原则吧：

　　　　1.保持事务短小
　　　　2.尽量避免事务中rollback
　　　　3.尽量避免savepoint
　　　　4.默认情况下，依赖于悲观锁
　　　　5.为吞吐量要求苛刻的事务考虑乐观锁
　　　　6.显示声明打开事务
　　　　7.锁的行越少越好，锁的时间越短越好



### 锁

#### 行级锁

```python
entries = Entry.objects.select_for_update().filter(author=request.user)  #加互斥锁，由于mysql在查询时自动加的是共享锁，所以我们可以手动加上互斥锁。create、update、delete操作时，mysql自动加行级互斥锁

SELECT * FROM t1 WHERE id=1 FOR UPDATE;
model.T1.objects.select_for_update().filter(id=1)
```

#### 表锁

```python
class LockingManager(models.Manager):
    """ Add lock/unlock functionality to manager.
Example::

    class Job(models.Model): #其实不用这么负载，直接在orm创建表的时候，给这个表定义一个lock和unlock方法，借助django提供的connection模块来发送锁表的原生sql语句和解锁的原生sql语句就可以了，不用外层的这个LckingManager(model.Manager)类

        manager = LockingManager()

        counter = models.IntegerField(null=True, default=0)

        @staticmethod
        def do_atomic_update(job_id)
            ''' Updates job integer, keeping it below 5 '''
            try:
                # Ensure only one HTTP request can do this update at once.
                Job.objects.lock()

                job = Job.object.get(id=job_id)
                # If we don't lock the tables two simultanous
                # requests might both increase the counter
                # going over 5
                if job.counter < 5:
                    job.counter += 1                                        
                    job.save()

            finally:
                Job.objects.unlock()
"""    

def lock(self):
    """ Lock table. 

    Locks the object model table so that atomic update is possible.
    Simulatenous database access request pend until the lock is unlock()'ed.

    Note: If you need to lock multiple tables, you need to do lock them
    all in one SQL clause and this function is not enough. To avoid
    dead lock, all tables must be locked in the same order.

    See http://dev.mysql.com/doc/refman/5.0/en/lock-tables.html
    """
    cursor = connection.cursor()
    table = self.model._meta.db_table
    logger.debug("Locking table %s" % table)
    cursor.execute("LOCK TABLES %s WRITE" % table)
    row = cursor.fetchone()
    return row

def unlock(self):
    """ Unlock the table. """
    cursor = connection.cursor()
    table = self.model._meta.db_table
    cursor.execute("UNLOCK TABLES")
    row = cursor.fetchone()
    return row
```



## 二、Ajax

参考https://www.cnblogs.com/clschao/articles/10468335.html

### 　**1.简介**

　　　　AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步的Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML,现在更多使用json数据）。

　　　　AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

　　　　AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。（这一特点给用户的感受是在不知不觉中完成请求和响应过程）

　　　　AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。

　　　　　　a.**同步交互**：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；

　　　　　　b.**异步交互**：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。

 　AJAX除了**异步**的特点外，还有一个就是：浏览器页面**局部刷新**；（这一特点给用户的感受是在不知不觉中完成请求和响应过程

```html
特性：
	1.异步请求
	2.局部刷新
	<script>
    $('#btn').click(function () {
        $.ajax({
            {#url:'/login/',#}
            url:"{% url 'login' %}",
            type:'post',
            data:{
                csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
                {#csrfmiddlewaretoken:"{{ csrf_token }}",#}
                name:$('#username').val(),
                pwd:$('#password').val(),
            },
            success:function (res) {
                var resStr = JSON.parse(res)
                if (resStr['code'] == 0){
                    location.href=resStr['redirect_url']
                }else{
                    if(resStr['code'] == 3){
                        var spanEle = document.createElement('span');
                        $(spanEle).text(resStr['warning'])
                        $('form').append(spanEle)
                    }
                }

                console.log(resStr)
            }
        })
    })
```

### 2.ajax请求和响应

```html
# urls.py
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.LoginView.as_view(),name='login'),
    url(r'^index/', views.IndexView.as_view()),
]
# views.py
class LoginView(View):

    def get(self, request):

        # return render(request, reverse('login'))
        return render(request, 'login.html')

    def post(self, request):
        # name = request.POST.get('username')
        # password = request.POST.get('passwoame')
        name = request.POST.get('name')
        password = request.POST.get('pwd')
        print(name, password)
        if name == 'laowang' and password == '123':
            ret = {'code': 0, 'redirect_url': '/index/'}
            ret = json.dumps(ret)
            return HttpResponse(ret)
        else:
            ret = {'code':3,'warning': '用户名或者密码错误！！！'}
            ret = json.dumps(ret)
            # return HttpResponse(ret)
        	return HttpResponse(ret, content_type='application/json') # 加上这个后在ajax中就不必在进行json解析了

class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')
# login.html
<body>
<h1>你好，世界！</h1>
<form action="/login/" method="post">
    {% csrf_token %}
    用户名： <input type="text" id="username" name="username">
    密码：   <input type="password" id="password" name="password">
{#    submit和button就会触发form表单请求#}
{#    <input type="submit" id="btn">#}
{#    <button></button>#}
    <input type="button" id="btn" value="提交">
</form>
<!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
<script>
    $('#btn').click(function () {
        $.ajax({
            {#url:'/login/',#}
            url:"{% url 'login' %}",
            type:'post',
            data:{
                csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
                {#csrfmiddlewaretoken:"{{ csrf_token }}",#}
                name:$('#username').val(),
                pwd:$('#password').val(),
            },
            success:function (res) {
                // var resStr = JSON.parse(res)
                if (resStr['code'] == 0){
                    location.href=resStr['redirect_url']
                }else{
                    if(resStr['code'] == 3){
                        var spanEle = document.createElement('span');
                        $(spanEle).text(resStr['warning'])
                        $('form').append(spanEle)
                    }
                }

                console.log(resStr)
            }
        })
    })
</script>
</script>
</body>
```

```python
from django.http import JsonResponse
# 这种回复最方便，直接Json了，也不用导入Json
if name == 'laowang' and password == '123':
    ret = {'code': 0, 'redirect_url': '/index/'}
    # ret = json.dumps(ret)
    return JsonResponse(ret)
    # return HttpResponse(ret, ontent_type='application/json') # 加上这个后在ajax中就不必在进行json解析了
```



## 三、form表单上传文件

```html
{#enctype="multipart/form-data"  必须指定contenttype#}
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    头像：<input type="file" name="headicon">
    用户名：<input type="text" name="name">
    密码：<input type="password" name="pwd">
    <input type="submit">
</form>
```
```python
# views.py
class UploadView(View):

    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        print(request.FILES)  # <MultiValueDict: {'headicon': [<InMemoryUploadedFile: 佩奇.png (image/png)>]}>
        file_obj = request.FILES.get('headicon') # 文件数据需要用request.FILES去拿
        print(file_obj)
        file_name = file_obj.name
        path = os.path.join(settings.BASE_DIR, 'static', 'img', file_name)
        # with open('static/img/'+file_name, 'wb') as f:
        with open(path, 'wb') as f:
            # for i in file_obj:
              #   f.write(i)
      		for chunck in file_obj.chuncks() # 一次返回65536B，可以设置chunck_size的大小
            f.write(chunck)
        return HttpResponse('ok')
```

### 文件的上传 二

```python
views.py

from django.shortcuts import render, HttpResponse
from django.views import View

# 用CBV的模式
class Upload(View):

    def get(self, request):
        return render(request, "Upload.html")

    def post(self, request):
        # 获取文件之前一定要改form表单里面的enctype="multipart/form-data"
        print(request.FILES)  # <MultiValueDict: {'file_name': [<InMemoryUploadedFile: 1.jpg (image/jpeg)>]}>
        # 获取用户上传的文件
        file_path = request.FILES.get("file_name")
        print(file_path, type(file_path))  # 获取得就是文件名1.jpg<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        print(file_path.name, type(file_path.name))  # 1.jpg <class 'str'>
        with open(file_path.name, "wb")as f:  # 因为file_path获得的是一个文件对象，所以要.name一下
            for i in file_path:
                f.write(i)
        return HttpResponse("ok")
```

```html
Upload.html
{# 一定要修改enctype="multipart/form-data,还有不要忘记csrf_token #}
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="file_name" >
    <button>上传</button>
</form>
```

```python
urls.py

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', views.Upload.as_view()),  #不要忘记括号
]
```

file_path.name：上传文件的名字

### form表单注意的点:

1. form标签的属性action 指定提交的地址(不写默认当前地址)，method请求方法(默认为get)
2. input标签要有name属性,有的标签还需要有value
3. 有一个button按钮或者是type="submit"的input标签（只能用submit提交）

```html
<form class="form-signin" action="" method="post" novalidate>#这里如果是method="get"的话，就会改变原url
        <h2 class="form-signin-heading">请输入你的电子邮箱</h2>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input type="email" name="user" id="inputEmail" class="form-control" placeholder="Email address" required="" autofocus="">
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="pwd" id="inputPassword" class="form-control" placeholder="Password" required="">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="remember-me"> 记住我的选择
            </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
    </form>
```

**novalidate:不进行格式验证**

这里如果是method="get"的话，就会改变原url http://127.0.0.1:8000/login/?user=abc&pwd=123 ：会让安全不严谨



目前要提交POST请求的必要操作：

在setings.py中注释一个中间键

```
MIDDLEWARE = [ #中间键
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  注释掉了可以提交POST请求
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```



在urls.py中对数据进行操作(登录成功就返回一个页面，登录失败就返回原来页面)

```python
def login(requests):
    print(requests, type(requests))  # 这里的requests,是一个类
    print(requests.method, type(requests.method))  # 获得它的方法，POST GET
    print(requests.POST, type(requests.POST.get("user")))  # 在POST请求前关掉一个中间键

    #  处理POST请求的逻辑
    if requests.method == "POST":
        #  获取用户提交的用户和密码
        user = requests.POST.get("user")
        pwd = requests.POST.get("pwd")
        #  先设置一个固定的值 (以后会导入数据库)
        if user == "abc" and pwd == "123":
            # 校验成功，返回
            return render(requests, "login2.html")
    # 校验失败
    return render(requests, "login.html")
```



## 四、ajax

### ajax文件上传

```html
Ajax头像：<input type="file" id="file">
Ajax用户名<input type="text" id="uname">
<button id="btn">提交</button>

<!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
<script src="{% static 'js/jquery.js' %}"></script>

<script>
    $('#btn').click(function () {
        var formdata = new FormData();  // 可以携带文件数据
        formdata.append('name', $('#uname').val());
        formdata.append('file_obj', $('#file')[0].files[0]);
        formdata.append('csrfmiddlewaretoken', $('[name=csrfmiddlewaretoken]').val());
        $.ajax({
            url:'/upload',
            type:'post',
            {#data:{#}
            {#    name:$('#uname').val(),#}
            {#    file_obj:$('#file')[0].files[0],#}
            data:formdata,
            processData:false, // 不处理数据
            contentType:false, // 不设置内容类型
            success:function (res) {
                console.log(res)
            }
        })
    })
</script>
```

```python
class UploadView(View):

    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        print(request.FILES)  # <MultiValueDict: {'headicon': [<InMemoryUploadedFile: 佩奇.png (image/png)>]}>
        # file_obj = request.FILES.get('headicon') # 文件数据需要用request.FILES去拿
        file_obj = request.FILES.get('file_obj')  # 文件数据需要用request.FILES去拿
        print(file_obj)
        file_name = file_obj.name
        path = os.path.join(settings.BASE_DIR, 'static', 'img', file_name)
        # with open('static/img/'+file_name, 'wb') as f:
        with open(path, 'wb') as f:
            # for i in file_obj:
            #     f.write(i)
            for chunk in file_obj.chunks():  # 一次饭hi65536B
                f.write(chunk)

        return HttpResponse('ok')
```



### 用ajax完成加法操作

1. urls.py

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^calc/', views.calc),
]
```

2. views.py

```python
def index(request):
    return render(request, "index.html", locals())

def calc(request):
    x1 = request.GET.get("x1")
    x2 = request.GET.get("x2")
    print(x1)
    print(x2)
    time.sleep(3)  # 暂停3秒测试异步
    l3 = int(x1) + int(x2)
    return HttpResponse(l3)  # 在response里面给我返回了计算的结果
```

3. index.html

```html
<body>

    <input type="text" name="l1" >+
    <input type="text" name="l2" >=
    <input type="text" name="l3" >
    <button id="b1">计算</button>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
    $("#b1").click(function () {
        $.ajax({
            url:"/calc/",
            type:"get",
            {#async:false,  把异常改成同步 ajax用它本来就是异常，所以没有必要#}
            data:{
                "x1":$('[name="l1"]').val(),
                "x2":$('[name="l2"]').val(),
            },
            success:function (data) {
                {#把获取到的x1,x2的值传递给l3#}
                $('[name="l3"]').val(data)
            },
        });
    });
</script>
</body>
```



### ajax的接收参数的操作

views.py

```python
import json
from django.http.response import JsonResponse


def text(request):
    print(request.GET)
    xqu = json.loads(request.GET.get("xqu")) #接收ajax参数，把接收的字符串传化为json
    print(xqu, type(xqu))
    return JsonResponse({"status":200,"msg":"ok"})  #给ajax返回信息
```

html

```html
 $("#b3").click(function () {
        $.ajax({
            url:"/text/",
            type:"get",
            data:{	#ajax给函数传递信息
                name: 'aaa',
                age: 15,
                xqu: JSON.stringify(['抽烟','喝酒','烫头']), # 可以直接传递字符串
            },
            success:function (data) {	#接收函数返回的信息
                console.log(data)
                console.log(data.msg)
                console.log(data.status)
            },
        });
    });
```



### 用ajax实现删除

用地址跳转删除的（跳转是要刷新页面的）

html代码

```html
{#实现ajax实现删除功能#}
<button url="{% url 'del' 'publisher' i.pk %}" class="btn btn-danger btn-sm" >删除</button>



ajax
<script>
    $(".btn-danger").click(function () {
        $.ajax({
            url:$(this).attr('url'),
            type:"get",
            success:function (data) {  //接收不能重定向，所以接收的是地址
                //用地址跳转
                location.href  = data
            }
        })
    })
```

views.py

```python
@is_cookies
def delete(request, name, pk):
 	# 代码
    return  HttpResponse(reverse(name))  #返回的字符串
```



不用跳转的删除

html代码

```html
{#实现ajax实现删除功能#}
<button url="{% url 'del' 'publisher' i.pk %}" class="btn btn-danger btn-sm" >删除</button>


ajax
<script>
    $(".btn-danger").click(function () {
        $.ajax({
            url:$(this).attr('url'),
            type:"get",
           success:function (data) {  //接收不能重定向，所以接收的是地址
                //用地址跳转
                {#location.href  = data#}
                if(data.status===200){
                    //后端删除成功，前面删除该行
                    _this.parent().parent().remove()
                }
            }
        })
    })
```

views.py

```python
@is_cookies
def delete(request, name, pk):
 	# 代码
    return JsonResponse({"status":200})  #返回一个字典，让ajax提取如果是200的话，就删除本页面的th标签
```





### sweetalert的使用(弹窗效果)

给ajax删除，添加的sweetalert弹窗效果

1. 导入script

```js
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
```

2. 编写js文件

```js
<script>
    $(".btn-danger").click(function () {
        swal({
            title: "确实删除数据?",
            text: "删除后无法恢复数据!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {
                    var _this = $(this)
                    $.ajax({
                        url: $(this).attr('url'),
                        type: "get",
                        success: function (data) { //接收不能重定向，所以接收的是地址
                            //用地址跳转
                            {#location.href  = data#}
                            if (data.status === 200) {
                                //后端删除成功，前面删除该行
                                _this.parent().parent().remove()
                                swal("数据删除成功!", {
                                    icon: "success",
                                });
                            } else {
                                swal("数据删除成功!", {
                                    icon: "error",
                                });
                            }
                        }
                    })
                } else {
                    swal("数据删除失败!");
                }
            });
    })
</script>
```



更多样式弹窗样式的网站：https://sweetalert.js.org/guides/

AJAX资料网：https://www.cnblogs.com/maple-shaw/articles/9524153.html



## 五、JSON

轻量级的文本数据交换格式

python

支持的数据类型

​	字符串	数据	布尔	列表	字典	None

序列化

​	python的数据类型 --> json字符串

反序列话

​	json字符串 --> python的数据类型



### 给视图函数添加csrf校验

方法一：

```python
from  django.views.decorators.csrf import  csrf_exempt,csrf_protect

@csrf_exempt  加在视图上  该视图不需要进行csrf校验
@csrf_protect 加在视图上  该视图需要进行csrf校验
@ensure_csrf_cookie 加在视图上 确保返回时设置csrftoken的cookie
```

csrf的校验原理

```
从cookie中获取csrftoken的值
从request.POST中获取csrfmiddlewaretoken的值或者从请求头中获取x-csrftoken的值
把这两个值对比，对比成功就接受请求，反之拒绝
```

让ajax可以通过django的csrf的校验：

### 给html的ajax添加csrf校验

方法二：

1. 直接给ajax中的data添加csrfmiddlewaretoken的键值对

```html
 data:{
   csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken]').val(),
   name: 'aaa',
   age: 15,
   xqu: JSON.stringify(['抽烟','喝酒','烫头']),
},
```

前提：必须有csrftoken的cookie的

- 使用{% csrf_token%}

- 使用ensure_csrf_cookie的装饰器，加在视图上 

  ​	from django.views.decorators.csrf import ensure_csrf_cookie

  

   	2. 给header添加x-csrftoken的键值对(导入文件的方式）

```python
1.把header添加到ajax中
 $.ajax({
            url:"/calc2/",
            type:"post",
            headers: {"X-CSRFToken": $('[name="csrfmiddlewaretoken]').val()},  // 从Cookie取csrftoken，并设置到请求头中
            {#async:false,把异常改成同步 ajax用它本来就是异常，所以没有必要#}
            data:{
                "x1":$('[name="l11"]').val(),
                "x2":$('[name="l22"]').val(),
            },
            

2。设置static的js文件，先在settings.py中写入STATICFILES_DIRS[os.path.join(BASE_DIR,'static')]
在写入js文件

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});


3.在html中写入 {% csrf_token %}
	{% csrf_token %}
	
4. 在视图函数中对应位置，添加装饰器
from  django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def calc2(request):
	pass
```



最终推荐：导入文件+确保有cookie(最后面这种)

资料：https://www.cnblogs.com/maple-shaw/articles/9524153.html



## 时间日期类型不可json问题

```python
import json
from datetime import datetime
from datetime import date

#对含有日期格式数据的json数据进行转换
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,field)


d1 = datetime.now()

dd = json.dumps(d1,cls=JsonCustomEncoder)
print(dd)
```

