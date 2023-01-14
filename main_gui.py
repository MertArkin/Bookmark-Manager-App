
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

'''
class AnotherWindow(QWebEngineView):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self, url):
        super().__init__()
        # Set the URL
        self.load(QUrl(url))
        self.resize(500, 500)
        # Hide the window, hide and nothing works the same
        # self.hide()
        # self.show()
        DOESNT WORK
        # Create a QWebEngineView and set the URL
        self.web_view = QWebEngineView()
        self.web_view.load(
            QUrl("https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/"))
        self.web_view.resize(500, 600)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        self.resize(500, 600)
        self.show()
'''


class LinksWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        # self.resize(self.sizeHint())

        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: gray;")
        self.layout = QVBoxLayout()
        self.label = QLabel("link to open/hide")

        # self.label1 = QLabel("link to open/hide")

        self.button = QPushButton("button to open/hide")
        self.button.setFixedSize(100, 30)
        self.label.setFixedSize(140, 12)

        # self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.label.setCursor(Qt.PointingHandCursor)

        # self.setCursor(Qt.PointingHandCursor)

        self.layout.addWidget(
            self.label, alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        # self.layout.addWidget(
        #     self.label1, alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.layout.addWidget(
            self.button, alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.setLayout(self.layout)


class WebWidget(QWidget):
    def __init__(self, url):
        super().__init__()
        # self.setAutoFillBackground(True)
        # self.setStyleSheet("background-color: red;")
        self.layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl(url))
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.splitter = QSplitter(Qt.Horizontal)
        self.links = LinksWidget()
        self.web = WebWidget(
            "https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/")
        self.splitter.addWidget(self.links)
        self.splitter.addWidget(self.web)
        self.splitter.setHandleWidth(0)
        self.setCentralWidget(self.splitter)
        self.resize(1200, 600)
        self.links.button.clicked.connect(self.toggle_web_view)

        self.links.label.mousePressEvent = self.toggle_web_view

        # self.splitter.setSizes([200, 500])
        self.splitter.setStretchFactor(0, 2)  # links widget
        self.splitter.setStretchFactor(1, 4)  # web widget

    def toggle_web_view(self, event=None):
        if self.web.isVisible():
            self.web.setVisible(False)
            self.splitter.setSizes([300, 0])
            self.splitter.setStretchFactor(0, 2)
        else:
            self.web.setVisible(True)
            self.splitter.setSizes([300, 600])
            self.splitter.setStretchFactor(1, 4)


# Create a QApplication instance
app = QApplication(sys.argv)

w = MainWindow()
w.show()
sys.exit(app.exec())
"""

continue with adding more labels but not strecth too much ?
under each other nicely ? if mmore scroll bar auto ?
loop and test

make the text consist the linkk and when clicked pass to webview !!!
maybe dont hide at this point just show by clciking2 diffreent labels and open 2 different links
oldu galiba

pass the cookies whenever reponse is made


"""
