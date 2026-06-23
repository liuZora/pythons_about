from Layout import Ui_Form
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # 创建对象初始化，提供图形界面的底层管理功能
    app = QApplication([])

    # 创建主窗口
    mainWindow = QWidget()
    # ui控件
    ui = Ui_Form()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    # 显示窗口
    mainWindow.show()

    # 进入事件主循环，接收用户输入事件
    app.exec_()