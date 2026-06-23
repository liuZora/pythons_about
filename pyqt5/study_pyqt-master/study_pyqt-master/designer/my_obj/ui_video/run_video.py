# 基于pyqt5
import os
import sys

from PyQt5.QtCore import QDateTime, QUrl
from PyQt5.QtMultimedia import QAudioOutput, QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QSlider

from video import Ui_MainWindow


class Video_win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Video_win, self).__init__()
        self.setupUi(self)
        # self.audio = QAudioOutput()  #pyside6中要单独实例音频
        self.player = QMediaPlayer()
        # self.player.setAudioOutput(self.audio)  # 读取输出音频设备
        self.player.setVideoOutput(self.videoout)
        # 播放列表
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)
        # 当前播放的进度，显示调整视频进度条
        self.timeSlider.setValue(0)
        self.timeSlider.setMinimum(0)
        self.player.positionChanged.connect(self.get_time)
        self.timeSlider.sliderPressed.connect(self.player.pause)
        self.timeSlider.sliderMoved.connect(self.change_time)
        self.timeSlider.sliderReleased.connect(self.player.play)
        # 当前播放音量
        self.volumeSlider.setValue(50)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)  # 刻度位置
        self.volumeSlider.valueChanged.connect(self.change_volume)  # 修改音量
        # 打开文件
        self.actionfiles.triggered.connect(self.open_file)
        # 打开文件夹
        self.actiondirs.triggered.connect(self.open_dir)
        # 通过列表切换视频
        self.listvidename.itemClicked.connect(self.change_by_list)
        # 快进
        self.right_button.clicked.connect(self.up_time)
        # play
        self.play_button.clicked.connect(self.player.play)
        # pause
        self.mid_button.clicked.connect(self.player.pause)
        # 快退
        self.left_button.clicked.connect(self.down_time)
        # 下一部
        self.actionnext.triggered.connect(self.next_video)
        # 上一部
        self.actionprevious.triggered.connect(self.previous_video)
        # 默认设置顺序循环播放
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        # 改变播放顺序
        self.playlistBox.activated.connect(self.change_PlayBackMode)

    # 切换播放模式
    def change_PlayBackMode(self, num):
        self.actionnext.setEnabled(True)
        if num == 0:
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)  # 顺序循环播放
        if num == 1:
            self.playlist.setPlaybackMode(QMediaPlaylist.Random)  # 随机播放
        if num == 2:
            self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)  # 当前视频循环播放
            self.actionnext.setDisabled(True)

    # 下一部
    def next_video(self):
        self.playlist.next()
        num = self.playlist.currentIndex()
        self.listvidename.setCurrentRow(num)
        # self.player.play()

    # 上一部
    def previous_video(self):
        self.playlist.previous()
        num = self.playlist.currentIndex()
        self.listvidename.setCurrentRow(num)
        self.player.play()

    # 选取文件
    def open_file(self):
        urls = QFileDialog.getOpenFileUrls()[0]
        for url in urls:
            yu = url.toString()
            drv, left = os.path.split(yu)
            self.listvidename.addItem(left)

            content = QMediaContent(url)
            self.playlist.addMedia(content)
        num = self.playlist.mediaCount() - len(urls)
        self.playlist.setCurrentIndex(num)
        self.listvidename.setCurrentRow(num)
        self.player.play()

    # 选取文件夹
    def open_dir(self):
        dir = QFileDialog.getExistingDirectory()
        files = os.listdir(dir)
        for file in files:
            self.listvidename.addItem(file)
            url = os.path.join(dir, file)
            Qurl = QUrl.fromLocalFile(url)
            content = QMediaContent(Qurl)
            self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(0)
        self.listvidename.setCurrentRow(0)
        self.player.play()

    # 调节音量
    def change_volume(self, num):
        self.volume.setText(str(num))
        self.player.setVolume(num)

    # 调节播放进度
    def change_time(self, num):
        self.player.setPosition(num)

    # 快进
    def up_time(self):
        num = self.player.position() + int(self.player.duration() / 20)
        self.player.setPosition(num)

    def down_time(self):
        num = self.player.position() - int(self.player.duration() / 20)
        self.player.setPosition(num)

    # 获取获得进度条进度
    def get_time(self, num):
        self.timeSlider.setMaximum(self.player.duration())
        self.timeSlider.setValue(num)
        d = QDateTime.fromMSecsSinceEpoch(num).toString("mm:ss")
        all = self.player.duration()
        all_d = QDateTime.fromMSecsSinceEpoch(all).toString("mm:ss")
        self.nowtime.setText(d + '/ ' + all_d)

    # 通过点击播放列表切换视频
    def change_by_list(self, current):
        index = self.listvidename.currentRow()
        self.playlist.setCurrentIndex(index)
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Video_win()
    win.show()
    sys.exit(app.exec())

