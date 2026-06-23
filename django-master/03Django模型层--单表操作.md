## 一、ORM简介

```
对象关系映射（Object Relational Mapping，简称ORM）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术。

简单的说，ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中。

ORM在业务逻辑层和数据库层之间充当了桥梁的作用。
```

对应关系：

- 类   -->  表

- 对象  -->  数据行(记录)

- 属性  -->  字段

### 使用ORM

1. 在settings中配置数据库的连接sql:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }
   ```

2. 在app下的models.py中写类:

   ```python
   class User(models.Model):  # 继承models.Model
       username = models.CharField(max_length=32)  # varchar(32)
       password = models.CharField(max_length=32)  # varchar(32)
       #在templates文件中就生成了一个db.sqlite3
   ```

   - 然后点击最右边的database   

   - 双击文件db.sqlite3 ![image-20200806085206537](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806085206537.png)

     - 点击设置![image-20200806085303026](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806085303026.png)    

   - 第一次要下载插件，直接download  --> 下载完后![image-20200806085618232](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806085618232.png)

     

3. 数据库迁移的命令 (在Teminal下输入下面的命令)

   ```python
   python manage.py makemigrations  #检测所有app下的models。py文件有什么变化,将变更记录制作成迁移文件
   python manage.py migrate  # 数据库的迁移 将变更的记录同步到数据库
   ```

   ![image-20200806085936230](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806085936230.png)- 

- 刷新以后就![image-20200806090053016](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806090053016.png)

- 然后双击app01_user，添加数据，添加完后点击DB哪里保存![image-20200806090505955](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806090505955.png)



**在settings.py中加上这句话，可以在控制台看到翻译后的sql语句**

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```

　




### ORM测试

```python
 from app01 import models
    res = models.User.objects.all() #获取表中所有的数据
    for i in res:
        '''
        User object abc 123 <class 'str'>
        User object cba 123 <class 'str'>
        '''
        print(i,i.username,i.password,type(i.username))
        
    ret = models.User.objects.get(username="abc",password="123") #获取一条数据  User object
    # ret1 = models.User.objects.get(password="123") # 获取一条数据(获得不到，或者获得多条数据，就会报错)
        
    ret = models.User.objects.filter(password="123") #获取多条数据 ，返回一个列表，如果获取不到返回一个空的列表
    print(ret[0].username,ret[1].username,ret) #abc cba <QuerySet [<User: User object>, <User: User object>]>
```



### 使用mysql数据库的流程:

1. 创建一个mysql数据库

   ```
   create database login;
   ```

   

2. 配置settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'login',  # 数据库名称
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'mysql',
    }
}
```

3. 使用pymysql的模块连接mysql数据库

   习惯的写到与项目同名的文件夹下的’__init__.py‘中

   ```
   import pymysql
   pymysql.install_as_MySQLdb()
   ```

   

4. 在app下的models.py写入类

   ```
   class User(models.Model):  #User表名 继承models.Model
       username = models.CharField(max_length=32)  # varchar(32)
       password = models.CharField(max_length=32)  # varchar(32)
   ```

5. 执行数据库迁移的命令

   ```
   python manage.py makemigrations  #检测所有app下的models。py文件有什么变化,将变更记录制作成迁移文件
   python manage.py migrate  # 数据库的迁移 将变更的记录同步到数据库
   ```

   我们生成文件成功后：就点击右边的Datebases ---> 在点击左上角的+号 ----- 选择Data Source --->在选择MYSQL进行设置----》![image-20200806120059381](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200806120059381.png)

   ---》最后在 test Connection测试一下连接，

   如果报错这个就是没有在mysql里面设置时区:**Server returns invalid timezone. Go to 'Advanced' tab and set 'serverTimezone' property manually.**

   只需要输入二条命令：show variables like'%time_zone';  

    set global time_zone = '+8:00';

   或者：

   在Advanced中的 --> serverTimezone设置哦Hongkong



## 二、Model

### Model常用的字段

```python
AutoField	自增字段 primary_key=True 变成主键。
IntegerField	整形 10位 -2147483648 ~ 2147483647。
CharField	字符串 varchar max_length（长度） 必填参数
DateField	日期类型，日期格式为YYYY-MM-DD(年-月-日)
DatetimeField	日期时间字段，格式为YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] (年-月-日-时-分-秒)
    #auto_now：每次修改时修改为当前日期时间。
    #auto_now_add：新创建对象时自动添加当前日期时间。
    #auto_now和auto_now_add和default参数是互斥的，不能同时设置。
BooleanFiled	布尔类型
TextField	大文本
FloatField	浮点型
DecimalField	10进制小数
		 #max_digits，小数总长度
         #decimal_places，小数位长度	

