from PyQt5 import QtCore, QtDesigner
from PyQt5.QtWidgets import *

# 下面这个是自己qt design随便绘制一个ui文件，这个只是一个实例引用
from ui_control_form import Control_Param_Form

def dump_ui(widget, path):
    builder = QtDesigner.QFormBuilder()
    stream = QtCore.QFile(path)
    stream.open(QtCore.QIODevice.WriteOnly)
    builder.save(stream, widget)
    stream.close()

app = QApplication([''])

dialog = QDialog()
Control_Param_Form().setupUi(dialog)

dialog.show()

dump_ui(dialog, 'myui.ui')