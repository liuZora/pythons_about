三种表关系：一对一、一对多、多对多。

## 一、创建模型

- OneToOneField() 一对一
- ForeignKey() 一对多 多对一
- ManyToManyField() 多对多

```python
#添加外键 一对多 多对一
class Book(models.Model):
    name = models.CharField(max_length=32)
    # 添加外键ForeignKey
    publishers = models.ForeignKey(Publisher, on_delete=models.CASCADE) #默认是级联删除
    """
        on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
        on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
        on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
        on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
        on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
        on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
        on_delete=models.SET,         # 删除关联数据,
        a. 与之关联的值设置为指定值,设置：models.SET(值)
        b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
    """
```



```python
class Author(models.Model):
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
    # 一对一到详细信息表
    # foreign+unique 不写tofield会自动关联主键
    # on_delete = models.CASCADE 被关联的键删除后跟它有关联的也都删除了
    # on_delete = models.SET_NULL 被关联的删除后，关联的变为空

class AuthorDetail(models.Model):#不常用的放到这个表里面

    birthday=models.DateField()
    # telephone=models.BigIntegerField()
    telephone=models.CharField(max_length=32)
    addr=models.CharField( max_length=64)

# 出版社表和书籍表是一对多的关系Forirgn
class Publish(models.Model):
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()  # 实际上是CharField --- 但是后期可以校验格式xx@xx.


class Book(models.Model):

    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方，字段publish如果是外键字段，那么它自动是int类型
    publishs=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
    # foreign key(publish) references publish(id)

    authors=models.ManyToManyField(to='Author',)  # author不是表的字段，知识类的一个属性，用来操作下边的第三张表，写在被关联的那张表里也可以

# manytomany会自动生成下边这样一张表，如果还有其他字段可以手动创建这张表
# class BookToAuthor(models.Model):
#     book_id = models.ForeignKey(to="Book",to_field="id",on_delete=models.CASCADE)
#     author_id = models.ForeignKey(to="Author",to_field="id",on_delete=models.CASCADE)
```



## Django–admin

1. 创建一个超级用户

```python
python manage.py createsuperuser

Username (leave blank to use 'bee'): root	#输入用户名，默认为bee
Email address: 			#电子邮箱
Password:				#输入root1234
Password (again):		#root1234
Superuser created successfully.
```

​	2. 在app下的admin.py中注册model

```python
from django.contrib import admin
from app01 import models
# Register your models here.

admin.site.register(models.Person) # 操作的表名
admin.site.register(models.User) # 操作的表名
```

3. 登录网页http://127.0.0.1:8000/admin/进行操作

```
登录之后就进入admin页面，就可以操作数据库了
输入刚以输入的用户root和密码root1234
```



## views.py通过models操作

### 增

```python
from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
def query(request):
    # 增
    # 一对一增加
    new_author_detail = models.AuthorDetail.objects.create(
        birthday='1979-08-08',
        telephone='13456789876',
        addr='黑龙江哈尔滨',
    )
    # 方式1
    models.Author.objects.create(
        name='卡特',
        age=18,
        authorDetail=new_author_detail,
    )
    # 方式2 常用
    obj = models.AuthorDetail.objects.filter(addr='陕西临汾').first()
    models.Author.objects.create(
        name='卡特',
        age=18,
        authorDetail_id=obj.id,
    )

    # 一对多
    # 方式1
    models.Book.objects.create(
        title='祖安快嘴练习生',
        publishDate='2019-08-09',
        price=3,
        publishs=models.Publish.objects.get(id=1),
    )
    # 方式2 常用
    models.Book.objects.create(
        title='祖安快嘴练习生2',
        publishDate='2019-08-09',
        price=3,
        publishs_id=models.Publish.objects.get(id=1).id,
    )

    # 多对多
    # 方式1 常用
    book_obj = models.Book.objects.get(id=1)
    book_obj.authors.add(*[1, 2])
    # 方式2
    author1 = models.Author.objects.get(id=1)
    author2 = models.Author.objects.get(id=3)
    book_obj_ = models.Book.objects.get(id=5)
    book_obj_.authors.add(*[author1, author2])
    


    return HttpResponse('ok')
```

### 删

