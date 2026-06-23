# QApplication命令程序，QMainWindow窗口，QPushButton按钮，QPlainTextEdit文本编辑
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


class Stats(QMainWindow):
    def __init__(self):
        super(Stats, self).__init__()
        # self.window = QWidget()
        # 设置主窗口工作区大小，不加菜单栏边框
        self.resize(500, 400)
        # 移动到相对于父窗口位置，在显示器相对左上角的位置
        self.move(300, 310)
        # 窗口标题栏
        self.setWindowTitle("薪酬统计")

        # 文本框控件类  实例化时有一个父控件对象window
        self.textEdit = QPlainTextEdit(self)
        # 提示文本
        self.textEdit.setPlaceholderText("请输入薪酬表")
        # move是控件显示像素相对父窗口左上角位置
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        # 定义一个按钮，继承父窗口
        self.button = QPushButton("统计", self)
        self.button.move(380, 80)

        self.button1 = QPushButton("退出应用", self)
        self.button1.move(380, 120)

        # button的点击信号(signal)连到handleCalc函数的槽(slot)里
        self.button.clicked.connect(self.handleCalc)

        self.button1.clicked.connect(self.close_window)

    # 处理点按信号函数，叫做槽(slot)
    def handleCalc(self):
        info = self.textEdit.toPlainText()
        # 弹出窗口显示结果
        QMessageBox.about(self, '结果', "输入完成")

    # 自定义的槽，退出程序
    def close_window(self):
        # 查看信号由哪个控件发出
        # sender = self.window.sender()
        # print(sender.text())
        # 获取对象的指针
        app = QApplication.instance()
        # 退出程序
        app.quit()

if __name__ == '__main__':
    # 创建对象初始化，提供图形界面的底层管理功能
    app = QApplication([])
    # 设置图标，后缀为ico
    app.setWindowIcon(QIcon("./ico_data/Mario.ico"))

    stats = Stats()
    # 显示主窗口
    stats.show()

    # 进入事件循环，接收用户输入事件
    app.exec_()
