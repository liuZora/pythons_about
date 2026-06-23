## 一、Form

参考：https://www.cnblogs.com/clschao/articles/10486468.html

### Form自动生成登录标签并校验



```python
# views.py
class LoginForm(forms.Form):

    name = forms.CharField(
        label='用户名：',
        initial='小李',
        max_length=16,
        min_length=6,
        widget=forms.widgets.TextInput(attrs={'class':'form-control'}),  # 密码输入不可见，括号里边加样式
    )

    password = forms.CharField(
        label='密码：',
        widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}),  # 密码输入不可见，括号里边加样式
    )

    sex = forms.ChoiceField(
        label='性别',
        choices=((1,"男"), (2, "女"), (3, "其他")),
        widget=forms.widgets.RadioSelect(),
        initial=3,
    )

    city = forms.ChoiceField(
        label='城市',
        choices=((1,"北京"), (2, "上海"), (3, "东莞")),
        widget=forms.widgets.Select(),  # 下拉框
        initial=3,
    )

    hobby = forms.ChoiceField(
        label='爱好',
        choices=((1,"抽烟"), (2, "喝酒"), (3, "烫头")),
        widget=forms.widgets.CheckboxSelectMultiple,  # 多选框， SelectMultiple多选下拉框
        initial=3,
    )

    birthday = forms.CharField(
        label='生日',
        widget=forms.widgets.TextInput(attrs={'type':'date'}),
    )
    
def register(request):
    form_obj = LoginForm()
    if request.method == 'GET':
        return render(request, 'register.html',{'form_obj':form_obj})
    else:
        username = request.POST.get('name')
        password = request.POST.get('password')
        print(username, password)
        return HttpResponse('登录成功')
```

```html
# register.html
<form action="" method="post">
    {% csrf_token %}
{#    用户名：<input type="text" name="username">#}
{#    密码：<input type="password" name="password">#}
    <div>
        <label for="">{{ form_obj.name.label }}</label>
        {{ form_obj.name }}
    </div>
    <div>
        <label for="">{{ form_obj.password.label }}</label>
        {{ form_obj.password }}
    </div>
    <div>
        <label>{{ form_obj.sex.label }}</label>
        {{ form_obj.sex }}
    </div>
    <div>
        <label>{{ form_obj.city.label }}</label>
        {{ form_obj.city }}
    </div>
    <div>
        <label>{{ form_obj.hobby.label }}</label>
        {{ form_obj.hobby }}
    </div>
    <div>
        <label>{{ form_obj.birthday.label }}</label>
        {{ form_obj.birthday }}
    </div>
{#    {{ form_obj.as_p }}#}
    <input type="submit">
</form>
```

### 其他属性

```python
class LoginForm(forms.Form):

    name = forms.CharField(
        required=False,
        label='用户名：',
        initial='小李',
        max_length=16,
        min_length=6,
        error_messages={'requried':'不能为空','min_length':'不能太短'},
        widget=forms.widgets.TextInput(attrs={'class':'form-control'}),  # 密码输入不可见，括号里边加样式
    )
    
def register(request):
    form_obj = LoginForm()
    if request.method == 'GET':
        return render(request, 'register.html',{'form_obj':form_obj})
    else:
        # username = request.POST.get('name')
        # password = request.POST.get('password')
        # print(username, password)
        # request.POST = name:"ssss"
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():  # 做校验
            print(form_obj.cleaned_data)  # 通过的校验数据
        else:
            print(form_obj.errors)
            return render(request, 'register.html', {'form_obj':form_obj})

        return HttpResponse('登录成功')
```

```html
{##novalidate 关闭浏览器校验#}
<form action="" method="post" novalidate>
    {% csrf_token %}
{#    用户名：<input type="text" name="username">#}
{#    密码：<input type="password" name="password">#}
    <div>
        <label for="">{{ form_obj.name.label }}</label>
        {{ form_obj.name }}
{#        # 不取列表，只取一个#}
        {{ form_obj.name.errors.0 }}
    </div>
    <input type="submit">
</form>
```

### 校验器组件