```python
# 删除
# 一对一和多对一的情况和单表删除的操作相同
# 一对一
# author也会跟着级联删除
models.AuthorDetail.objects.get(id=2).delete()
# 删除author对AuthorDetail没有影响
models.Author.objects.get(id=1).delete()

# 一对多
# 删出版社，这个出版社下边的书全部被级联删除
models.Publish.objects.get(id=1).delete()
# 删除某本书,不会对出版社有影响
models.Book.objects.get(id=2).delete()

# 多对多
# 删除id为3的那本书的作者里边id为4和5的作者，就是id=3的书没有作者4和5了，书还在，作者也在，知识删掉自动生成的 book_author那张表里的记录
book_obj_1 = models.Book.objects.get(id=3)
book_obj_1.authors.remove(*[4, 5])
# 方式2就是找到作者对象，放进列表去
book_obj_1.authors.clear()  # 把id=3的对应的作者记录全删了
book_obj_1.authors.set(['5', '6'])  # 先清空，再添加个5和6
```

### 改

```python
# 更新
# 一对一
# 把id=2的作者新更改
models.Author.objects.filter(id=2).update(
    name='厄加特',
    age=18,
    # authorDetail=models.AuthorDetail.objects.get(id=5),
    authorDetail_id=5,  # 两种方式
)

# 一对多
# 把id=4的书的出版社改为3的出版社
models.Book.objects.filter(pk=4).update(  # pk表的主键字段
    title='B哥往事',
    # publishs=models.Publish.objects.get(id=3),
    publishs_id=3,  # 两种方式
)
# 不会做级联更新，orm没有级联更新，可以在mysql中级联更新，自查
```

### 查

```python
def books_list(request):
    # 获取数据库里面的内容
    all_books = models.Book.objects.all()
       for i in all_books:
        print(i.publishers.name, i.publishers.id,i.publishers_id) # 书籍所关联的出版社对象nam
    return render(request, "books_list.html", {"all_books": all_books})
```



## 查询

### 基于对象的跨表查询-类似于子查询

**正向查询和反向查询**

通过设立约束关系的表想被约束关系的表查询是正向查询–从大腿想孩子查

反过来查就是反向查询

正向查询：关系属性（字段）卸载哪个类（表）里边，从当前类（表）的数据去查询它的关联类（表）的数据。

反向查询：反之。

```python
# 一对一
# 正向查询
# 查询盖伦的住址
author_obj = models.Author.objects.filter(name='盖伦').first()
print(author_obj.authDetail.addr)  # 盖伦的那一条AuthorDetail
# 反向查询
# 查询444这个电话号是谁的？
author_detail_obj = models.AuthorDetail.objects.get(telephone='444')
print(author_detail_obj.author.name)
# Author ---------> AuthorDetail  正向查询 author_obj.authDetail.addr， 对象.关联名称
# Author <--------- AuthorDetail 反向查询 author_detail_obj.author.name，对象.小写类名

# 一对多
# 正向查询
# 查询一下 李帅的床头故事 这本书的出版社是哪个
book_obj = models.Book.objects.get(title='李帅的床头故事')
print(book_obj.publishs.name)  # B哥出版社
# 反向查询
# B哥出版社出版了哪些书？
pub_obj = models.Publish.objects.get(name='B哥出版社')
print(pub_obj.book_set.all())  # 一对多，反向找，可能会找到多个，所以加set,结果是QuerySet
# Book -----------> Publish 正向查询 book_obj.publishs.name 对象.属性
# Book <----------- Publish 反向查询 pub_obj.book_set.all() 对象.小写类名_set

# 多对多
# 正向查询
# 李帅的床头故事 这本书是谁写的？
book_obj = models.Book.objects.get(title='李帅的床头故事')
print(book_obj.authors.all())
# 反向查询
# 盖伦写了哪些书？
author_obj = models.Author.objects.get(name='盖伦')
print(author_obj.book_set.all())
# Book ---------------> Author 正向查询 book_obj.authors.all() 对象.属性
# Book <--------------- Author 反向查询 pub_obj.book_set.all() 对象.小写类名_set
```



### 基于双下划线的跨表查询