# 更多参数：https://www.cnblogs.com/maple-shaw/articles/9323320.html
```

**实例**

```python
class Person(models.Model):
    pid = models.AutoField(primary_key=True)  #设置主键， 如果没有设置，会自动添加
    name = models.CharField(max_length=32) # varchar(32)
    age = models.IntegerField() #整形
    birth = models.DateTimeField(auto_now_add=True) #新创建对象时自动添加当前时间
    birth = models.DateTimeField(auto_now=True) #修改对象的时候改变时间
```



### 自定义的字段

1. 自定义字段

```python
class MyCharField(models.Field):
    """
    自定义的char类型的字段类
    """
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)
    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length  #char(11)
```

2. 输入数据库迁移命令

```
python manage.py makemigrations
#因为是添加字段，所以会出现以下图片的内容：
```

![image-20200812123047869](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200812123047869.png)

![image-20200812123054818](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200812123054818.png)

给前面字段添加默认参数，或者添加默认值(default)

3. 使用

```python
class Person(models.Model):
    #添加自定义的字段
    cname = MyCharField(max_length=11) #char(11)
```

![image-20200812123229954](C:\Users\Bee\AppData\Roaming\Typora\typora-user-images\image-20200812123229954.png)



### model字段参数

添加或删除字段，记得都要迁移一下数据库

```python
null=True	该字段在数据库可以为空
blank=True	允许用户输入为空(True就是必须输入)
db_column	数据库中字段的列名(别名)
defalut		默认值	(在admin中显示默认) 
db_index	建立索引
unique=True	唯一约束(表示不能为重复的，如果有重复的就会报错) 如果新创建一个数据库和unique=True一起迁移，那一定不能有重复的元素，不然就删除了新迁移的数据，在重新迁移
verbose_name显示的字段名 (在admin中显示)
choices		用户选择的参数 models.BooleanField(choices=((True,"男"),(False,"女"))) 下拉选择框

更多更详细的数据：https://www.cnblogs.com/maple-shaw/articles/9323320.html
```

例：

```python
class Person(models.Model):
    pid = models.AutoField(primary_key=True)  #设置主键， 如果没有设置，会自动添加
    name = models.CharField(verbose_name="姓名",db_column='nick',max_length=32, blank=True,unique=True) # varchar(32)
    age = models.IntegerField(null=True,default=18) #整形
    birth = models.DateTimeField(auto_now_add=True) #新创建对象时自动添加当前时间
    # birth = models.DateTimeField(auto_now=True) #修改对象的时候改变时间
    sex = models.BooleanField(choices=((True,"男"),(False,"女"))) #0为True  1为False
    #添加自定义的字段
    cname = MyCharField(max_length=11)  #char(11)
```



### model表的参数

修改表的(要迁移数据库，不要忘记)

```python
class Person(models.Model):
    pid = models.AutoField(primary_key=True)  #设置主键， 如果没有设置，会自动添加
    name = models.CharField(verbose_name="姓名",db_column='nick',max_length=32, blank=True,unique=True) # varchar(32)
    age = models.IntegerField(null=True,default=18) #整形
    birth = models.DateTimeField(auto_now_add=True) #新创建对象时自动添加当前时间
    # birth = models.DateTimeField(auto_now=True) #修改对象的时候改变时间
    sex = models.BooleanField(choices=((True,"男"),(False,"女"))) #0为True  1为False
    #添加自定义的字段
    cname = MyCharField(max_length=11)  #char(11)

    class Meta:
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名(右边这个Database里面的数据表)
        db_table = "Person"
        
        # admin中显示的表名称
        verbose_name = '个人信息'

        # verbose_name加s   admin中显示
        verbose_name_plural = '所有用户信息'

        # 联合索引  会和上面的unique=True冲突，所以一定要看好
        index_together = [
            ("name", "age"),  # 应为两个存在的字段
        ]

        # 联合唯一索引  会和上面的unique=True冲突，所以一定要看好
        unique_together = (("name", "age"),)  # 应为两个存在的字段

```







## 三、ORM单表增删改查

#### 增

- save()
- create()
- bulk_create()
- update_or_create()

```python
# 创建记录方式1
    student_obj = models.Student(
        name='老王',
        age=19,
    )
    student_obj.save() # 刷到表里
# 创建记录方式2
    new_obj = models.Student.objects.create(name='小李', age=15) # Student object -- models对象
    print(new_obj.name)
    print(new_obj.age)

# 创建方式3
    批量创建
    objs = []
    for i in range(20):
        obj = models.Student(
            name='xiangxi%s' % i,
            age=10 + i,
        )
        objs.append(obj)

    models.Student.objects.bulk_create(objs)

# 创建方法4
    update_or_create() 有就更新 没有就创建、
    models.Student.objects.update_or_create(
        name='老王2',
        defaults={
            'age':48,
        }
    )