```python
import re
from django.core.exceptions import ValidationError
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误

class LoginForm(forms.Form):

    name = forms.CharField(
        required=False,
        label='用户名：',
        initial='小李',
        max_length=16,
        min_length=6,
        error_messages={'requried':'不能为空','min_length':'不能太短'},
        # validators=[RegexValidator(r'^金瓶梅','没看过金瓶梅不能通过'),],
        validators=[mobile_validate, ],
        widget=forms.widgets.TextInput(attrs={'class':'form-control'}),  # 密码输入不可见，括号里边加样式
    )
```

### Hook钩子方法

在Form类中定义钩子函数，来实现自定义的验证功能。

源码分析：https://www.bilibili.com/video/BV1aJ411H7Ej?p=405

#### 局部钩子和全局钩子

```python
import re
from django.core.exceptions import ValidationError
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误

class LoginForm(forms.Form):

    name = forms.CharField(
        required=False,
        label='用户名：',
        initial='小李',
        max_length=16,
        min_length=6,
        error_messages={'requried':'不能为空','min_length':'不能太短'},
        validators=[RegexValidator(r'^金瓶梅','没看过金瓶梅不能通过'),],
        # validators=[mobile_validate, ],
        widget=forms.widgets.TextInput(attrs={'class':'form-control'}),  # 密码输入不可见，括号里边加样式
    )
    # 局部钩子
    def clean_name(self):
        value = self.cleaned_data['name']
        if '小李' in value:
            raise ValidationError('含有敏感词汇：小李')
        else:
            return value
    # 全局钩子
    def clean(self):
        value = self.cleaned_data

        p1 = value['password']
        p2 = value['r_password']
        if p1 == p2:
            return value
        else:
            # raise ValidationError('两次输入的密码不一致')
            self.add_error('r_password','两次输入的密码不一致')
            raise ValidationError('两次输入的密码不一致')
```

```html
<form action="" method="post" novalidate>
    {% csrf_token %}
{#    用户名：<input type="text" name="username">#}
{#    密码：<input type="password" name="password">#}
    <div>
        <label for="">{{ form_obj.name.label }}</label>
        {{ form_obj.name }}
{#        # 不取列表，只取一个#}
        {{ form_obj.name.errors.0 }}
    </div>
    <div>
        <label for="">{{ form_obj.password.label }}</label>
        {{ form_obj.password }}
    </div>
    <div>
        <label for="">{{ form_obj.r_password.label }}</label>
        {{ form_obj.r_password }}
    </div>
    
# html
<body>
<div class="container">
    <h1>student</h1>
    <form method="POST" novalidate>
        {% csrf_token %}
        {# {{ student_list.as_p }}#}
        {% for student in student_list %}
            <div class="form-group col-md-6">
                {# 拿到数据字段的verbose_name,没有就默认显示字段名 #}
                <label class="col-md-3 control-label">{{ student.label }}</label>
                <div class="col-md-9" style="position: relative;">{{ student }}</div>
            </div>
        {% endfor %}
        <div class="col-md-2 col-md-offset-10">
            <input type="submit" value="提交" class="btn-primary">
        </div>
    </form>
</div>
</body>
```



### form组件的使用

自动生成input标签：

form组件的定义：

```python
from django import forms

class ReForm(forms.Form):
    user = forms.CharField(label="姓名", min_length=6)  # 最小长度是6位，(默认添加了一个判断字段是否为空)
    pwd = forms.CharField(label="密码")

```

使用：

```python
def reg2(request):
    reform = ReForm()  # 一个空的form
    if request.method == "POST":
        # 对提交的数据进行校验
        reform = ReForm(request.POST)  # 包含用户提交数据的form(POST请求获取的数据)
        if reform.is_valid():  # 对数据进行校验，有数据返回True,否则 False
            # 校验成功
            return HttpResponse("成功")
    return render(request, "reg2.html", locals()) # 如果没有数据，返回错误信息那些
```

模板：

