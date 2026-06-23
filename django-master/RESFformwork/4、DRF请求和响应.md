# DRF请求和响应

**目录：**

- DRF请求和响应介绍
- 装饰器视图 @api_view(['GET','POST'])
- 类视图：APIView

## 一、介绍

**请求和响应：**

　　目前我们用的都是Django 里面的 request、也是Django 里面的 response，状态也是django里面的。但是 DRF里面的 request是基于 django 里面的 request 进行的封装。

**请求(request)：**

　　REST里面有个HttpRequest特别相似的对象叫request，主要获取前端传递过来的数据，获取数据的方法就是request.data

**响应(`Response`)：**

　　REST里面有个HttpResponse特别相似的对象叫Response,主要用来给前端传递数据，传递数据的方法就是Response(data)

**状态码(status)：**

　　REST里面的状态码比较人性化。每个状态都用意思去表示。比如：

```
HTTP_200_OK = 200 #OK
HTTP_201_CREATED = 201 #创建成功
HTTP_403_FORBIDDEN = 403 # 权限拒绝
'''
'''
```

**API视图：**

　　API视图主要为了咱们RESTFUL风格的API。主要用来包装request,response、现在api请求方法。

- 基于函数视图的`@api_view(['GET','POST'])`装饰器
- 基于类视图的`APIView`类



## 二、装饰器视图 @api_view(['GET','POST'])

我们根据 DRF 提供我们的 api_view、Response、status、request 来重写我们的视图函数

```python
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response  #提供drf的响应
from rest_framework import status  #提供DRF状态码
 
 
@api_view(['GET', 'POST'])  #首先告诉它支持哪些方法,而且装饰之后不需要crf_token验证，因为api_view已经帮我们做了验证
def user_list(request): #用了api_view装饰器之后，这边的request就已经是DFR的request了。
    if request.method == "GET":
        arts = User.objects.all()
        ser = UserSerializer(instance=arts, many=True, context={'request': request})
        return Response(ser.data, status=status.HTTP_200_OK)  #直接把序列化数据很状态码传入进去
    elif request.method == "POST":
        #获取入参直接是 request.data 即可获取
        ser = UserSerializer(data=request.data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return JSONResponse(ser.errors, status=status.HTTP_401_UNAUTHORIZED)
```

知识点说明：

```python
@api_view(['GET', 'POST'])：
    1.告诉它需要支持哪些方法：这边支持POST和GET
    2.装饰完api_view,不在需要crf_token验证了，因为api_view已经帮你封装好了
    3.用了api_view装饰器之后，request就已经是DRF的request了，不再是 django的 request了 => 调用直接 request.data
 
drf的响应：from rest_framework.response import Response => Response(data，status=status.HTTP_201_CREATED)
  
提供DRF状态码：from rest_framework import status  => status.HTTP_201_CREATED
```



## 三、类视图：APIView

我们还有一种方法，可以通过 类视图：APIView，功能跟我们的 @api_view 一样，只不过采用的是CBV的方式

```python
class UserDetail(APIView): #采用类视图，定义 get、patch、put和delete
 
    def get_object(self, id):  # 判断是否
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist as e:
            return Http404
 
    def get(self,request, *args, **kwargs):
        user = self.get_object(kwargs.get('id'))   #根据传值 **kwargs获取id的值
        ser = UserSerializer(instance=user,context={"request": request})
        return Response(ser.data, status=status.HTTP_200_OK)
 
    def put(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('id'))
        ser = UserSerializer(instance=user,data=request.data, context={"request": request})  #request是drf的了，所以获取数据request.data
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('id'))
        ser = UserSerializer(instance=user, data=request.data, context={"request": request},partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('id'))
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

说明：因为我们是采用CBV的方式，所以路由的方式要改变

```python
from django.urls import path
from app03 import views
 
 
urlpatterns = [
    path("user/", views.user_list, name="user-list"),  #FBV的方式
    path("user/<int:id>/", views.UserDetail.as_view(), name="user-detail")  #cbv方式 => views.UserDetail.as_view()
]
```

保存的时候把不属于的字段去掉

```python
    def validate(self, attrs): #组合验证
        if attrs.get('pwd1') != attrs.get('pwd'):
            raise serializers.ValidationError("两次密码不一样")
        if "pwd1" in attrs:  #这边需要加一个验证，当我通过patch传进来的时候，没有pwd1的参数，则我不删除
            attrs.pop('pwd1')
        return attrs
```



## 四、DRF中的响应和请求Request 与 Response

### 4.1 Request

REST framework 传入视图的request对象不再是Django默认的HttpRequest对象，而是REST framework提供的扩展了HttpRequest类的**Request**类的对象。

REST framework 提供了**Parser**解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）将请求数据进行parse解析，解析为类字典对象保存到**Request**对象中。

**Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果。**

无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。

### 常用属性

#### 1）.data

`request.data` 返回解析之后的请求体数据。类似于Django中标准的`request.POST`和 `request.FILES`属性，但提供如下特性：

- 包含了解析之后的文件和非文件数据
- 包含了对POST、PUT、PATCH请求方式解析后的数据
- 利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON数据

#### 2）.query_params

`request.query_params`与Django标准的`request.GET`相同，只是更换了更正确的名称而已。

### 4.2 Response

```
rest_framework.response.Response
```

REST framework提供了一个响应类`Response`，使用该类构造响应对象时，响应的具体数据内容会被转换（render渲染）成符合前端需求的类型。

REST framework提供了`Renderer` 渲染器，用来根据请求头中的`Accept`（接收数据类型声明）来自动转换响应数据到对应格式。如果前端请求中未进行Accept声明，则会采用默认方式处理响应数据，我们可以通过配置来修改默认响应格式。

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    )
}
```

### 构造方式

```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

`data`数据不要是render处理之后的数据，只需传递python的内建类型数据即可，REST framework会使用`renderer`渲染器处理`data`。

`data`不能是复杂结构的数据，如Django的模型类对象，对于这样的数据我们可以使用`Serializer`序列化器序列化处理后（转为了Python字典类型）再传递给`data`参数。

参数说明：

- `data`: 为响应准备的序列化处理后的数据；
- `status`: 状态码，默认200；
- `template_name`: 模板名称，如果使用`HTMLRenderer` 时需指明；
- `headers`: 用于存放响应头信息的字典；
- `content_type`: 响应数据的Content-Type，通常此参数无需传递，REST framework会根据前端所需类型数据来设置该参数。

#### 常用属性：

##### 1）.data

传给response对象的序列化后，但尚未render处理的数据

##### 2）.status_code

状态码的数字

##### 3）.content

经过render处理后的响应数据

### 4.3 状态码

为了方便设置状态码，REST framewrok在`rest_framework.status`模块中提供了常用状态码常量。

```
##### 1）信息告知 - 1xx

##### 2）成功 - 2xx

##### 3）重定向 - 3xx

##### 4）客户端错误 - 4xx

##### 5）服务器错误 - 5xx
```

