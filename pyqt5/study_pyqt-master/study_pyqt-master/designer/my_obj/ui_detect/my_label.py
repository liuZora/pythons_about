from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLabel
import sys

sys.path.append("designer.my_obj.ui_detect")


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.img = None
        self.scaled_img = None
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.wheel_flag = False

        self.scale = 1
        self.old_scale = 1
        self.point = QPoint(0, 0)
        self.x = -1
        self.y = -1
        self.img_height = -1
        self.img_width = -1

    def init_ui(self):
        self.setWindowTitle("MyLabel")

    def clear_image(self):
        self.setPixmap(QPixmap(""))

    def set_image(self, piximg):
        self.img = piximg
        if piximg:
            width, height = self.img.width(), self.img.height()
            label_w = self.size().width()
            label_h = self.size().height()
            self.scaled_img = self.img.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio)

            new_width, new_height = self.scaled_img.width(), self.scaled_img.height()
            self.img_height = height
            self.img_width = width
            self.scale = min(new_width / width, new_height / height)
            self.first_scale = self.scale
            # 刚开始原图就缩放了，所以需要把比例也计算到图上
            self.point = QPoint(int((label_w - new_width) * 0.5 / self.scale),
                                int((label_h - new_height) * 0.5 / self.scale))

        # 相当于刷新一下
        self.setPixmap(QPixmap(""))

    def paintEvent(self, e):
        if self.img:
            painter = QPainter()
            painter.begin(self)
            painter.scale(self.scale, self.scale)
            if self.wheel_flag:  # 定点缩放
                self.wheel_flag = False
                # 判断当前鼠标pos在不在图上
                # 计算图片左上角实际在画布的位置
                this_left_x = self.point.x() * self.old_scale
                this_left_y = self.point.y() * self.old_scale
                # 现在图像的宽高
                this_scale_width = self.img_width * self.old_scale
                this_scale_height = self.img_height * self.old_scale

                # 鼠标点在图上，以鼠标点为中心动作
                gap_x = self.x - this_left_x
                gap_y = self.y - this_left_y
                if 0 < gap_x < this_scale_width and 0 < gap_y < this_scale_height:
                    new_left_x = int(self.x / self.scale - gap_x / self.old_scale)
                    new_left_y = int(self.y / self.scale - gap_y / self.old_scale)
                    self.point = QPoint(new_left_x, new_left_y)
                # 鼠标点不在图上，固定左上角进行缩放
                else:
                    true_left_x = int(self.point.x() * self.old_scale / self.scale)
                    true_left_y = int(self.point.y() * self.old_scale / self.scale)
                    self.point = QPoint(true_left_x, true_left_y)
            # 在原图缩放
            painter.drawPixmap(self.point, self.img)
            painter.end()

    def wheelEvent(self, event):
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()
        self.old_scale = self.scale
        self.x, self.y = event.x(), event.y()
        self.wheel_flag = True
        # 获取当前鼠标相对于view的位置
        if angleY > 0:
            self.scale *= 1.08
        else:  # 滚轮下滚
            self.scale *= 0.92
        # 缩放比例小于原始缩放比例的0.3倍，就不能在缩小了
        if self.scale < self.first_scale * 0.3:
            self.scale = self.first_scale * 0.3
        self.update()

    # 鼠标移动
    def mouseMoveEvent(self, e):
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos  # 当前位置-起始位置=差值
            self.point = self.point + self.end_pos / self.scale  # 左上角的距离变化
            self.start_pos = e.pos()
            self.repaint()

    # 鼠标按下
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    # 鼠标松开
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