```html
<form action="" method="post">
    {% csrf_token%}
    {{ reform }}	{# 一次性生成所有的input框#}
    
      <p>
        <label for="{{ reform.user.id_for_label }}" >{{ reform.user.label }}</label>
        {{ reform.user }}
        <span style="color: red;" >{{ reform.user.errors }}</span>
    </p>
    <p>
        <label for="{{ reform.pwd.id_for_label }}">{{ reform.pwd.label }}</label>
        {{ reform.pwd }}
        <span style="color: red;">{{ reform.pwd.errors }}</span>
    </p>
    
    <button>注册</button>
</form>


拿form组件定义里面的内容：
 {{ reform.user }}  该字段的Input框
 {{ reform.user.label }}  该字段提示的信息
 {{ reform.user.id_for_label }}	 该字段input的框的id (就是一个文本框)
 {{ reform.user.errors }}  该字段的所有错误
 {{ reform.user.errors.0 }}  该字段的第一个错误
 {{ reform。errors }}  所有字段的错误
```



#### 常用字段

```
CharField  文本输入框
ChoiceField	 单选 默认是select
MultipleChoiceField  多选 默认是select
```

#### 字段参数

```
initial="张三"	默认值
error_messages	 自定义错误信息
widget    修改类型 修改input框的类型
required	是否必填
disablead	是否禁用
validators=[定义的函数]   校验器
```



在使用选择标签时，需要注意choices的选项可以从数据库中获取，但是由于是静态字段 ***获取的值无法实时更新***，那么需要自定义构造方法从而达到此目的。

其实就是数据里面定义相关的参数，然后form获取里面的参数，呈现给html

1. 定义models.py

```python
from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
```

2. 在views.py操作

```python
from django import forms
from app01 import models
from django.forms import models as form_model

class ReForm(forms.Form):
    hobby = form_model.ModelMultipleChoiceField(queryset=models.Hobby.objects.all(),widget=forms.CheckboxSelectMultiple) #所有的对象列表
```

3. html

```html
    <p>
        <label for="{{ reform.hobby.id_for_label }}">{{ reform.hobby.label }}</label>
        {{ reform.hobby }}
        <span style="color: red;">{{ reform.hobby.errors }}</span>
    </p>
```



### 校验

校验器：

​	1.定义函数

```python
def check_name(value):  # 用户输入文本框的值
    # 校验不符合
    if "abc" in value:
        raise ValidationError("不让用abc")
    # 符合校验不做任何操作

class ReForm(forms.Form):
    user = forms.CharField(label="姓名",
                           validators=[check_name], #其它字段要用的话也是加这个
                           )
```

2. 使用内置的校验器

```python
from django.core.exceptions import ValidationError
# 内置校验器
phone = forms.CharField(validators=[RegexValidator(r'^1[3-9]\d[9]','手机号模式不正确')])
```



#### 钩子函数

1. 局部钩子

clean是固定的,_号后面的user，是选择装饰钩子的字段

self.cleaned_data.get("user")：获取user框中用户输入的内容

self.cleaned_data：获取全部数据

```python
 # 局部钩子函数
    def clean_user(self):
        # 不符合校验规则 抛出异常
        value = self.cleaned_data.get("user")  # 获取user框中用户输入的内容
        if "adc" in value:
            raise ValidationError("adc名字-.-，你懂吗？")
        # 符合校验规则  返回该字段的值
        return value
```

​	2.全局钩子

elf.add_error("pwd","one"): 将错误信息加入某个字段中，并返回错误信息

```python
# 全局钩子
def clean(self):
    pwd = self.cleaned_data.get("pwd") # 获取输入的内容
    re_pwd = self.cleaned_data.get("re_pwd")
    if pwd != re_pwd:
        #不符合校验规则，则抛出异常
        #将错误信息加入到某个字段中
        self.add_error("pwd","one")
        self.add_error("re_pwd","输入有误")
        raise ValidationError("再次密码不一样")
    return self.changed_data # 返回全部数据
```



### is_valid()流程：

