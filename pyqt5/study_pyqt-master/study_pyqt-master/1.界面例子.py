# QApplication命令程序，QMainWindow窗口，QPushButton按钮，QPlainTextEdit文本编辑
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
import pandas as pd
import re


class Stats():
    def __init__(self):
        # 定义主窗口
        self.window = QMainWindow()
        # self.window = QWidget()
        # 设置主窗口工作区大小，不加菜单栏边框
        self.window.resize(500, 400)
        # 移动到相对于父窗口位置，在显示器相对左上角的位置
        self.window.move(300, 310)
        # 窗口标题栏
        self.window.setWindowTitle("薪酬统计")

        # 文本框控件类  实例化时有一个父控件对象window
        self.textEdit = QPlainTextEdit(self.window)
        # 提示文本
        self.textEdit.setPlaceholderText("请输入薪酬表")
        # move是控件显示像素相对父窗口左上角位置
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        # 定义一个按钮，继承父窗口
        self.button = QPushButton("统计", self.window)
        self.button.move(380, 80)

        self.button1 = QPushButton("退出应用", self.window)
        self.button1.move(380, 120)

        # button的点击信号(signal)连到handleCalc函数的槽(slot)里
        self.button.clicked.connect(self.handleCalc)

        self.button1.clicked.connect(self.close_window)

    # 处理点按信号函数，叫做槽(slot)
    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 统计输入数据
        messas = []
        regex = re.compile('\s+')  # 正则化匹配空格
        for line in info.splitlines():
            messa = regex.split(line)  # 切割字符串
            messa = [messa[0], float(messa[1]), int(messa[2])]
            messas.append(messa)
        df = pd.DataFrame(messas, columns=["姓名", "薪资", "年龄"])
        df = df.sort_values(by=["薪资"], ascending=False)  # 根据第一列降序排列
        df1 = df[df["薪资"] > 20000]
        df2 = df[df["薪资"] <= 20000]
        name1 = df1["姓名"].to_string(index=False)  # 将姓名一列去掉索引转换为字符串输出
        name2 = df2["姓名"].to_string(index=False)

        # 弹出窗口显示结果,弹出框名字，弹出框内容
        QMessageBox.about(self.window, '统计结果', f'''薪资20000以上的有：\n{name1}\n\n\n薪资20000以下的有：\n{name2}''')

    # 自定义的槽
    def close_window(self):
        # 查看信号由哪个控件发出
        # sender = self.window.sender()
        # print(sender.text())
        # 获取对象的指针
        app = QApplication.instance()
        # 退出程序
        app.quit()


""""
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35
"""

if __name__ == '__main__':
    # 创建对象初始化，提供图形界面的底层管理功能
    app = QApplication([])
    # 设置图标，后缀为ico
    app.setWindowIcon(QIcon("./ico_data/Mario.ico"))

    stats = Stats()
    # 显示主窗口
    stats.window.show()

    # 进入事件循环，接收用户输入事件
    app.exec_()
