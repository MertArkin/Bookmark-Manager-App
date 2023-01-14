import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QSplitter,
    QDockWidget,
    QSizePolicy,
)
from PyQt5.QtGui import QPalette, QColor


class LinksWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: gray;")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


class WebWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.splitter = QSplitter(Qt.Horizontal)
        self.links = LinksWidget()
        self.web = WebWidget()
        self.splitter.addWidget(self.links)
        self.splitter.addWidget(self.web)
        self.web.setVisible(False)
        self.splitter.setHandleWidth(0)
        self.setCentralWidget(self.splitter)
        self.resize(1200, 600)
        links = ["youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com",
                 "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org"]
        for i in range(10):
            label = QLabel(links[i])
            # here it adds them to linkwidget ↓
            self.links.layout.addWidget(label)
            label.setCursor(Qt.PointingHandCursor)
            # print(links[i])
            label.mousePressEvent = lambda event, url=links[i]: self.open_link(
                event, url)
        self.splitter.setStretchFactor(0, 2)  # links widget
        self.splitter.setStretchFactor(1, 4)  # web widget

    def open_link(self, event, url):
        print(url)
        self.web.web_view.load(QUrl("https://"+url))
        self.web.setVisible(True)
        self.splitter.setSizes([300, 600])
        self.splitter.setStretchFactor(1, 4)


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())

"""
#check if dynamically suits ?
"""


'''
youtube.com ,, www.blogger.com ,, www.google.com ,, play.google.com ,, apple.com ,, support.google.com ,, linkedin.com ,, microsoft.com ,, mozilla.org ,, en.wikipedia.org
'''
