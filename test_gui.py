

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
app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/"))
web.resize(500, 600)
web.show()
sys.exit(app.exec_())


import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()

        # Set the HTML content of the web view
        html = '<style>div { padding: 2px; background-color: lightblue; }</style><div><ol><li><a href="https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/">Click here to visit the GeeksforGeeks page on PyQt vs Tkinter</a></li><li><a href="https://www.twitch.tv/sommerset">Click here to visit the Twitch channel of sommerset</a></li><li><a href="https://www.twitch.tv/clix">Click here to visit the Twitch channel of clix</a></li></ol></div>'
        self.setHtml(html)
        self.resize(500, 600)
        self.show()

app = QApplication(sys.argv)
# Create a new WebView
web = WebView()
sys.exit(app.exec_())

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

        # DOESNT WORK
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
        # self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QHBoxLayout()
        self.resize(600, 700)

        # Create the buttons and window instances
        self.windows = []
        self.buttons = []

        self.labels = []

        self.windows.append(AnotherWindow(
            "https://www.geeksforgeeks.org/python-gui-pyqt-vs-tkinter/"))
        self.windows.append(AnotherWindow("https://example.com/"))
        self.windows.append(AnotherWindow("https://www.twitch.tv/shroud"))

        # make sure the label and window number match - no list error
        for i in range(3):
            self.labels.append(QLabel("Window {}".format(i+1)))
            layout.addWidget(self.labels[i])

            # self.buttons.append(QPushButton("Window {}".format(i+1)))

            # Add the button to the layout
            # layout.addWidget(self.buttons[i])
            # Connect the button's clicked signal to the toggle_window slot

            # Every label has a mouse press event attached, when clicked, the event and the current label object
            # is passed to the toggle_window function and
            self.labels[i].mousePressEvent = lambda event, label=self.labels[i]: self.toggle_window(
                event, label)

            # print label numbers
            # print(self.labels.index(self.labels[i]))

        # Create a widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the widget as the central widget of the main window
        self.setCentralWidget(widget)

    # open right link

    def toggle_window(self, event, label):
        """
        This event handler function is called when a label is clicked.
        It shows the corresponding window.
        """
        # Get the sender label
        # label = self.sender()
        # Find the label's index
        i = self.labels.index(label)
        print(i)
        # Get the corresponding window instance
        window = self.windows[i]
        if window.isVisible():
            window.hide()
        else:
            window.show()


app = QApplication(sys.argv)

# Create a new MainWindow and show it
w = MainWindow()
w.show()
sys.exit(app.exec_())
