# QApplication命令程序，QMainWindow窗口，QPushButton按钮，QPlainTextEdit文本编辑
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QFormLayout
from PyQt5.QtWidgets import QGroupBox,QRadioButton,QStackedLayout
from PyQt5.QtCore import Qt
import pandas as pd
import re


class Demo():
    def __init__(self):
        # 定义主窗口
        self.window = QWidget()
        # 主窗口大小
        self.window.resize(300, 200)

        # 水平垂直布局
        # self.init_qvh_ui()

        # 表单布局
        self.init_form_ui()


    def init_qvh_ui(self):
        # 垂直布局
        layout = QVBoxLayout()

        "======第一个组========="
        # 创建一个组
        hobby_box = QGroupBox("爱好")
        # 组内的空间垂直排列
        v_layout = QVBoxLayout()
        self.button_v1 = QRadioButton("抽烟")
        self.button_v2 = QRadioButton("喝酒")
        self.button_v3 = QRadioButton("烫头")
        # 按钮给了布局期后只由布局期控制
        v_layout.addWidget(self.button_v1)
        v_layout.addWidget(self.button_v2)
        v_layout.addWidget(self.button_v3)
        # 调整布局空间
        # v_layout.addStretch()
        # 当前组使用此布局
        hobby_box.setLayout(v_layout)

        "======第二个组========="
        # 创建一个组
        sex_box = QGroupBox("性别")
        # 组内的空间水平排列
        h_layout = QHBoxLayout()
        self.button_h1 = QRadioButton("男")
        self.button_h2 = QRadioButton("女")
        # 按钮给了布局期后只由布局期控制
        h_layout.addWidget(self.button_h1)
        h_layout.addWidget(self.button_h2)
        # 调整布局空间
        # v_layout.addStretch()
        # 当前组使用此布局
        sex_box.setLayout(h_layout)

        # 把爱好组添加到最外层布局器里
        layout.addWidget(hobby_box)
        layout.addWidget(sex_box)

        # 让当前窗口使用此布局
        self.window.setLayout(layout)

    def init_form_ui(self):
        # 窗口不可以改变大小
        self.window.setFixedSize(300,200)

        # 垂直布局
        layout = QVBoxLayout()

        # 表单布局
        form_layout = QFormLayout()

        # 创建输入框
        edit1 = QLineEdit()
        edit1.setPlaceholderText("请输入账号")
        form_layout.addRow("账号:",edit1)

        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        form_layout.addRow("密码:", edit2)

        # 子布局添加到父布局
        layout.addLayout(form_layout)

        button = QPushButton("登录")

        # 按钮居中对其  AlignHCenter水平居中  AlignRight右对齐  AlignLeft左对齐
        layout.addWidget(button,alignment=Qt.AlignCenter)

        self.window.setLayout(layout)


    def do(self):
        pass

if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.window.show()

    app.exec_()