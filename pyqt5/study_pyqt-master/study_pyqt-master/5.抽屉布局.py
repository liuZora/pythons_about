# QApplication命令程序，QMainWindow窗口，QPushButton按钮，QPlainTextEdit文本编辑
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow, QPushButton, QPlainTextEdit, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QFormLayout
from PyQt5.QtWidgets import QGroupBox,QRadioButton,QStackedLayout
from PyQt5.QtCore import Qt
import pandas as pd
import re

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        # self.window1 = QWidget()
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("输入框1")

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        # self.window2 = QWidget()
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("输入框2")

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        # self.window = QWidget()

        # 初始化两个抽屉页面
        self.layout = self.stack_layout()
        self.init_ui()

    def stack_layout(self):
        layout = QStackedLayout()

        # 创建两个页面
        win1 = Window1()
        win2 = Window2()

        layout.addWidget(win1)
        layout.addWidget(win2)

        return layout

    def init_ui(self):
        self.setFixedSize(300,270)

        layout = QVBoxLayout()

        # 定义一个页面
        widget = QWidget()
        widget.setLayout(self.layout)

        button1 = QPushButton("页面1")
        button2 = QPushButton("页面2")

        # 给按钮添加事件，使用匿名函数或重新定义函数才能运行
        button1.clicked.connect(lambda:self.layout.setCurrentIndex(0))
        button2.clicked.connect(lambda:self.layout.setCurrentIndex(1))

        layout.addWidget(widget)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])

    mywindow = MyWindow()
    mywindow.show()

    app.exec_()




