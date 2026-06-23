# 一、前后端分离介绍

```
详细地址：https://www.cnblogs.com/zhangqigao/p/12750612.html
```

## 1.1 前后端分离优缺点

（1）为什么要前后端分离（优点）：

- PC、APP、PAD多端适应
- SPA开发模式开始流行
- 前后端开发职责不清
- 开发效率问题，前后端互相等待
- 前端一直配合着后端，能力受限
- 后台开发语言和模板高度耦合，导致开发语言依赖严重

（2）前后端分离缺点

- 前后端学习门槛增加
- 数据依赖导致文档重要性增加
- 前端工作量加大
- SEO搜索引擎优化的难度增大
- 后端开发模式迁移增加成本



# 二、restful API设计规范

## 2.1 resTful API基本介绍

```
一句话：RESTful API是目前前后端分离的最佳实践，它是一套标准，一个规范，而不是一个框架。
```

标准对于开发者来说是十分重要的，就像HTTP、HTML这些都是标准。

在前后端分离的时候，我们会设计API，如果我们在设计的时候依据RESTful准则，那么这套API这可以称作RESTful API。

- 1. RESTful API轻量，直接通过http或者https，不需要额外的协议，一般有四种常用操作post/get/put/delete。
- 2. RESTful API面向资源，一目了然，具有自解释性。
- 3. RESTful API数据的描述十分简单，基于Json或XML的数据格式进行数据传输。

总结什么是RESTful架构：

- （1）每一个URI代表一种资源；
- （2）客户端和服务器之间，传递这种资源的某种表现层；
-   (3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。

## 2.2 restful API设计指南

```
参考资料：http://www.ruanyifeng.com/blog/2014/05/restful_api.html
```

### 1、协议

API与用户的通信协议，总是使用[HTTPs协议](https://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)

推荐使用 HTTPS.安全

### 2、域名

应该尽量将API部署在专用域名之下

```
https://api.example.com
```

如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。

```
https：//example.org/api/
```

### 3、版本

应该将API的版本号放入URL

```
http://www.example.com/app/1.0/apples
http://www.example.com/app/1.1/apples
http://www.example.com/app/2.0/apples
```

另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。[Github](https://developer.github.com/v3/media/#request-specific-version)采用这种做法.

### 4、路径

路径又称"终点"（endpoint），表示API的具体网址

```
GET /products ：将返回所有产品清单
POST /products ：将产品新建到集合
GET /products/4 ：将获取产品4
PATCH /products/4 将更新产品4（部分属性更新）
PUT /products/4：将更新产品4 （全部属性更新）
```

对数据的操作增删改查 即：

```
create：增
read： 查
update： 改
delete： 删
```

 所以：

```
GET: 获取资源
POST：新增资源
PUT： 更新资源(全部更新) => {"id":1,"name":'帅高高'，"age":13}
PATCH: 部分更新 => {"id":1,"age":13} => 选择性的更新DELETE: 删除资源
```

### 5、HTTP动词

```
| 请求方法 | 请求地址    | 后端操作                     |
| -------- | ----------- | --------------------------|
| GET      | /students   | 获取所有学生                |
| POST     | /students   | 增加学生                   |
| GET      | /students/1 | 获取编号为1的学生           |
| PUT      | /students/1 | 更新编号为1的学生（全部属性） |
| DELETE   | /students/1 | 删除编号为1的学生        　　|
| PATCH    | /students/1 | 更新编号为1的学生（部分属性） |
```

### 6、过滤信息

如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

```
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?animal_type_id=1：指定筛选条件
```

### 7、状态码

服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）。

> - 200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
> - 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
> - 202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
> - 204 NO CONTENT - [DELETE]：用户删除数据成功。
> - 400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
> - 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
> - 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
> - 404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
> - 406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
> - 410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
> - 422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
> - 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

状态码的完全列表参见[这里](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)。

### **8、错误处理**

```js
{
	error:"Invalid API key"
}

#移动端格式
{
	'code':1,
	'msg':xxxx,
	"data":{}
}
```

### **9、返回结果**

针对不同操作，服务器向用户返回的结果应该符合以下规范。

REST framework返回的数据都是JSON格式的

```
GET /collection：返回资源对象的列表（数组）
GET /collection/resource：返回单个资源对象
POST /collection：返回新生成的资源对象
PUT /collection/resource：返回完整的资源对象
PATCH /collection/resource：返回完整的资源对象
DELETE /collection/resource：返回一个空文档
```

### 10、返回结构中提供链接

```
"link": {
  "rel":   "collection https://www.example.com/zoos",
  "href":  "https://api.example.com/zoos",
  "title": "List of zoos",
  "type":  "application/vnd.yourformat+json"
}
```

