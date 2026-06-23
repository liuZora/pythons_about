## 三、QFormLayout表单

一般适用于提交数据**form表单**。比如： 登录，注册类似的场景

### 常用方法

- **`addRow(label, widget)`**: 添加一行，其中 `label` 是标签文本，`widget` 是要放置在标签旁边的控件。例如，`form_layout.addRow("账号：", edit)` 将 "账号：" 标签和 `edit` 控件添加到同一行。
- **`addRow(label, widget1, widget2)`**: 添加一行，其中 `widget1` 和 `widget2` 放置在标签 `label` 旁边，适用于需要两个控件的情况。
- **`setLabelAlignment(Qt.Alignment)`**: 设置所有标签的对齐方式，如 `Qt.AlignRight右对齐` 或 `Qt.AlignLeft`。
- **`setFieldGrowthPolicy(policy)`**: 设置控件在布局中的增长策略，例如 `QFormLayout.ExpandingFieldsGrow` 使得控件在布局中可以扩展以填满空间。

```python
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QApplication, QWidget


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设定当前Widget的宽高(可以拉伸大小)
        # self.resize(300, 200)
        # 禁止改变宽高（不可以拉伸）
        self.setFixedSize(300, 150)

        # 外层容器
        container = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        # 创建1个输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入账号")
        form_layout.addRow("账号：", edit)

        # 创建另外1个输入框
        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        form_layout.addRow("密码：", edit2)

        # 将from_layout添加到垂直布局器中
        container.addLayout(form_layout)

        # 按钮
        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)

        # 把按钮添加到容器中，并且指定它的对齐方式
        container.addWidget(login_btn, alignment=Qt.AlignRight)

        # 设置当前Widget的布局器，从而显示这个布局器中的子控件
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
```

运行效果：

<img src=".\assets\8 QFormLayout表单布局_test.PNG" alt="8 QFormLayout表单布局_test" style="zoom:67%;" />

## 四、QStackedLayout抽屉布局

提供了多页面切换的布局，一次只能看到一个界面。 **抽屉布局**

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QLabel


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2要显示的内容", self)
        self.setStyleSheet("background-color:red;")


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 创建堆叠(抽屉)布局
        self.stacked_layout = QStackedLayout()
        # 创建单独的Widget
        win1 = Window1()# 实例化类
        win2 = Window2()# 实例化类
        # 将创建的2个Widget添加到抽屉布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 设置Widget大小以及固定宽高
        self.setFixedSize(300, 270)

        # 1. 创建整体的布局器
        container = QVBoxLayout()

        # 2. 创建1个要显示具体内容的子Widget，用于创建一个子窗口
        widget = QWidget()
        #将抽屉布局器设置为创建的子窗口的布局器
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        # 3. 创建2个按钮，用来点击进行切换抽屉布局器中的Widget
        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")
        # 给按钮添加事件（即点击后要调用的函数）
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        # 4. 将需要显示的空间添加到布局器中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        # 5. 设置当前要显示的Widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget--》对应的是 self.stacked_layout.addWidget(win1)
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget--》对应的是 self.stacked_layout.addWidget(win2)
        self.stacked_layout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MyWindow()
    win.setWindowTitle("QStack抽屉布局_test")
    win.show()

    app.exec()
