import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ListViewDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.imgName = []
        self.resize(400, 350)
        HLayout = QHBoxLayout()
        VLayout = QVBoxLayout()
        self.lab1 = QLabel()
        self.lab1.setPixmap(QPixmap("./images/python.jpg"))
        HLayout.addWidget(self.lab1)
        self.listView = QListView()
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单
        self.listView.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)

        self.selectbtn = QPushButton("选择图片")
        self.btnOK = QPushButton("开始检测")
        groupBox = QGroupBox("是否使用GPU")
        self.checkBox1 = QCheckBox("&Yes")
        self.checkBox1.setChecked(False)
        self.checkBox1.stateChanged.connect(lambda: self.btnstate(self.checkBox1))

        layout = QHBoxLayout()  # 复选框单独用了一个水平布局
        layout.addWidget(self.checkBox1)
        groupBox.setLayout(layout)

        VLayout.addWidget(self.btnOK)
        VLayout.addWidget(self.selectbtn)
        VLayout.addWidget(groupBox)
        VLayout.addWidget(self.listView)

        bar = self.menuBar()
        file = bar.addMenu("File")
        edit = bar.addMenu("Edit")
        file.addAction("Open")
        file.addAction("Save")
        file.addAction("Close")
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        HLayout.addLayout(VLayout)
        main_frame = QWidget()
        main_frame.setLayout(HLayout)

        self.setWindowTitle("行人检测系统")
        self.selectbtn.clicked.connect(self.openimage)
        self.listView.doubleClicked.connect(self.clicked)
        self.listView.clicked.connect(self.clicked)
        self.btnOK.clicked.connect(self.processimage)
        self.setCentralWidget(main_frame)

    def rightMenuShow(self):
        rightMenu = QtWidgets.QMenu(self.listView)
        removeAction = QtWidgets.QAction(u"Delete", self, triggered=self.removeimage)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
        rightMenu.addAction(removeAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    def processTrigger(self, q):
        if (q.text() == "show"):
            self.statusBar.showMessage(q.text() + " 菜单选项被点击了", 5000)

    def btnstate(self, btn):
        chk1Status = self.checkBox1.isChecked()
        print(chk1Status)
        if chk1Status:
            QMessageBox.information(self, "Tips", "使用GPU!", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "Tips", "不使用GPU!")

    def clicked(self, qModelIndex):
        # QMessageBox.information(self, "QListView", "你选择了: "+ imgName[qModelIndex.row()])
        global path
        self.lab1.setPixmap(QPixmap(imgName[qModelIndex.row()]))
        path = imgName[qModelIndex.row()]

    def openimage(self):
        global imgName
        imgName, imgType = QtWidgets.QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
        slm = QStringListModel()
        slm.setStringList(imgName)
        self.listView.setModel(slm)

    def removeimage(self):
        selected = self.listView.selectedIndexes()
        itemmodel = self.listView.model()
        for i in selected:
            itemmodel.removeRow(i.row())

    def processimage(self):
        QMessageBox.information(self, "Tips", "Done!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())