```

#### 删

- delete()

```python
# 删除 delete  queryset 和 model 都可以调用
models.Student.objects.get(id=2).delete()  # model对象调用delete方法
models.Student.objects.filter(name='小小').delete()
models.Student.objects.all().delete()  # 删除所有
```

#### 改

- update()

```python
# 更新 update() 方法  model对象不能调用更新方法 只能QuerySet调用
models.Student.objects.filter(name='老王').update(age=29)
```

#### 查

- .all() 查询所有，返回querySet集合（类似于列表）
- .filter() 查不到返回一个空集合不报错，返回QuerySet
- .get() 有且只有1个结果(没有或者多于一个结果报错)，返回model对象

```python
# 简单查询
all_obj = models.Student.objects.all()  # 查询所有
print(all_obj)  # <QuerySet [<Student: Student object>, <Student: Student object>]>--类似于列表 -- QuerySet集合
for i in all_obj:
    print(i.name)

# 条件查询  .filter() 返回的也是QuerySet集合，查不到返回一个空集合，不报错
objs = models.Student.objects.filter(id=2)
objs = models.Student.objects.filter(name='老王')
print(objs)

# 条件查询  get() 返回的是model对象，而且get方法有且必须有1个结果
obj = models.Student.objects.get(id=1)
print(obj)  # 老王
obj = models.Student.objects.get(name='小小')  # 报错1，查询结果多于1个
get() returned more than one Student -- it returned 2!
obj = models.Student.objects.get(name='大大')  # 报错2 没有查询到任何内容
# Student matching query does not exist.
print(obj)
```



### 查询接口

```python
<1> all():                  查询所有结果，结果是queryset类型

<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象，结果也是queryset类型 Book.objects.filter(title='linux',price=100) #里面的多个条件用逗号分开，并且这几个条件必须都成立，是and的关系，or关系的我们后面再学，直接在这里写是搞不定or的
      models.Student.objects.filter(id=7, name='xiangxi0').update(
            name='小小妹妹',
            age=18,
        )
  
<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，不是queryset类型，是行记录对象，返回结果有且只有一个，
                            如果符合筛选条件的对象超过一个或者没有都会抛出错误。捕获异常try。  Book.objects.get(id=1)
  
<4> exclude(**kwargs):      排除的意思，它包含了与所给筛选条件不匹配的对象，没有不等于的操作昂，用这个exclude，返回值是queryset类型 Book.objects.exclude(id=6)，返回id不等于6的所有的对象，或者在queryset基础上调用，Book.objects.all().exclude(id=6)
 　　　　　　　　　　　　　　　　
<5> order_by(*field):       queryset类型的数据来调用，对查询结果排序,默认是按照id来升序排列的，返回值还是queryset类型
　　　　　　　　　　　　　　　　  models.Book.objects.all().order_by('price','id') #直接写price，默认是按照price升序排列，按照字段降序排列，就写个负号就行了order_by('-price'),order_by('price','id')是多条件排序，按照price进行升序，price相同的数据，按照id进行升序
        
<6> reverse():              queryset类型的数据来调用，对查询结果反向排序，返回值还是queryset类型
  
<7> count():                queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量。
  
<8> first():                queryset类型的数据来调用，返回第一条记录 Book.objects.all()[0] = Book.objects.all().first()，得到的都是model对象，不是queryset
  
<9> last():                queryset类型的数据来调用，返回最后一条记录
  
<10> exists():              queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False
　　　　　　　　　　　　　　     空的queryset类型数据也有布尔值True和False，但是一般不用它来判断数据库里面是不是有数据，如果有大量的数据，你用它来判断，那么就需要查询出所有的数据，效率太差了，用count或者exits
　　　　　　　　　　　　　　　　 例：all_books = models.Book.objects.all().exists() #翻译成的sql是SELECT (1) AS `a` FROM `app01_book` LIMIT 1，就是通过limit 1，取一条来看看是不是有数据

<11> values(*field):        用的比较多，queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                            model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。
<12> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
 
<13> distinct():            values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录
```



### 必会必知13条

```python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

import django

django.setup()

from app01 import models

#  all 查询所有的数据  QuerySet  对象列表  【对象，对象】
ret = models.Person.objects.all()  # 光查询这个的话是先调用的__repr__

#  get 获取一个有且唯一的数据  对象  没有或者多个就报错(其实就是Id为1的)
ret = models.Person.objects.get(pk=1)  # 有具体查询的就是直接调用的__str__

#  filter 获取满足条件的数据  对象列表  【对象，对象】 没有会返回一个空的列表
ret = models.Person.objects.filter(pk=1)

#  order_by 排序 默认升序 如果字段前加-号，就变成降序排序 【可以多字段排序】
ret = models.Person.objects.all().order_by("-age", "pid")

