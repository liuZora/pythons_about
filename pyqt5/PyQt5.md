# PyQt5

## 一、介绍

### [1. Qt](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/01.jieshaoyuanzhuang?id=_1-qt)

![Qt 是什么](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/1-1Z52Q60303101.gif)

Qt（官方发音 `[kju:t]`）是一个跨平台的C++开发库，主要用来开发图形用户界面（Graphical User Interface，GUI）程序

Qt 是纯 C++ 开发的，正常情况下需要先学习C语言、然后在学习C++然后才能使用Qt开发带界面的程序

多亏了开源社区使得**Qt 还可以用Python、Ruby、Perl 等脚本语言进行开发。**

**Qt 支持的操作系统有很多，例如通用操作系统 Windows、Linux、Unix，智能手机系统Android、iOS， 嵌入式系统等等**。可以说是跨平台的

QT官网：https://doc.qt.io/qt-5/index.html

### [2. PyQt](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/01.jieshaoyuanzhuang?id=_2-pyqt)

PyQt的开发者是英国的“Riverbank Computing”公司。它提供了GPL（简单的说，以GPL协议发布到网上的素材，你可以使用，也可以更改，但是经过你更改然后再次发布的素材必须也遵守GPL协议，主要要求是必须开源，而且不能删减原作者的声明信息等）与商业协议两种授权方式，因此它可以免费地用于自由软件的开发。

**PyQt可以运行于Microsoft Windows、Mac OS X、Linux以及Unix的多数变种上**。

PyQt是Python语言的GUI（Graphical User Interface，简称 GUI，又称图形用户接口）编程解决方案之一

可以用来代替Python内置的`Tkinter`。其它替代者还有`PyGTK`、`wxPython`等，与Qt一样，PyQt是一个自由软件

文档相关地址：https://www.riverbankcomputing.com/software/pyqt/

比较不错的参考资料：https://wiki.python.org/moin/PyQt/Tutorials

### [3. 一句话概括](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/01.jieshaoyuanzhuang?id=_3-一句话概括)

- Qt (C++ 语言 GUI )
- PyQt = Python + Qt技术

### [4. Python GUI开发热门选择](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/01.jieshaoyuanzhuang?id=_4-python-gui开发热门选择)

- Tkinter

  Python官方采用的标准库，优点是作为Python标准库、稳定、发布程序较小，缺点是控件相对较少。

- wxPython

  基于wxWidgets的Python库，优点是控件比较丰富，缺点是稳定性相对差点、文档少、用户少。

- PySide2、PyQt5

  基于Qt 的Python库，优点是控件比较丰富、跨平台体验好、文档完善、用户多。

  缺点是 库比较大，发布出来的程序比较大。

  PyQt5 的开发者是英国的“Riverbank Computing”公司 ， 而 PySide2 则是 qt 针对python语言提供的专门

  # [PyQt基本UI](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/02.ui?id=pyqt基本ui)(带界面的操作)

### `QWidget` 和 `QApplication`

在 PyQt5 库中，`QWidget` 和 `QApplication` 是两个核心类，用于构建图形用户界面 (GUI) 应用程序。它们各自有不同的功能和作用：

#### `QApplication`

- **作用**: `QApplication` 类是 PyQt5 应用程序的核心。它负责管理整个应用程序的控制流和主要设置。
- **职责**:
  - 初始化应用程序的设置，比如样式表和全局的配置。
  - 处理和管理应用程序的事件循环（事件驱动的机制，用于处理用户输入、窗口重绘等）。
  - 管理应用程序的资源，比如内存、定时器等。
  - 提供应用程序级别的功能，比如处理命令行参数和系统托盘等。
- **创建**: 通常，在创建一个 PyQt5 应用程序时，你需要先创建一个 `QApplication` 对象。这个对象必须在创建任何其他 GUI 组件之前创建。

#### `QWidget`

- **作用**: `QWidget` 类是 PyQt5 中所有用户界面对象的基类。它代表一个窗口或控件的基本元素。
- **职责**:
  - 提供基础的窗口或控件功能，比如绘制和显示。
  - 支持事件处理，比如鼠标点击和键盘输入。
  - 可以作为其他窗口或控件的容器，支持布局管理。
  - 允许创建子类来实现更复杂的窗口和控件。
