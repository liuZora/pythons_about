# QApplication命令程序，QMainWindow窗口，QPushButton按钮，QPlainTextEdit文本编辑
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QDesktopWidget,QVBoxLayout
import pandas as pd
import re


class Demo():
    def __init__(self):
        # 定义主窗口
        self.window = QMainWindow()
        # 主窗口大小
        self.window.resize(300, 200)

        # 将窗口显示在屏幕中间
        # 获取屏幕中心点
        center_point = QDesktopWidget().availableGeometry().center()
        x = center_point.x()
        y = center_point.y()
        # 获取窗口位置和大小
        old_x, old_y, width, hight = self.window.frameGeometry().getRect()
        # 移动到相对于父窗口中心的位置，在显示器相对左上角的位置
        self.window.move(x - width // 2, y - hight // 2)
        # 窗口标题栏
        self.window.setWindowTitle("demo")

        # 父窗口定义纯文本
        self.label = QLabel("账号：", self.window)
        self.label.setGeometry(20, 30, 30, 20)
        # self.label.move(20, 20)

        self.text = QLineEdit(self.window)
        self.text.setPlaceholderText("请输入账号")
        # self.text.move(60, 20)
        # 设置窗口属性，x,y,w,h
        self.text.setGeometry(60, 30, 200, 20)

        self.button = QPushButton("注册", self.window)
        self.button.setGeometry(120, 90, 70, 30)



    def do(self):
        pass


if __name__ == '__main__':
    app = QApplication([])

    demo = Demo()
    demo.window.show()

    app.exec_()