#  reverse 对已经排序的对象列表进行翻转
ret = models.Person.objects.all().order_by("pid").reverse()

#  values 不指定字段  获取数据所有的字段和值 QuerySet [{},{},{}] 字典
#  指定字段 获取数据指定的字段名和值 QuerySet [{"pid":5,"name":111}] 字典
ret = models.Person.objects.all().values("pid", "name")

#  values_list 不指定字段 获取数据所有的值 QuerySet [(),()] 元组
#  指定字段 获取数据指定字段的值 QuerySet  [('111', 5), ('1111', 3)]
ret = models.Person.objects.all().values_list("name", "pid")

#  distinct 去重(去除age一样的)
ret = models.Person.objects.values("age").distinct()

#  count 计数
ret = models.Person.objects.all().count()

#  first 获取第一个元素
ret = models.Person.objects.all().first()

#  last 获取最后一个元素
ret = models.Person.objects.all().last()

#  exists 判断是否有结果 True,False
ret = models.Person.objects.filter(pk=2).exists()
print(ret)

"""
返回对象列表
all
filter
exclude   取反
order_by
reverse
values      [{},{}]
values_list     [(),()]
distinct

返回对象
get
first
last

返回数字
count

返回布尔值
exists
"""
```





### 基于双下划线的模糊查询

- in 之中
- gt 大于等于
- lt 小于等于
- range 区间
- contains / icontains 包含
- startswidth 开头
- year 日期 (查找日期的时候要注意时区的问题，在settings.py中改USE_TZ为FALSE)

```python
Book.objects.filter(price__in=[100,200,300]) #price值等于这三个里面的任意一个的对象
Book.objects.filter(price__gt=100)  #大于，大于等于是price__gte=100，别写price>100，这种参数不支持
Book.objects.filter(price__lt=100)
Book.objects.filter(price__range=[100,200])  #sql的between and，大于等于100，小于等于200
Book.objects.filter(title__contains="python")  #title值中包含python的
Book.objects.filter(title__icontains="python") #不区分大小写
Book.objects.filter(title__startswith="py") #以什么开头，istartswith  不区分大小写
Book.objects.filter(pub_date__year=2012）
# 日期查询
# all_books = models.Book.objects.filter(pub_date__year=2012) #找2012年的所有书籍
    # all_books = models.Book.objects.filter(pub_date__year__gt=2012)#找大于2012年的所有书籍
    all_books = models.Book.objects.filter(pub_date__year=2019,pub_date__month=2)#找2019年月份的所有书籍，如果明明有结果，你却查不出结果，是因为mysql数据库的时区和咱们django的时区不同导致的，了解一下就行了，你需要做的就是将django中的settings配置文件里面的USE_TZ = True改为False，就可以查到结果了，以后这个值就改为False，而且就是因为咱们用的mysql数据库才会有这个问题，其他数据库没有这个问题。
```



### 单表的双下划线

```python
ret = models.Person.objects.filter(pid__lt=5)  # 字段__条件 = less than pid小于5的
ret = models.Person.objects.filter(pid__gt=5)  # 字段__条件 = less than pid大于5的
ret = models.Person.objects.filter(pid__lte=5)  # 字段__条件 = less than equal pid小于等于5的
ret = models.Person.objects.filter(pid__gte=5)  # 字段__条件 = less than pid equal 大于等于5的

ret = models.Person.objects.filter(pid__range=[1, 6])  # 范围 在1到6之间的 包括1和6
ret = models.Person.objects.filter(pid__in=[1, 3, 11])  # 成员判断 pid中有没有 为1，3，11的

ret = models.Person.objects.filter(name__contains="李小小")  # 表示name里面有没有包含"李小小"的
ret = models.Person.objects.filter(name__icontains="a")  # 表示name里面有没有包含"a/A"的 加i了忽略大小写

ret = models.Person.objects.filter(name__startswith="李")  # 表示name以“李”开头的
ret = models.Person.objects.filter(name__istartswith="a")  # 表示name以“a/A”开头的,忽略大小写

ret = models.Person.objects.filter(name__endswith="小")  # 表示name以“小”结尾的
ret = models.Person.objects.filter(name__iendswith="a")  # 表示name以“a/A”结尾的,忽略大小写

ret = models.Person.objects.filter(birth__year="2020")  # 表示birth里面年为2020的
# ret = models.Person.objects.filter(birth__month="2")  # 表示birth里面月为2的
# ret = models.Person.objects.filter(birth__day="21")  # 表示birth里面日期为21的

ret = models.Person.objects.filter(birth__contains="-10-")  # 表示月份为10的

ret = models.Person.objects.filter(name__isnull=False)  # 输出name字段不为空的
```