- **用法**: 你通常会创建一个 `QWidget` 的子类，来实现自定义的窗口或控件。

#### 总结

- **`QApplication`**: 应用程序的主类，管理整个应用程序的生命周期和设置，是创建任何 PyQt5 应用程序的基础。
- **`QWidget`**: 所有用户界面对象的基类，代表了一个窗口或控件,提供基础的窗口或控件功能，是构建用户界面的基本元素，其他控件和窗口都继承自它。

### 关于 app = QApplication(sys.argv)

1. **初始化应用程序**:
   - `QApplication` 类是 PyQt5 应用程序的核心，用于管理应用程序的整体设置和控制流。`app = QApplication(sys.argv)` 这行代码创建了一个 `QApplication` 对象 `app`，它负责初始化应用程序所需的各种设置和资源。
2. **事件循环管理**:
   - 创建 `QApplication` 对象后，应用程序会进入事件循环（`app.exec_()`）。事件循环是应用程序的核心部分，用于处理用户输入、系统事件以及界面更新等。`QApplication` 对象管理和调度这些事件。
3. **命令行参数**:
   - `sys.argv` 是一个参数列表，用于传递命令行参数给 `QApplication` 对象。虽然在许多简单的应用程序中可能不会用到这些参数，但它们可以用于设置应用程序的行为，比如解析命令行选项。

### 关于`sys.argv`

`sys.argv` 是 Python 中 `sys` 模块提供的一个列表，用于存储命令行参数。具体来说，`sys.argv` 包含了在启动 Python 脚本时传递给脚本的所有命令行参数。

### 详细解释

1. **`sys` 模块**:
   - `sys` 是 Python 的一个标准库模块，提供了对 Python 解释器使用的一些变量和函数的访问。
2. **`sys.argv`**:
   - `sys.argv` 是一个列表，其中包含了命令行参数。
   - 列表的第一个元素 `sys.argv[0]` 是 Python 脚本的名称（或者在交互式解释器中是空字符串）。
   - 后续的元素 `sys.argv[1]`, `sys.argv[2]`, 等等，依次是传递给脚本的其他命令行参数。

## 一、第一个PyQt程序

```python
import sys
#创建了一个 QApplication 对象 app，它负责初始化应用程序所需的各种设置和资源。
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

运行上述代码的效果如下：

![image-20201119172023747](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201119172023747.png)

程序解释说明：

![image-20201119172557560](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201119172557560.png)

## 二、模块介绍

PyQt中有非常多的功能模块,开发中最常用的功能模块主要有三个:

- **QtCore**:包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用
- **QtGui**:包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类
- **QtWidgets**:包含了一些列创建桌面应用的UI元素：控件、按钮等

可以参考PyQt官网的所有模块，地址：https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index

C++具体实现的API文档，地址：https://doc.qt.io/qt-5/qtwidgets-module.html

**用到什么功能就它相关的api或者别人分享的使用心得，这是学习最快的方式**

### 流程

0.导入需要的包和模块

1. 创建一个应用程序对象`app = QApplication(sys.argv)`

2. 控件的操作：创建控件，设置控件（大小，位置，样式……），事件，信号的处理

   - 2.1创建控件：`window = QWidget()`，当我们创建一个控件之后，如果该控件无父控件，则把它作为顶层控件（窗口），系统会自动给窗口添加一些装饰（标题栏；

   - 2.2设置控件：窗口控件具备一些特性（设置标题、图标等），控件也可以作为一个容器（承载其他控件）

   - 2.3展示控件：刚创建好一个控件之后（该控件无父控件），默认不会展示该控件，只有手动调用show()

3.应用程序的执行， 进入到消息循环`sys.exit(app.exec_())`：让整个程序开始执行，并且进入到消息循环（无限循环），检测整个程序所接收到的用户的交互信息



# 窗口

## 一、分类

在Qt中，生成窗口有三种方式： `QWidget` | `QMainWindow` | `QDialog`

### 1. QWidget

控件和窗口的父类 ，自由度高（什么都东西都没有），没有划分菜单、工具栏、状态栏、主窗口 等区域

不想有状态栏、菜单栏的时候选择继承QWidget

### 2. QMainWindow

是` QWidget`的子类，包含菜单栏，工具栏，状态栏，标题栏等，中间部分则为主窗口区域

### 3. QDialog

对话框窗口的基类

## 二、QWidget

```python
import  sys