```python
# 基于双下划线的跨表查询 联表 效率高
# 一对一
# 1.查询盖伦的电话号
# 方式1 正向
obj = models.Author.objects.filter(name='盖伦').values('authorDetail__telephone')
print(obj)  # QuerySet类型
# 方式2 反向
obj = models.AuthorDetail.objects.filter(author__name='盖伦').values('telephone', 'author__age')
print(obj)  # QuerySet类型
# 2.查询哪个老师的电话是444？
# 正向
obj = models.Author.objects.filter(authorDetail__telephone='444').values('name')
print(obj)
# 反向查询
obj = models.AuthorDetail.objects.filter(telephone='444').values('author__name')
print(obj)

# 一对多
# 查询一下 李帅的床头故事 这本书的出版社是哪个？
obj = models.Book.objects.filter(title='李帅的床头故事').values('publishs__name')
print(obj)
obj = models.Publish.objects.filter(book__title='李帅的床头故事').values('name')
print(obj)
# B哥出版社都出版了那些书？
obj = models.Publish.objects.filter(name='B哥出版社').values('book__title')
print(obj)
obj = models.Book.objects.filter(publishs__name='B哥出版社').values('title')
print(obj)

# 多对多
# 李帅的床头故事 这本书是谁写的？
obj = models.Book.objects.filter(title='李帅的床头故事').values('authors__name')
print(obj)
obj = models.Author.objects.filter(book__title='李帅的床头故事').values('name')
print(obj)
# 盖伦写了那些书
obj = models.Book.objects.filter(authors__name='盖伦').values('title')
print(obj)
obj = models.Author.objects.filter(name='盖伦').values('book__title')
print(obj)
```



### 进阶的查询

```python
# 进阶的查询
# 查询B哥出版社出版的书的名称以及作者的名字？
obj = models.Book.objects.filter(publishs__name='B哥出版社').values('title','authors__name')
print(obj)
# 手机号以4开头的作者出版过的所有书籍名称以及出版社名称
# Author AuthorDetail Book Publish
obj = models.Author.objects.filter(authorDetail__telephone__startswith='4').values('book__title', 'book__publishs__name')
print(obj)

# models.py里的calss里，外键起别名
    # publishs=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE,related_name='xxx')  # 反向查询的时候不用写表名了，直接写xxx即可，再写表名就会报错，正向不影响
    # 同样的manytomany也有
```



### 聚合查询  aggregate

`aggregate()`是`QuerySet` 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。

键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的

```python
from django.db.models import Max, Min, Count, Sum, Avg

# 聚合aggregate  终止子句

# {'price__max': Decimal('999.00')}
ret = models.Book.objects.all().aggregate(Max("price"))  # 获取Book表中price的最大值
# {'price__max': Decimal('999.00'), 'price__min': Decimal('1.00')
ret = models.Book.objects.all().aggregate(Max("price"), Min("price"))  # 获取Book表中price的最大,最小值
# {'max': Decimal('999.00'), 'min': Decimal('1.00')}
ret = models.Book.objects.all().aggregate(max=Max("price"), min=Min("price"))  # 设置别名
# {'max': Decimal('999.00'), 'min': Decimal('22.00')}
ret = models.Book.objects.filter(id__lte=5).aggregate(max=Max("price"), min=Min("price"))  # 添加条件让id<=5的最大最小值
# print(ret)
```



### 分组查询group by(annotate)

```python
# 分组 group by
# annotate 注释 过程中使用了分组

# 统计每一本书的作者个数   {'name': '软件工程dsds', 'pub_id': 1} values:表示以什么进行分组
ret = models.Book.objects.annotate(Count("authors")).values("name","pub_id")
# for i in ret:
#     print(i)

# 统计出每个出版社卖最便宜的书的价格
#方法一:
ret = models.Publisher.objects.annotate(Min("book__price")).values()
# for i in ret:
#     print(i)
#方法二:
ret = models.Book.objects.values("pub","pub__name").annotate(Min("price")) # 按照pub_id pub_name进行分组
# for i in ret:
#     print(i)

# 统计不止一个作者的图书
ret = models.Book.objects.annotate(cont=Count("authors")).filter(cont__gt=1) # 两个下划线
# for i in ret:
#     print(i)

# 根据一本图书作者数量的多少对查询集 QuerySet进行排序
ret = models.Book.objects.annotate(count=Count("authors")).order_by("-count")  #加-是降序
# for i in ret:
#     print(i)

# 查询条个作者出的书的总价格
ret = models.Author.objects.annotate(sum=Sum("books__price")).values()
# for i in ret:
#     print(i)
ret = models.Book.objects.values("authors","authors__name").annotate(sum=Sum("price"))
# for i in ret:
#     print(i)

更多资料：https://www.cnblogs.com/maple-shaw/articles/9403501.html
```



### F和Q