```

效果：

<img src=".\assets\9_1 QStack抽屉布局_test.PNG" alt="9_1 QStack抽屉布局_test" style="zoom:67%;" /><img src="C:\Users\liujinfeng\Desktop\pythonLJF\PyQt5\assets\9_2 QStack抽屉布局_test.PNG" alt="9_2 QStack抽屉布局_test" style="zoom:67%;" />

# 信号与槽

## 一、说明

`信号`和`槽`是 Qt的核心内容

### 1. 信号(signal)

其实就是事件（按钮点击 、内容发生改变 、窗口的关闭事件） 或者是 状态 （check选中了， togglebutton 切换。）

当程序触发了某种状态或者发生了某种事件（比如：按钮被点击了, 内容改变等等），那么即可发射出来一个`信号`。

### 2. 槽( slot)

若想捕获这个信号，然后执行相应的逻辑代码，那么就需要使用到 `槽` ， `槽`实际上是一个函数， 当`信号`发射出来后，会执行与之绑定的`槽`函数

### 3. 将信号与槽链接

为了能够实现，当点击某个按钮时执行某个逻辑，需要把具体的`信号`和具体的`槽`函数绑定到一起.

操作大体流程如下

```python
对象.信号.connect(槽函数)
```

![img](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/signal_slot.png)

需求：

```markup
当出现了某一种信号（某一种事件）的时候，需要执行一段代码（用函数来包装这份代码。）
```

解决的办法：

```markup
信号和槽
```

## 二、案例1--功能：接收信号

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 更改当前Widge的宽高
        self.resize(500, 300)
        # 创建一个按钮
        btn = QPushButton("可点击的按钮", self)
        # 设置窗口位置、宽高
        btn.setGeometry(150, 150, 200, 40)
        # 将按钮被点击时触发的信号与我们定义的函数（方法）进行绑定
        # 注意：这里没有()，即写函数的名字，而不是名字()
        btn.clicked.connect(self.click_my_btn)

    def click_my_btn(self):
    #def click_my_btn(self, arg):
        # 槽函数，点击按钮则调用该函数
        # 这里的参数正好是信号发出，传递的参数
        print("点击按钮后屏幕打印显示")
        #print("点击按钮啦~", arg)  arg打印false


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.setWindowTitle("function_test")
    w.show()

    app.exec()
```

运行效果：

<img src="C:\Users\liujinfeng\Desktop\pythonLJF\PyQt5\assets\13 function_test.PNG" alt="13 function_test" style="zoom:67%;" />

## 三、案例2：自定义信号【重点】

1、创建：定义一个类属性：pyqtSignal(参数)----》2、绑定：给信号绑定槽函数---》3、触发： self.自定义信号my_signal.emit(参数)触发，最后被绑定的槽函数就会被执行

除了接收Qt自带的信号之外，我们也可以自行定义信号，在合适的时机，自行发射信号

注意：自定义信号需要使用到 `pyqtSignal`来声明信号 ，并且需要在类中的函数之外声明，不能在方法中定义,（只能在类属性定义）

如果会自定义信号，那么信号和槽基本上也就掌握了。否则永远只会接收别人发射出的信号

找属性：先找实例对象self中是否有，然后再实例对象的类属性中去寻找。例如 self.my_signal.connect(self.my_slot)

表示发射信号 对象.信号.发射(参数)，emit相当于触发

`QScrollArea` 是一个滚动区域部件，用于显示内容超出其可视区域时提供滚动条。它通常用于显示较大的内容或控件，允许用户通过滚动查看全部内容。

### 作用

- **显示超出视窗的内容**: 如果内部控件的大小超出了 `QScrollArea` 的视窗，会自动提供滚动条。
- **嵌套布局**: 可以嵌套复杂的布局和控件，使其可以在滚动区域内显示。

### 主要方法

- **`setWidget(widget)`**: 设置要在滚动区域中显示的部件。
- **`setWidgetResizable(True)`**: 设置部件是否应自动调整大小以适应滚动区域。()  
- **`horizontalScrollBar()`** 和 **`verticalScrollBar()`**: 获取水平和垂直滚动条对象，以便进行进一步的配置。

```python
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    # 声明一个信号 只能放在函数的外面--->创建自定义信号 （只能在类属性定义）
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()  # 用来存放消息

    def init_ui(self):
        self.resize(500, 200)

        # 创建一个整体布局器
        container = QVBoxLayout()

        # 用来显示检测到漏洞的信息
        self.msg = QLabel("")
        self.msg.resize(440, 15)
        # print(self.msg.frameSize())   PyQt5.QtCore.QSize(439, 14)
        #print(self.msg)                <PyQt5.QtWidgets.QLabel object at 0x00000263BB833B88>
        self.msg.setWordWrap(True)  # 自动换行
        self.msg.setAlignment(Qt.AlignTop)  # 靠上
        # self.msg.setStyleSheet("background-color: yellow; color: black;")

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建水平布局器
        h_layout = QHBoxLayout()
        #创建按钮
        btn = QPushButton("开始检测", self)
        # 绑定按钮的点击，点击按钮则开始检测---》调用check函数 
        btn.clicked.connect(self.check)
        
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 设置布局器
        self.setLayout(container)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        # 更新内容
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        self.msg.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def check(self):
        # 列表推导式 生成一个包含 IP 地址（从 192.168.1.1 到 192.168.1.254）的列表
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            #使用 enumerate 函数为每个 IP 地址生成一个 (索引, IP 地址) 的二元组。
            msg = "模拟，正在检查 %s 上的漏洞...." % ip
            # print(msg)
            if i % 5 == 0:
 # 表示发射信号 对象.信号.发射(参数)，因为之前 self.my_signal.connect(self.my_slot)绑定信号和槽，----》相当于调用了my_slot函数：def my_slot(self, msg)
                self.my_signal.emit(msg + "【发现漏洞】")
            time.sleep(0.01)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
```