from PyQt5.QtWidgets import QWidget, QLabel , QApplication

class mywnd(QWidget):

    def __init__(self):
        super(mywnd, self).__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("这是文字内容，开始编写各种文本内容" )
        label.setStyleSheet("font-size:30px;color:red")
        label.setParent(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = mywnd()

    #设置窗口标题
     w.setWindowTitle("qwidget窗口_test")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

效果：

<img src="C:\Users\liujinfeng\Desktop\pythonLJF\PyQt5\assets\10 qwidget窗口_test.PNG" alt="10 qwidget窗口_test" style="zoom: 50%;" />

## 三、QMainWindow

```python
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("文本内容：开始编辑文字~~")
        label.setStyleSheet("font-size:30px;color:red")

        # 调用父类中的menuBar，从而对菜单栏进行操作
        menu = self.menuBar()
        # 如果是Mac的话，菜单栏不会在Window中显示而是屏幕顶部系统菜单栏位置
        # 是否按照本地系统例如Windows的那种方式在Window中显示Menu
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")
        edit_menu.addAction("剪切")

        # 设置中心内容显示
        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 设置窗口标题
    w.setWindowTitle("QMainWindow_test")
    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

效果（Mac与Windows效果稍有不同）

<img src=".\assets\11_01 QMainWindow_test.png" alt="11_01 QMainWindow_test" style="zoom:67%;" /><img src=".\assets\11_02 QMainWindow_test.png" alt="11_02 QMainWindow_test" style="zoom:67%;" />

## 四、QDialog

不过对话框一般不应该作为主窗口的存在，而是通过点击操作弹出，起到提示作用

```python
import sys

from PyQt5.QtWidgets import QDialog, QPushButton, QApplication


class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("QDialog_btn", self)
        ok_btn.setGeometry(50, 50, 100, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyDialog()
    # 设置窗口标题
    w.setWindowTitle("QDialog_test")
    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

运行效果：<img src=".\assets\12 QDialog_tes.PNG" alt="12 QDialog_tes" style="zoom:67%;" />

# 三、基本UI

窗口内的所有控件，若想在窗口中显示，都需要表示它的父亲是谁，而不能直接使用 show 函数显示

### 1. 按钮QPushButton

按钮对应的控件名称为 ` QPushButton` ， 位于 `PyQt5.QtWidgets` 里面

按钮展示在哪个控件里面，设置该控件为其setParent

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    # 创建一个 QApplication 对象 app，它负责初始化应用程序所需的各种设置和资源
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
     w.setWindowTitle("pyqt5_按钮_test")

    # 在窗口里面添加控件
    btn = QPushButton("按钮")

    # 设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    btn.setParent(w)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

运行效果：<img src=".\assets\2 pyqt5_按钮_test.PNG" alt="2 pyqt5_按钮_test" style="zoom:50%;" />



### 2. 文本QLabel

纯文本控件名称为 ` QLabel` ， 位于 `PyQt5.QtWidgets` 里面

纯文本控件仅仅作为标识显示而已，类似输入内容前的一段标签提示（账号 、密码）

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
     w.setWindowTitle("pyqt5_文本Label_test")

    # # 下面创建一个Label，然后调用方法指定父类
    # label = QLabel("账号: ", w)
    # # 设置父对象
    # label.setParent(w)

    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)

    # 显示位置与大小 ： （左上角位置）x, y , w宽, h高
    label.setGeometry(200, 200, 300, 300)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

运行效果：

<img src=".\assets\3 pyqt5_文本Label_test.PNG" alt="3 pyqt5_文本Label_test" style="zoom:50%;" />

### 3. 输入框QLineEdit

输入框的控件名称为 `QLineEdit`， 位于 `PyQt5.QtWidgets` 里面

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("pyqt5_QlineEdit_test")

    # 纯文本
    label = QLabel("账号:", w)
    label.setGeometry(20, 20, 40, 40)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(80, 30, 200, 20)

    # 在窗口里面添加控件
    btn = QPushButton("注册", w)
    btn.setGeometry(50, 80, 70, 30)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
复制Error复制成功...
```

运行效果：

![4 pyqt5_QlineEdit_test](.\assets\4 pyqt5_QlineEdit_test.PNG)

### 4. 调整窗口大小

`setGeometry` 和 `resize` 是 PyQt5 中用于设置窗口部件大小和位置的两个不同方法。它们的作用和使用场景如下：

#### 1. `setGeometry`

`setGeometry(x, y, width, height)` 方法用于设置窗口部件的位置和大小。这个方法一次性设置了窗口部件的位置和大小。

- 参数

  :

  - **`x`**: 窗口部件左上角的 x 坐标（相对于其父窗口）。
  - **`y`**: 窗口部件左上角的 y 坐标（相对于其父窗口）。
  - **`width`**: 窗口部件的宽度（单位是像素）。
  - **`height`**: 窗口部件的高度（单位是像素）。

#### 2. `resize`

`resize(width, height)` 方法仅用于设置窗口部件的大小。它不会改变窗口部件的位置，只调整其宽度和高度。

- 参数

  :

  - **`width`**: 窗口部件的宽度（单位是像素）。
  - **`height`**: 窗口部件的高度（单位是像素）。

#### 3. `move`

- **功能**: 仅调整窗口部件的位置，不改变其大小。

- 参数

  :

  - **`x`**: 新的 x 坐标（相对于父窗口的左上角）。
  - **`y`**: 新的 y 坐标（相对于父窗口的左上角）。

resize(width, height) 是 QWidget 类中的一个方法，用于设置窗口部件的大小。仅接受两个参数：宽度和高度。

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个pyqt5 test")

    # 窗口的大小--->resize(width, height) 是 QWidget 类中的一个方法，用于设置窗口部件的大小。仅接受两个参数：宽度和高度。
    w.resize(600, 600)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
复制Error复制成功...
```

运行效果：

<img src=".\assets\第一个pyqt5 test.PNG" alt="第一个pyqt5 test" style="zoom:50%;" />

### 5. 窗口显示在屏幕的中间

```python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")

    # 窗口的大小
    w.resize(300, 300)

    # 将窗口设置在屏幕的左上角
    # w.move(0, 0)

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x() #屏幕中间位置
    y = center_pointer.y() #屏幕中间位置
    # w.move(x, y)
    #屏幕中间位置需要减去控件大小窗口各一半
    # w.move(x-150, y-150)
    #自动计算方法
# frameGeometry() 是 QWidget 的一个方法，返回一个 QRect 对象，表示窗口的几何框架（即包含窗口边框、标题栏等的区域）。
#QRect 是 Qt 中表示矩形的类，包含矩形的左上角坐标（x 和 y）以及矩形的宽度和高度
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))#getRect() 是 QRect 的一个方法，返回一个四元组 (x, y, width, height)，表示矩形的左上角坐标 (x, y) 和矩形的宽度和高度
    old_x, old_y, width, height = w.frameGeometry().getRect()#控件大小窗口
    w.move(x - width / 2, y - height / 2) #屏幕中间位置需要减去控件大小窗口各一半

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
```

不在中央的样子

![image-20201119181842503](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201119181842503.png)

在中央的样子

![image-20201119182825369](https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/assets/image-20201119182825369.png)

### 6. 设置窗口icon

可以下载icon图标网站：https://www.easyicon.net/

```python
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget
    w = QWidget()
    # 设置标题
    w.setWindowTitle("看看我图标帅吗")
    # 设置图标icon---传图片地址
    w.setWindowIcon(QIcon('panda.png'))
    # 显示QWidget
    w.show()

    app.exec()
```

# 布局

在Qt里面布局分为四个大类 ：

- QBoxLayout
- QGridLayout
- QFormLayout
- QStackedLayout

## 一、QBoxLayout盒子布局

一般使用它的两个子类`QHBoxLayout` 和 `QVBoxLayout` 负责水平horizontal和垂直vertical布局

垂直布局示例：

```python
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QGroupBox, QMainWindow
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()

        # 设置大小
        self.resize(300, 300)
        # 设置标题
        self.setWindowTitle("QBoxLayout_垂直布局_test")

        # 垂直布局
        layout = QVBoxLayout()

        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零
        # 会将你放在layout中的空间压缩成默认的大小
        # 下面的比例1：1：1：2，添加一个伸缩器（理解为一个弹簧）
        layout.addStretch(1)

        # 按钮1
        btn1 = QPushButton("按钮1")
        # 添加到布局器中
        # layout.addWidget(btn1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn1)

        layout.addStretch(1)

        # 按钮2
        btn2 = QPushButton("按钮2")
        # 添加到布局器
        layout.addWidget(btn2)

        layout.addStretch(1)

        # 按钮3
        btn3 = QPushButton("按钮3")
        # 添加到布局器
        layout.addWidget(btn3)

        layout.addStretch(2)
        
        #让当前窗口使用这个排列的规则（布局器）
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget子类
    w = MyWindow()
    w.show()

    app.exec()
```

运行效果：

<img src="C:\Users\liujinfeng\Desktop\pythonLJF\PyQt5\assets\5 QBoxLayout_垂直布局_test.PNG" alt="5 QBoxLayout_垂直布局_test" style="zoom: 67%;" />

水平布局--->**注意**水平布局器与垂直布局器是可以混合使用即嵌套使用

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 最外层的垂直布局，包含两部分：爱好和性别
        container = QVBoxLayout()

        # -----创建第1个组，添加多个组件-----
        # hobby 主要是保证他们是一个组。
        hobby_box = QGroupBox("爱好")
        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        btn1=QRadioButton("听歌")
        btn2=QRadioButton("跑步")
        btn3=QRadioButton("游泳")
        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # -----创建第2个组，添加多个组件-----
        # 性别组
        gender_box = QGroupBox("性别")
        # 性别容器
        h_layout = QHBoxLayout()
        # 性别选项
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        # 追加到性别容器中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 添加到 box中
        gender_box.setLayout(h_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
     w.setWindowTitle("QBoxLayout_test")
    w.show()

    app.exec()
```

运行效果：

<img src=".\assets\6 QBoxLayout_test.PNG" alt="6 QBoxLayout_test" style="zoom: 67%;" />

## 二、QGridLayout网格布局

有的人称之为九宫格布局

#### 法一：使用字典数据

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")

        # 准备数据
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }

        # 整体垂直布局
        layout = QVBoxLayout()

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        # 把输入框添加到容器中----》添加的普通控件使用addWidget
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()

        # 循环创建追加进去
        for line_number, line_data in data.items():
            # 此时line_number是第几行，line_data是当前行的数据
            for col_number, number in enumerate(line_data):
                # 此时col_number是第几列，number是要显示的符号
                btn = QPushButton(number)
                # grid.addWidget(btn)
                grid.addWidget(btn, line_number, col_number)

        # 把网格布局追加到容器中----》添加的另一个布局器使用addLayout
        layout.addLayout(grid)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
```

运行效果：

<img src=".\assets\7 QGridLayout_计算器_test.PNG" alt="7 QGridLayout_计算器_test" style="zoom:67%;" />

#### 法二：使用列表数据

```python
# 准备数据
        data = ["7", "8", "9", "+", "(",
                "4", "5", "6", "-", ")",
                "1", "2", "3", "*", "<-",
                "0", ".", "=", "/", "C"]

        # 整体垂直布局
        layout = QVBoxLayout()


        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        # 把输入框添加到容器中----》添加的普通控件使用addWidget
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()

        # 循环创建追加进去
        positions=[(line_number,col_number) for line_number in range(4) for col_number in range(5)]
            # 此时line_number是第几行，line_data是当前行的数据
        for position, number in zip(positions, data):
                    # 此时col_number是第几列，number是要显示的符号
                btn = QPushButton(number)
                # grid.addWidget(btn)
                grid.addWidget(btn, *position)

            # 把网格布局追加到容器中----》添加的另一个布局器使用addLayout
        layout.addLayout(grid)

        self.setLayout(layout)
```

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