```python
from django.db.models import F,Q

# F
ret = models.Book.objects.filter(kucun__lt=50).values("name","kucun") #kucun小于50的书籍

ret = models.Book.objects.filter(sale__gt=F("kucun")).values("name","sale","kucun") # 销售量大于kucun的书籍
# for i in ret:
#     print(i)
models.Book.objects.filter(id__lte=5).update(sale=F("sale")*5+10)  # 更新id小于等于5的，让sale数量*5+10


# Q()
'''
| 或
& 与
~ 非
'''
ret = models.Book.objects.filter(Q(id__lt=4)|Q(id__gt=5)).values("name","id") # id小于4或id大于5的

ret = models.Book.objects.filter(Q(Q(id__lt=3)|Q(id__gt=5)) & Q(name__startswith="张"))

ret = models.Book.objects.filter(Q(Q(id__lt=3)|Q(id__gt=5)) &~ Q(name__startswith="张")).values("name","id")
for i in ret:
    print(i)
```





## 二、外键的操作

1.在models.py创建表，在数据库迁移

```python
class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name="出版社名称")

    def __str__(self):
        return "<Publisher object:{}-{}>".format(self.id,self.name)

class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name="书名")
    pub = models.ForeignKey("Publisher", on_delete=models.CASCADE, related_name="books", related_query_name="book")

    def __str__(self):
        return "<Book object:{}-{}>".format(self.id,self.name)
```

### 基于对象查询

```python
# 正向查询  通过Book表，拿到publisher表
book_obj = models.Book.objects.get(pk=3)  # 获取Book表id为3的
print(book_obj)
print(book_obj.pub)  # 查询Book表id为3的 对应的出版社名称
print(book_obj.pub_id)  # 关系出版社的id

# 反向查询  通过Publisher，拿到Book表
pub_obj = models.Publisher.objects.get(pk=2)  # 获取Publisher表id为2的
# 1.没有指定related_name 就是类名小写_set
print(pub_obj)
print(pub_obj.book_set, type(pub_obj.book_set))  # 类名小写_set   关系管理对象
print(pub_obj.book_set.all())  # 获取全部的书
# 2.指定related_name="books" 没有类名小写_set的写法了
print(pub_obj.books.all())  # 直接  对象.别名.all()
```

### 基于字段查询

```python
ret = models.Book.objects.filter(pub__name="清华出版社2")  # 根据Book表的外键，pub出版社的名字查找对应的书籍
ret = models.Book.objects.filter(pub__name__contains="清华出版社2")  # 根据Book表的外键，包含"清华出版社2"的名称
#  不指定related_name="books" 就是类名小写	不指定related_query_name
ret = models.Publisher.objects.filter(book__name="Hadoop大数据挖掘")
#  指定related_name="books"  指定的名字 不指定related_query_name
ret = models.Publisher.objects.filter(books__name="Hadoop大数据挖掘")
#  指定related_query_name="book"
ret = models.Publisher.objects.filter(book__name="Hadoop大数据挖掘")
```



### 多对多的操作

```python
# 图书表和作者表的多对多的关系
author_obj = models.Author.objects.get(pk=1)  # author-->author_books-->book
print(author_obj.books)  # 关系管理对象
print(author_obj.books.all())  # 所关联的对象集合  3-软件工程dsds

book_obj = models.Book.objects.get(pk=4)  # book-->author_books-->author 用Book 通过author_books表的book_id=4，查询对应的作者
print(book_obj.author_set.all())

ret = models.Book.objects.filter(author__name="李四")  # author--> author_books --> book  4-大数据可视化
ret = models.Author.objects.filter(books__name="大数据可视化")  # book-->author_books-->author

# 关系管理对象的方法
# all 查询所有的对象
print(author_obj.books.all())

# set 设置多对多的关系[id,id] [对象，对象]
author_obj.books.set([3,4,5])  #修改了id=1代表作为3，4，5
author_obj.books.set(models.Book.objects.filter(id_in=[1,2]))

# add 添加多对多关系
author_obj.books.add(6)  # 给id=添加一个代表作6
author_obj.objects.add(models.Book.objects.filter(id__in=[5,6])) # 添加5，6

# remove 删除多对多关系
author_obj.books.remove(3, 4)  # 删除作者1对应的3,4的代表作
 author_obj.books.remove(*models.Book.objects.filter(id__in=[5])) #删除5

#clear 清空多对多关系
author_obj.books.clear

# create 新建一个对象和当前的对象建立关系
author_obj.books.create(name="一二三四",pub_id=2)

```



### 添加快捷键

