#### 一、Web基础了解

1. ##### HTTP协议

   - HTTP是一个客户端终端（用户）和服务器端（网站）请求和应答的标准（TCP)

2. ##### 状态码

   -  1xx 提示信息接受了请求需要进一步的处理
   -  2xx 成功的提示 接受了请求，正常处理了
   -  3xx 重定向 接受了请求，要处理请求的话，需要再次访问另外的一个地址
   -  4xx 请求方面的错误 404 403
   -  5xx 服务器的错误

3. ##### 请求和相应的流程

   + 浏览器发送请求
   + 服务器接受请求，进一步的去处理，根据路径找到函数，执行函数处理逻辑，返回相应的内容
   + 内容按照HTTP协议的响应式返回

4. ##### 访求方法

   ​	8种：get,post,head,options,trace,connect,delete,put

5. ##### URL

   https:端口是443 http：端口是80

   ​     ![image-20200802122144061](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200802122144061.png)

6. ##### 请求，响应

   ​	  请求：浏览器给服务器发送的数据 request

   ​           格式：

   ​              “请求方法 路径 HTTP/1.1

   ​              K1=v1

   ​              K2=v2

   ​              请求体”-> get请求没有请求体

   ​       响应：服务器返回给浏览器的数据 response

   ​           “HTTP/1.1 状态码 状态描述

   ​           K1=v1

   ​           K2=v2

   ​           响应体(响应数据 )

   7. **模型**

      ```
      TCP/IP 5层模型:应用层，传输层，网络层，数据链路层，物理层
      
      osi七层模型
      
      socket：套接字 位于应用层和传输层之间的一个虚拟层，一个接口
      
       
      
      C/S架构(如QQ软件)               B/S架构(如浏览器)
      ```

   8. **服务端客服端连接方式**

      ```
      百度服务器  socket服务端
      
      1．Socket服务端
      
      2．绑定IP和端口
      
      3．监听
      
      4．等待连接
      
      5．接受连接
      
      6．接受数据
      
      7. 返回数据
      
      8. 断开连接
      
      浏览器 socket客户端
      
      5.socket客户端
      
      6.连接上百度的socket服务端
      
      7.发送数据
      
      8.接受数据
      
      9.断开连接
      ```

      **`Web框架的原理：https://www.cnblogs.com/maple-shaw/p/8862330.html`**

    [https://www.bootcss.com/](前端开发框架):前端开发css框架网站
   
   [http://www.jq22.com/]():html模板网站



快捷键(Chrome的):

- Ctrl+U:查看网页源代码

- Ctrl+S:直接下载当前网页的所有图片,css,js

Pycharm:

- Ctrl+R:替换

- Ctrl+f :查找 