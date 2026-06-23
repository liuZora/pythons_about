from PyQt5.QtCore import QFile
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from signal_slot import Ui_MainWindow
import cv2
import numpy as np


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_img)

    def open_img(self):
        # 打开文件夹
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")
        # 打开文件，返回文件路径  getOpenFileNames-打开多个文件  getSaveFileName-保存文件
        fname, ftype = QFileDialog.getOpenFileName(self, "选取文件", "./", "Jpg(*.jpg);;Png(*.png)")
        if fname:  # 判断路径为空
            img = cv2.imdecode(np.fromfile(fname, np.uint8), -1)

            h = img.shape[1]  # 获取图像大小
            w = img.shape[0]

            frame = QImage(img.data, h, w, h * 3, QImage.Format_RGB888).rgbSwapped()

            # 此处x*3最好加上，否则图片会出现倾斜
            pix = QPixmap.fromImage(frame)

            self.label_4.setPixmap(pix)
            # 自适应大小
            self.label_4.setScaledContents(True)

        # self.label_4.


if __name__ == '__main__':
    # 创建对象初始化，提供图形界面的底层管理功能
    app = QApplication([])

    # 创建主窗口
    mainwindow = MyWindow()
    # 显示窗口
    mainwindow.show()

    # 进入事件主循环，接收用户输入事件
    app.exec_()