1. 执行一个full_clean方法
   1. 定义一个错误字典和cleaned_data={} # 存在已经经过校验的数据的字典
   2. 执行self._clean_fields()
      1. 循环所有的字段
      2. 对一个字段进行内置的校验，校验器的校验，局部钩子的校验
      3. 校验不通过，错误字典中有该字段的错误信息
      4. 所有校验通过，self.cleaned_data有该字段的值 
   3. 执行全局钩子

form更多操作：https://www.cnblogs.com/maple-shaw/articles/9537309.html



## 二、Modelform

modelform会自动生成你的model类（表）对应的字段的Form类

```PYTHON
# models.py
class Book(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publish=models.ForeignKey(to="Publish",to_field="nid")
    authors=models.ManyToManyField(to='Author',)
    def __str__(self):
       return self.title
       
# views.py
class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = "__all__"
        labels = {
            "title": "书名",
            "price": "价格"
        }
        widgets = {
            "password": forms.widgets.PasswordInput(attrs={"class": "c1"}),
            "publishDate": forms.widgets.DateInput(attrs={"type": "date"}),
        }
    #局部钩子：
    def clean_title(self):
        pass
　　#全局钩子
    def clean(self):
        pass
    def __init__(self,*args,**kwargs): #批量操作
        super().__init__(*args,**kwargs)
        for field in self.fields:
            #field.error_messages = {'required':'不能为空'} #批量添加错误信息,这是都一样的错误，不一样的还是要单独写。
            self.fields[field].widget.attrs.update({'class':'form-control'})
```

### class meta**常用参数**

```PYTHON
model = models.Book  # 对应的Model中的类
fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
exclude = None  # 排除的字段
labels = None  # 提示信息
help_texts = None  # 帮助提示信息
widgets = None  # 自定义插件
error_messages = None  # 自定义错误信息
error_messages = {
    'title':{'required':'不能为空',...} #每个字段的所有的错误都可以写，...是省略的意思，复制黏贴我代码的时候别忘了删了...
}
```



## 三、同源和跨域

详细：https://www.cnblogs.com/clschao/articles/10745966.html

深入理解python异步编程

同源策略（Same origin policy）是一种约定，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，则浏览器的正常功能可能都会受到影响。可以说Web是构建在同源策略基础之上的，浏览器只是针对同源策略的一种实现。


### 简单请求跨域

创建两个django项目，第一个叫做s1，一个叫做s2，s1用8000端口启动，s2用8001端口启动

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h2>s1的首页</h2>
<button id="btn">Ajax请求</button>


<script src="https://cdn.bootcss.com/jquery/3.4.0/jquery.js"></script>
<script>
    $('#btn').click(function () {
        $.ajax({
            //url:'/books/', 访问自己服务器的路由，同源(ip地址、协议、端口都相同才是同源)
            url:'http://127.0.0.1:8001/books/', //访问其他服务器的路由，不同源,那么你可以访问到另外一个服务器，但是浏览器将响应内容给拦截了，并给你不同源的错误：Access to XMLHttpRequest at 'http://127.0.0.1:8001/books/' from origin 'http://127.0.0.1:8000' has been blocked by CORS policy: The 'Access-Control-Allow-Origin' header has a value 'http://127.0.0.1:8002' that is not equal to the supplied origin.
            #并且注意ip地址和端口后面是一个斜杠，如果s2的这个url没有^books的^符号，那么可以写两个//。　　　　　　  type:'get',
            success:function (response) {
                console.log(response);
            }

        })
    })


</script>
</body>
</html>
```

```python
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def books(request):

    # return JsonResponse(['西游记','三国演义','水浒传'],safe=False)
    obj = JsonResponse(['西游记','三国演义','水浒传'],safe=False)
    return obj
    
    
# s2
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def books(request):

    # return JsonResponse(['西游记2','三国演义2','水浒传2'],safe=False)

    obj = JsonResponse(['西游记2','三国演义2','水浒传2'],safe=False)
    #下面这个响应头信息是告诉浏览器，不要拦着，我就给它，"*"的意思是谁来请求我，我都给
    # obj["Access-Control-Allow-Origin"] = "*"
    obj["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000" #只有这个ip和端口来的请求，我才给他数据，其他你浏览器帮我拦着
    return obj
```