效果：

<img src="C:\Users\liujinfeng\Desktop\pythonLJF\PyQt5\assets\14 pyqtSignal_test.PNG" alt="14 pyqtSignal_test" style="zoom:67%;" />

## 四、作业

左边的控件是 `QDial` ， 右边的控件是 `QSpinBox` 。两者相互关联，转动刻度右边的数字随之改变，改变右边的数字，左边的刻度盘也跟着转到指定位置。

<img src=".\assets\15 信号与槽_test.PNG" alt="15 信号与槽_test" style="zoom:67%;" />

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout,QSpinBox,QDial
 
class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()
 
        # 设置大小
        self.resize(300, 300)
        # 设置标题
 
        h_layout = QHBoxLayout() 
        self.spinBox = QSpinBox()
        self.dial = QDial()
        h_layout.addWidget(self.dial)
        h_layout.addWidget(self.spinBox)
        self.setLayout(h_layout)
        self.spinBox.valueChanged.connect(self.changed_spinBox)
        self.dial.valueChanged.connect(self.changed_dial)
 
    def changed_spinBox(self, value):
        # 槽函数，点击按钮则调用该函数
        self.dial.setValue(value)
        # 这里的参数正好是信号发出，传递的参数
        print("数值改变啦", value)
 
    def changed_dial(self, value):
        # 槽函数，点击按钮则调用该函数
        self.spinBox.setValue(value)
        # 这里的参数正好是信号发出，传递的参数
        print("数值改变啦", value)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)   #只要是QT制作的app,必须只有一个QApplication对象
 
    w = MyWindow()             #创建一个 QWidget 对象
    # 设置窗口标题
    w.setWindowTitle("作业")
    # 展示窗口
    w.show()
 
    # 程序进行循环等待状态
    app.exec() #程序开始运行
```



## 案例：模拟发送网络测试

<img src=".\assets\16 mySignal_test.PNG" alt="16 mySignal_test" style="zoom:67%;" />

```python
import sys
import time
 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
class MyWindow(QWidget):
    my_signal = pyqtSignal(str)
 
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()
 
    def init_ui(self):
        self.resize(500, 200)
 
        # 创建第一个整体布局器
        container = QVBoxLayout()
 
        # 显示检测的信息
        self.msg = QLabel("")
        self.msg.resize(440, 15)#宽400，每行字体高度15
        self.msg.setWordWrap(True) # 自动换行
        self.msg.setAlignment(Qt.AlignTop) # 靠上
        self.msg.setStyleSheet("background-color: yellow; color: black;")
 
        # 创建一个滚动对象，内容增加时会自动滚动，滚动对象需要放进对象布局器实现
        scroll = QScrollArea()
        scroll.setWidget(self.msg)
 
        # 创建垂直布局器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)
 
        # 创建水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("Detection", self)
        # 信号与槽事件绑定
        btn.clicked.connect(self.check)
        h_layout.addStretch(1) # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)
 
        # 将显示的空间和布局器添加到container中
        container.addLayout(v_layout)
        container.addLayout(h_layout)
 
        # 设置布局器
        self.setLayout(container)
 
        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)
 
    def my_slot(self, msg):
        # 更新内容
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        #自动更新大小不好使，采用手动更新大小
        self.msg.resize(540, self.msg.frameSize().height() + 15)
        self.msg.repaint()#刷新页面，更新内容，防止不更新可能没有显示内容
 
    def check(self):
        for i, ip in enumerate(["192.172.1.%d" % x for x in range(1, 255)]):
            msg = "模拟，正在检查 %s 上的漏洞..." % ip
            if i % 5 == 0:
                self.my_signal.emit(msg + "发现漏洞！！")  # 这里相当于调用了my_slot函数
            else:
                self.my_signal.emit(msg + "正常！")
 
            time.sleep(0.01)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建对象
 
    w = MyWindow()
    w.setWindowTitle("mySignal_test")
    w.show()
 
    # 程序进行循环等待状态
    app.exec_()
