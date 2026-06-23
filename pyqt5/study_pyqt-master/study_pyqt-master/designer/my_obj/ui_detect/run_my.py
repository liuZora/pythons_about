from PyQt5.QtCore import QStringListModel, Qt, QEvent, QPoint
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from my_object import Ui_MainWindow
import cv2
import numpy as np
import os
import re


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.detect = None  # 模型
        self.img = None  # 图像
        self.img_out = None  # 模型输出的图
        self.detect_num = 0  # 被检测保存到文件夹的图片数量
        self.detect_once = True  # 单张检测（默认）
        self.detect_all = True  # false停止检测
        self.lock_tools = True  # 默认锁定工具栏

        self.init_ui()

        # 选中下拉框传递下拉框的字符
        self.comboBox.activated[str].connect(self.init_model)
        # 检测图像
        self.toolButton_3.clicked.connect(self.detect_img)

        # 保存结果
        self.pushButton_3.clicked.connect(self.save_img)
        self.action_7.triggered.connect(self.save_img)

        # 单张模式和全部模式
        self.radioButton.toggled.connect(self.detect_mode)
        # 停止全部检测
        self.toolButton_4.clicked.connect(self.detect_stop)

    def init_ui(self):  # 初始化ui
        self.setupUi(self)
        # 打开文件夹
        self.actiondaka.triggered.connect(self.open_file)
        self.action.triggered.connect(self.open_files)

        # 选择图像
        self.listView.doubleClicked.connect(self.show_img)
        self.listView.clicked.connect(self.show_img)
        # 下一张和上一张
        self.toolButton.clicked.connect(self.last_img)
        self.toolButton_2.clicked.connect(self.next_img)

        # 只要改变文本就进行一次搜索，找到符合当前输入的所有文件
        self.lineEdit.textChanged.connect(self.get_text)

        # 恢复缩放的label和label_2图像
        self.pushButton.clicked.connect(self.renew_show_img)
        self.pushButton.clicked.connect(self.show_out_img)

        # 过滤器监控label窗口的触发
        self.label.installEventFilter(self)
        self.label_2.installEventFilter(self)

    def open_file(self):
        # 打开多个文件
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")
        # 打开文件，返回文件路径  getOpenFileNames-打开多个文件  getSaveFileName-保存文件
        global path_list
        path_list, ftype = QFileDialog.getOpenFileNames(self, "选取文件", "./", "图片类型 (*.png *.jpg *.bmp)")

        global show_path_list
        show_path_list = path_list

        self.show_listview(show_path_list)

    def open_files(self):
        # 打开文件夹
        global path_list
        path_list = []
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        if directory1:  # 有路径在操作
            for img_name in os.listdir(directory1):
                if img_name.split(".")[-1] not in ["jpg", "png", "bmp"]:
                    continue
                img_path = os.path.join(directory1, img_name)
                path_list.append(img_path)

            global show_path_list
            show_path_list = path_list

            self.show_listview(show_path_list)

    # 显示路径列表并添加复选框
    def show_listview(self, show_path_list):
        self.model = QStandardItemModel()
        for line in show_path_list:
            # 设置数据模式
            self.item = QStandardItem(line)
            # 不可以操作
            self.item.setCheckable(False)

            img_name = os.path.basename(line)
            save_dir = os.path.join(os.path.dirname(line), "out_image")
            save_path = os.path.join(save_dir, img_name.split(".")[0] + "_out.jpg")
            # 路径有输出结果图
            if os.path.exists(save_path):
                self.detect_num += 1
                self.item.setCheckState(Qt.Checked)
            else:
                # 设置未选中  选中：Qt.Checked
                self.item.setCheckState(Qt.Unchecked)
            # 一行信息加入model
            self.model.appendRow(self.item)
        self.listView.setModel(self.model)
        self.init_open_img()
        self.label_4.setText(fr"检测数量： {self.detect_num}/{len(path_list)}")

        # self.slm = QStringListModel()
        # self.slm.setStringList(show_path_list)
        # self.listView.setModel(self.slm)
        # self.init_open_img()

    def init_model(self, text):
        del self.detect

        if text == "Open_my":
            from model.side_img_crop import unet_onnx
            classes_list = ["background", "up", "down", "suilie"]  # 6个关键点
            onnx_path = r"model/weight/u2net_p_20220928.onnx"

            # 面积筛选去掉小的  # d_thresh 偏移量阈值像素值
            self.detect = unet_onnx(onnx_path, classes_list, draw_box=False, contour_area=800, d_thresh=20)
            self.textEdit.setText(f"模型加载成功：{text}")
        else:
            self.detect = None
            self.textEdit.setText(f"没有{text}模型可加载...")


    def detect_img(self):
        if np.array(self.img).all() and self.detect:
            if self.detect_once:  # 单张检测
                result, classes_list_out, self.img_out = self.detect.detect(self.img)
                self.show_out_img()
                self.textEdit.setText(f"图像路径：{os.path.basename(self.img_path)} \n结果：{result} \n类别：{classes_list_out}")
            else:  # 全部检测
                self.detect_all_img()

    # 检测所有图像
    def detect_all_img(self):
        save_dir = os.path.join(os.path.dirname(path_list[0]), "out_image")
        # 没有路径就创建
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for index, img_path in enumerate(path_list):
            img_name = os.path.basename(img_path)
            save_path = os.path.join(save_dir, img_name.split(".")[0] + "_out.jpg")
            if not self.detect_all:  # False停止检测
                break  # 结束当前循环
            # 路径没有输出结果图
            if not os.path.exists(save_path):
                img = cv2.imdecode(np.fromfile(img_path, np.uint8), -1)
                result, classes_list_out, img_out = self.detect.detect(img)
                # 保存
                cv2.imencode(".jpg", img_out)[1].tofile(save_path)

                qModelIndex = self.listView.model().index(index, 0)  # 获取行对象
                item = self.model.itemFromIndex(qModelIndex)
                # 设置被勾选
                item.setCheckState(Qt.Checked)

                # 更新检测数量
                self.detect_num += 1
                self.label_4.setText(fr"检测数量： {self.detect_num}/{len(path_list)}")

                # 实时刷新窗口
                QApplication.processEvents()

    def detect_stop(self):
        self.detect_all = False

    def detect_mode(self):
        if self.radioButton.isChecked():
            self.detect_once = True  # 单张检测（默认）
            # 设置开启自动保存选项
            self.checkBox.setChecked(False)
        else:
            self.detect_once = False  # 全部检测
            # 设置开启自动保存选项
            self.checkBox.setChecked(True)

    # 保存输出图
    def save_img(self):
        if np.array(self.img_out).all() != None:
            img_path = self.img_path
            img_name = os.path.basename(img_path)
            save_dir = os.path.join(os.path.dirname(img_path), "out_image")

            # 没有路径就创建
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, img_name.split(".")[0] + "_out.jpg")
            # 保存
            cv2.imencode(".jpg", self.img_out)[1].tofile(save_path)
            self.textEdit.append("图像保存成功...")

            # 设置保存图像为勾选状态
            qModelIndex = self.listView.currentIndex()  # 选中的对象
            item = self.model.itemFromIndex(qModelIndex)
            # 设置被勾选
            item.setCheckState(Qt.Checked)

            # 更新检测数量
            self.detect_num += 1
            self.label_4.setText(fr"检测数量： {self.detect_num}/{len(path_list)}")

    # 显示输出图
    def show_out_img(self):
        open_out = False  # 是不是打开路径的输出图
        # 没有输出图且有原图，打开路径图片，还没有就显示空界面
        if np.array(self.img_out).all() == None and np.array(self.img).all() != None:
            # 显示已经保存过的输出图
            img_name = os.path.basename(self.img_path)
            save_dir = os.path.join(os.path.dirname(self.img_path), "out_image")
            # 没有路径就创建
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            save_path = os.path.join(save_dir, img_name.split(".")[0] + "_out.jpg")
            # 打开路径图
            if os.path.exists(save_path):
                open_out = True
                self.img_out = cv2.imdecode(np.fromfile(save_path, np.uint8), -1)
            # 没有路径图显示空
            else:
                self.label_2.set_image(None)
                self.textEdit.clear()
                self.img_out = None
        # 有输出图显示输出
        if np.array(self.img_out).all() != None:
            h = self.img_out.shape[1]  # 获取图像大小
            w = self.img_out.shape[0]
            frame = QImage(self.img_out.data, h, w, h * 3, QImage.Format_RGB888).rgbSwapped()
            # 此处x*3最好加上，否则图片会出现倾斜
            pix_out = QPixmap.fromImage(frame)
            self.label_2.set_image(pix_out)

            # 选择自动保存 并且 没有打开路径输出图
            if self.checkBox.isChecked() and not open_out:
                self.save_img()

    def show_img(self, qModelIndex):
        # 显示第几张图像
        index = qModelIndex.row() + 1
        len_img = len(show_path_list)
        if len_img == 0:  # 没有符合搜索的图像，不显示
            self.label_3.setText(f"文件列表： {0}/{len_img}")
            self.label.set_image(None)
        else:
            self.label_3.setText(f"文件列表： {index}/{len_img}")
            self.img_path = show_path_list[qModelIndex.row()]
            if self.img_path:  # 判断路径为空
                self.img = cv2.imdecode(np.fromfile(self.img_path, np.uint8), -1)

                h = self.img.shape[1]  # 获取图像大小
                w = self.img.shape[0]

                frame = QImage(self.img.data, h, w, h * 3, QImage.Format_RGB888).rgbSwapped()
                # 此处x*3最好加上，否则图片会出现倾斜
                piximg = QPixmap.fromImage(frame)
                self.label.set_image(piximg)

        # 更新输出图
        self.img_out = None
        self.show_out_img()

    # 窗口图片恢复大小
    def renew_show_img(self):
        # 有图像再操作
        if np.array(self.img).all() != None:
            h = self.img.shape[1]  # 获取图像大小
            w = self.img.shape[0]
            frame = QImage(self.img.data, h, w, h * 3, QImage.Format_RGB888).rgbSwapped()

            # 此处x*3最好加上，否则图片会出现倾斜
            piximg = QPixmap.fromImage(frame)
            self.label.set_image(piximg)

    # 打开文件夹载入默认显示第一张
    def init_open_img(self):
        # 获取第一个对象,0行0列
        # modelindex = self.listView.model().index(0)
        modelindex = self.listView.model().index(0, 0)
        # 选中行
        self.listView.setCurrentIndex(modelindex)
        # 获取现在选中的对象
        qModelIndex = self.listView.currentIndex()
        # 显示图像
        self.show_img(qModelIndex)

    def last_img(self):
        # 有图像再操作
        if np.array(self.img).all() != None:
            # 获取现在选中的对象
            qModelIndex = self.listView.currentIndex()
            # 拿到索引
            row = qModelIndex.row()
            if row == 0:
                row = 1
            # 获取当前的上一个对象
            modelindex = self.listView.model().index(row - 1, 0)

            self.listView.setCurrentIndex(modelindex)
            qModelIndex = self.listView.currentIndex()
            self.show_img(qModelIndex)

    def next_img(self):
        # 有图像再操作
        if np.array(self.img).all() != None:
            # 获取现在选中的对象
            qModelIndex = self.listView.currentIndex()
            # 拿到索引
            row = qModelIndex.row()
            # 最后一张无下一张
            if row == len(show_path_list) - 1:
                row = len(show_path_list) - 2
            # 获取当前的下一个对象
            # modelindex = self.listView.model().index(row + 1, 0)
            modelindex = self.listView.model().index(row + 1, 0)
            self.listView.setCurrentIndex(modelindex)
            qModelIndex = self.listView.currentIndex()
            self.show_img(qModelIndex)

    # 搜索
    def get_text(self):
        # 获取输入的搜索字符
        input = self.lineEdit.text()
        if len(input) != 0:
            new_text_path = []
            for img_path in path_list:
                img_name = os.path.basename(img_path)
                result = re.findall(input, img_name)
                if len(result) != 0:  # 符合搜索条件的文件
                    new_text_path.append(img_path)
        else:
            new_text_path = path_list
        global show_path_list
        show_path_list = new_text_path

        self.show_listview(show_path_list)

    # 接受过滤器的触发事件
    def eventFilter(self, obj, event):
        if obj == self.label or obj == self.label_2:
            # 鼠标事件
            if event.type() == QEvent.MouseButtonPress:
                self.mousePressEvent_label(event)
        #     # 滚轮事件
        #     if event.type() == QEvent.Wheel:
        #         self.wheelEvent_label(event)
        #
        return False

    # label的鼠标事件处理
    def mousePressEvent_label(self, event):
        # 左键按下
        if event.buttons() == Qt.LeftButton:
            # 聚焦到文件列表
            self.listView.setFocus()

    def wheelEvent_label(self, event):
        # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angle = event.angleDelta() / 8
        angleX = angle.x()  # 水平滚过的距离(此处用不上)
        angleY = angle.y()  # 竖直滚过的距离
        scale = 0.1  # 滚轮的缩放比例

        if angleY > 0:  # 滚轮上滚
            print("滚轮上滚")
            self.scaledimg = self.piximg.scaled(self.scaledimg.width() * (1 + scale),
                                                self.scaledimg.height() * (1 + scale))
            newWidth = event.x() - (self.scaledimg.width() * (event.x() - self.singleOffset.x())) \
                       / (self.scaledimg.width() * (1 - scale))
            newHeight = event.y() - (self.scaledimg.height() * (event.y() - self.singleOffset.y())) \
                        / (self.scaledimg.height() * (1 - scale))
            self.singleOffset = QPoint(newWidth, newHeight)  # 更新偏移量
            self.label.setPixmap(self.scaledimg)
            # self.label.repaint()  # 重绘
        else:
            print("鼠标中键下滚")  # 响应测试语句
            self.scaledimg = self.piximg.scaled(self.scaledimg.width() * (1 - scale),
                                                self.scaledimg.height() * (1 - scale))
            newWidth = event.x() - (self.scaledimg.width() * (event.x() - self.singleOffset.x())) \
                       / (self.scaledimg.width() * (1 + scale))
            newHeight = event.y() - (self.scaledimg.height() * (event.y() - self.singleOffset.y())) \
                        / (self.scaledimg.height() * (1 + scale))
            self.singleOffset = QPoint(newWidth, newHeight)  # 更新偏移量
            self.label.setPixmap(self.scaledimg)


if __name__ == '__main__':
    import sys

    # 创建对象初始化，提供图形界面的底层管理功能
    app = QApplication([])

    # 创建主窗口
    mainwindow = MyWindow()
    # 显示窗口
    mainwindow.show()

    # 进入事件主循环，接收用户输入事件
    sys.exit(app.exec_())