```
File -->  Settings  -->  Editor --> Live Templates --> Django --> 点击右边的+号 --> 选择 Live Templates --> 在Abbreviation里面输入快捷键名字 --> Template text:里面输入内容
```



## 三、ORM练习题

```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_homework.settings")
django.setup()

from app01 import models

# 1. 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains="金老板")
# 2. 查找出版日期是2018年的书
ret = models.Book.objects.filter(publish_date__year=2018)
# 3. 查找出版日期是2017年的书名
ret = models.Book.objects.values("title").filter(publish_date__year=2017)
# 4. 查找价格大于10元的书
ret = models.Book.objects.filter(price__gt=10)
# 5. 查找价格大于10元的书名和价格
ret = models.Book.objects.values("title", "price").filter(price__gt=10)
# 6. 查找memo字段是空的书
from django.db.models import Q  # 有多个条件的时候可以用Q
ret = models.Book.objects.filter(Q(memo__isnull=True)|Q(memo=""))

# 7. 查找在北京的出版社
ret = models.Publisher.objects.filter(city="北京")
# 8. 查找名字以沙河开头的出版社
ret = models.Publisher.objects.filter(name__startswith="沙河")
# 9. 查找“沙河出版社”出版的所有书籍
ret = models.Book.objects.filter(publisher__name="沙河出版社")
# 10. 查找每个出版社出版价格最高的书籍价格
from django.db.models import Avg,Max,Min,Count,Sum
ret = models.Book.objects.annotate(max=Max("price")).values("publisher","publisher__name","max") # 通过book找publisher
ret = models.Publisher.objects.annotate(max=Max("book__price")).values("name","max")  #通过publisher找book
# 11. 查找每个出版社的名字以及出的书籍数量
ret = models.Publisher.objects.annotate(count=Count("book")).values("name","count")

# 12. 查找作者名字里面带“小”字的作者
ret = models.Author.objects.filter(name__contains="小")
# 13. 查找年龄大于30岁的作者
ret = models.Author.objects.filter(age__gt=30)
# 14. 查找手机号是155开头的作者
ret = models.Author.objects.filter(phone__startswith="155")
# 15. 查找手机号是155开头的作者的姓名和年龄
ret = models.Author.objects.filter(phone__startswith="155").values("name","age")

# 16. 查找每个作者写的价格最高的书籍价格
ret = models.Author.objects.annotate(max=Max("book__price")).values("name","max")
ret = models.Book.objects.values("author","author__name").annotate(max=Max("price"))
# 17. 查找每个作者的姓名以及出的书籍数量
ret = models.Author.objects.annotate(count=Count("book")).values("name","count")
ret = models.Book.objects.values("author","author__name").annotate(count=Count("id"))
# 18. 查找书名是“跟金老板学开车”的书的出版社
ret = models.Book.objects.filter(title="跟金老板学开车").values("publisher__name")
ret = models.Publisher.objects.filter(book__title="跟金老板学开车")
# 19. 查找书名是“跟金老板学开车”的书的出版社所在的城市
ret = models.Book.objects.filter(title="跟金老板学开车").values("publisher__name","publisher__city")
ret = models.Publisher.objects.filter(book__title="跟金老板学开车").values('city')
# 20. 查找书名是“跟金老板学开车”的书的出版社的名称
ret = models.Book.objects.filter(title="跟金老板学开车").values("publisher__name")
ret = models.Publisher.objects.filter(book__title="跟金老板学开车").values('name')
# 21. 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
pub_obj = models.Publisher.objects.filter(book__title="跟金老板学开车").first()
ret = pub_obj.book_set
ret = models.Book.objects.filter(publisher__book__title="跟金老板学开车").exclude(title="跟金老板学开车").values("title","price")

# 22. 查找书名是“跟金老板学开车”的书的所有作者
ret = models.Author.objects.filter(book__title="跟金老板学开车").values("name")
# 23. 查找书名是“跟金老板学开车”的书的作者的年龄
ret = models.Author.objects.filter(book__title="跟金老板学开车").values("age")
# 24. 查找书名是“跟金老板学开车”的书的作者的手机号码
ret = models.Author.objects.filter(book__title="跟金老板学开车").values("phone")
# 25. 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
authors = models.Author.objects.filter(book__title="跟金老板学开车")
# for author in authors:
#     print(author.book_set.values("title","price"))

ret = models.Book.objects.filter(title="跟金老板学开车").values("author__name","author__book__title","author__book__price")
for i in ret:
    print(i)
```