```

# 练习

### 第一个PyQT程序

<img src=".\assets\练习01.PNG" alt="练习01" style="zoom:50%;" />

```python
import sys

from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("第一个PyQt程序")
window.resize(500, 500)
window.move(400, 250)

label = QLabel(window)
label.setText("Hello world")
label.move(200, 240)

window.show()

sys.exit(app.exec_())
```



# Qt Designer

## 一、介绍

纯靠代码来编写界面，效率属实是有点底，今天我们用另外一个辅助设计图形化的软件 `QT Designer`

### 1. 下载

Mac版本：https://pan.baidu.com/s/1pxY05LeB0X8e3-uQWjo97Q?pwd=g4uc

Windows版本：https://pan.baidu.com/s/1iLqgzbDrZpoidRNSuf6Msw?pwd=gw4f

### 2. 安装&运行

安装过程很简单，按照正常软件安装即可，安装后的图片如下图：

![image-20201123214407351](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123214407351.png)

**但Mac平台用户要注意，运行时会出现如下图问题**：

![img](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/234234234234234.png)

**解决办法**：在“应用程序”文件夹，按住`control`键然后运行。只需要这种方式运行第一次即可，以后运行就像普通软件一样打开

![image-20201123214951153](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123214951153.png)

## 二、使用QT Designer

Mac运行之后的效果如下：

![image-20201123215209758](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215209758.png)

Windows基本也是如此，只是效果略有不同

## 三、使用流程

![image-20201123215321248](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215321248.png)

2.此时会创建一个新的窗口，如下效果

![image-20201123215359517](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215359517.png)

3.拖动想要的控件

![image-20201123215551661](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215551661.png)

4.选中控件，看属性

![image-20201123215750887](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215750887.png)

5.修改属性

![image-20201123215829602](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123215829602.png)

6.如果没有看到preperty等窗口怎么办？看下图

![image-20201123220059274](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123220059274.png)

7.信号与槽（没有没有看到Singal/Slot Editor请按照上一步操作进行显示）

![image-20201123220951729](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123220951729.png)

8.预览效果

![image-20201123221137373](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123221137373.png)

![image-20201123221237467](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123221237467.png)

9.保存

![image-20201123221409036](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123221409036.png)

我起名叫`tset.ui`保存后的效果如下：

![image-20201123221511280](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123221511280.png)

10.python代码使用`test.ui`文件

若要加载ui文件，则需要导入 `uic` 模块 , 它位于`PyQt5` 中

```python
"""
动态加载ui文件
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./test.ui")
    # 展示窗口
    ui.show()

    app.exec()
复制Error复制成功...
```

将`test.ui`与上述代码文件放到同一个路径下，运行次`.py`文件后的效果 如下：

![image-20201123221857466](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123221857466.png)

## 四、练习

请使用QT Designer设计如下效果

![image-20201123222952865](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123222952865.png)

## 五、进阶使用案例

目的：获取用户名、密码，在TextBrowser中显示一些登录的信息

用到的技术：python加载`.ui`文件获取了界面，对`.ui`文件中的控件操作，完成信号与槽的绑定等

1.看看`.ui`文件有什么属性，如下图

![image-20201123223607472](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123223607472.png)

在这里，我们看到加载后的`.ui`文件有7个对象属性，正好与在设计`.ui`文件时控件的数量一致，可见属性的个数正好对应`.ui`文件中的空间个数，所以想要操作哪个空间，就通过`对象.属性`的方式从`.ui`对象中提取即可。当然了不能盲目的提取，这些属性的名字其实就是在`.ui`文件中的空间的`Object name`，如下图

![image-20201123223905659](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123223905659.png)

2.编写代码如下：

```python
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./login.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        if user_name == "admin" and password == "123456":
            self.textBrowser.setText("欢迎%s" % user_name)
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText("用户名或密码错误....请重试")
            self.textBrowser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()
```

效果如下：

![image-20201123224751151](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201123224751151.png)

