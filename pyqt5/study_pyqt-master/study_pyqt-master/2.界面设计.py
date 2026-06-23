from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic
import pandas as pd
import re


class Stats:
    def __init__(self):
        # 从文件加载ui，动态创建窗口对象
        self.ui = uic.loadUi(r"./designer/stats.ui_detect")
        print(self.ui.__dict__)  # 获取对象的属性字典

        # 绑定按钮的信号和槽
        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()
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

        # 弹出窗口显示结果
        QMessageBox.about(self.ui, '统计结果', f'''薪资20000以上的有：\n{name1}\n\n\n薪资20000以下的有：\n{name2}''')


if __name__ == '__main__':
    app = QApplication([])  # 初始化，提供图形界面的底层管理功能

    stats = Stats()
    stats.ui.show()  # 主窗口全部显示

    app.exec_()  # 进入事件循环，接收用户输入事件
