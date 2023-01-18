import sys
import json

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QSplitter,
    QScrollArea,
    QDockWidget,
    QGridLayout,
    QSizePolicy,
    QSpacerItem,
    QLayout,
    QTreeWidget,
    QTreeWidgetItem,
    QAction,
    QToolBar,
    QLineEdit,
    QFrame,
    QAbstractScrollArea,
    QAbstractItemView,
)
from adblockparser import AdblockRules

app = QApplication(sys.argv)


class ParseBookmarks():
    def __init__(self):
        super(ParseBookmarks, self).__init__()
        with open("C:/Users/Mert Arkin/AppData/Local/Google/Chrome/User Data/Default/Bookmarks", "r", encoding="utf8") as f:
            data = json.load(f)

        self.roots = data.get("roots")
        self.bookmark_bar = self.roots.get("bookmark_bar")
        self.bookmark_folder_contents = self.bookmark_bar.get("children")


class LinksWidget(QWidget):
    def __init__(self):
        super(LinksWidget, self).__init__()
        self.setFixedSize(0, 0)  # just to draw outer border ?
        self.setStyleSheet("background-color: #909090;")
        self.setAutoFillBackground(True)

        self.layout = QVBoxLayout()
        self.layout.setSizeConstraint(QLayout.SetMinAndMaxSize)  # onemli
        self.setLayout(self.layout)


"""
ad block part ? - necessary ?
class WebEngineUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self):
        super(WebEngineUrlRequestInterceptor, self).__init__()
        with open("easylist.txt", encoding="utf-8") as f:
            raw_rules = f.readlines()
            self.rules = AdblockRules(raw_rules)
            
        def interceptRequest(self, info):
            url = info.requestUrl().toString()
            if self.rules.should_block(url):
                print("block::::::::::::::::::::::", url)
                info.block(True)

interceptor = WebEngineUrlRequestInterceptor()
QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
"""


class WebWidget(QWidget):
    def __init__(self):
        super(WebWidget, self).__init__()
        self.web_view = QWebEngineView()

        # Returns the cookie store for this profile.
        cookie_store = self.web_view.page().profile().cookieStore()
        cookie_store.loadAllCookies()  # deleteAllCookies()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    # ALL I HAD TO DO WAS ACCESS TREE WIDGETS SCROLL BAR :d
    def scrollToTop(self):
        print("scroll top")
        # print(self.tree_widget.verticalScrollBar().value())
        # bar = self.tree_widget.verticalScrollBar()
        # yScroll = bar.value() + 40
        # print(self.scroll.verticalScrollBar().setValue(0))
        # self.tree.scrollContentsBy(0, yScroll)
        # self.tree_widget.verticalScrollBar().setValue(0)
        self.tree_widget.verticalScrollBar().setValue(
            self.tree_widget.verticalScrollBar().value() - 15)
        # self.centralWidget().findChild(QScrollArea).verticalScrollBar().setValue(0)

    def scrollToBottom(self):
        print("scroll bottom")
        self.tree_widget.verticalScrollBar().setValue(
            self.tree_widget.verticalScrollBar().value() + 15)  # 30 or 15, it centers it in the QTreeWidget
        # self.tree_widget.verticalScrollBar().setValue(
        #    self.tree_widget.verticalScrollBar().maximum())
        # self.centralWidget().findChild(QScrollArea).verticalScrollBar().setValue(
        #    self.centralWidget().findChild(QScrollArea).verticalScrollBar().maximum())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Bookmarks Application")
        self.resize(1500, 700)

        self.bookmarks = ParseBookmarks()
        self.links_widget = LinksWidget()
        self.web = WebWidget()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.links_widget)
        self.scroll_area.setWidgetResizable(True)

        self.search_box = QLineEdit()
        self.search_box.setFixedWidth(265)
        self.search_box.setPlaceholderText("Search links in current folder")

        self.search_clear_button = QPushButton("clear")
        # self.search_clear_button.setFixedSize(65, 20)
        self.search_clear_button.clicked.connect(self.clear_search)

        self.scroll_up_button = QPushButton("Page Up")
        self.scroll_down_button = QPushButton("Page Down")
        self.scroll_up_button.setFixedSize(65, 20)
        self.scroll_down_button.setFixedSize(65, 20)

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_box)
        self.search_layout.addWidget(self.search_clear_button)
        self.links_widget.layout.insertLayout(0, self.search_layout)
        self.search_layout.addWidget(self.scroll_up_button)
        self.search_layout.addWidget(self.scroll_down_button)

        self.tree_widget = QTreeWidget()
        self.tree_widget .setHeaderHidden(True)
        self.tree_widget.setStyleSheet(
            "QTreeWidget::item:hover { background-color: #bf83a1; }; QTreeWidget { outline: none; }")
        # self.tree_widget.setAlternatingRowColors(False)
        self.links_widget.layout.addWidget(self.tree_widget)

        self.toolbar = self.addToolBar("Navigation")
        # self.toolbar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.toolbar.setStyleSheet(
            "QToolButton { border: 1.25px solid gray; }")
        # 0 is insert first, 1 is under 0 since its QVBoxLayout
        self.web.layout.insertWidget(0, self.toolbar)

        self.back_action = QAction("Back", self)
        # self.back_action.setShortcut("Alt+Left")
        self.back_action.triggered.connect(self.web.web_view.back)
        self.toolbar.addAction(self.back_action)

        self.forward_action = QAction("Forward", self)
        # self.forward_action.setShortcut("Alt+Right")
        self.forward_action.triggered.connect(self.web.web_view.forward)
        self.toolbar.addAction(self.forward_action)

        self.open_action = QAction("Open in web browser", self)
        self.open_action.triggered.connect(self.on_open_clicked)
        self.toolbar.addAction(self.open_action)

        # everything inside main frame - left and right side os qhboxlayout
        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.scroll_area)
        self.central_layout.addWidget(self.web)

        # the layout above is set layout as the widget --> lastly, you have to render widget ?
        self.central_widget = QWidget()
        self.central_layout.setStretch(0, 1)
        self.central_layout.setStretch(1, 1)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # scroll mechanic
        self.scroll_up_button.clicked.connect(self.scrollToTop)
        self.scroll_down_button.clicked.connect(self.scrollToBottom)

        print("\nWe start below ↓")

        def create_tree(bookmark_folder_contents, parent=None):
            i = 1
            for item in bookmark_folder_contents:
                if item.get("type") == "folder":
                    self.folderx = QTreeWidgetItem(parent)
                    self.folderx.setText(0, item.get("name"))
                    create_tree(item.get("children"), self.folderx)
                else:  # probably link, url ???
                    link_item = QTreeWidgetItem(parent)
                    # nice logic down here # cant watch twith but can youtube ?!?
                    url = item.get("url")
                    url_label = QLabel(url)  # ) + "\n")

                    name = item.get("name")
                    # ***
                    name_label = QLabel(str(i) + "  -  " + name)
                    i += 1
                    # set bg color when hovering on links !?! - you can set them to name_label * below
                    name_label.setStyleSheet(
                        "QLabel { color: #000000; };")

                    url_label.setStyleSheet(
                        "QLabel::hover { background-color: #bf83a1; }")
                    url_label.mousePressEvent = lambda event, urlparam=url: self.open_link(
                        event, urlparam)

                    # link_item.setText(0, name)  # + " " + str(i))
                    vbox = QVBoxLayout()
                    vbox.addWidget(name_label)
                    vbox.addWidget(url_label)

                    # vbox.setSpacing(50)
                    # vbox.setContentsMargins(5, 5, 300, 5)
                    # set border width and color

                    # ro use Qwidget, widget.setLayout ... - using frame cause it has bult-in borders,
                    # also check eah of these things documentation
                    frame = QFrame()
                    frame.setFrameShape(QFrame.StyledPanel)

                    # set border width and color
                    # frame.setStyleSheet("QFrame { border: 2px solid red; }")

                    # frame.setContentsMargins(0, 10, 0, 10)
                    # frame.setStyleSheet(
                    #    "QFrame { background-color: rgb(50,50,50); padding: 1px; }")

                    # the hell bro :DDD
                    # https://stackoverflow.com/questions/7885653/qt-4-how-to-set-outer-border-for-qwidget-so-that-its-inner-widgets-are-unaffect
                    """
                    Use
                    .QWidget
                    {
                        // your css rules
                    }
                    .QWidget will apply CSS only to classes that are EXACTLY QWidget and not inheriting QWidget
                    """

                    # this below is the margin to bottom but leaves clicable space
                    frame.setStyleSheet(
                        ".QFrame { border: 1px solid black; margin-top: 3.0px; margin-bottom: 3.0px; padding: 10px; }")

                    frame.setLayout(vbox)

                    # self.tree_widget.setStyleSheet(
                    #    "QFrame { padding: 5px 0; }")

                    self.tree_widget.setItemWidget(link_item, 0, frame)

        # calismaz bu
        # self.tree_widget.itemClicked.connect(self.open_link)

        # Add the root folder to the tree widget
        # nasil isler bhurasi bak ↓↑

        root = QTreeWidgetItem(self.tree_widget)
        root.setText(0, "Bookmarks bar")
        create_tree(self.bookmarks.bookmark_folder_contents, root)

        # BAK !
        """
        add horizontal scroll bar (fit in width) + better colours, - extra options 
        to the app ? like what ? #cookie ok saving and loading in each url
        save every click and show recenlty been websotes ?
        make it so left folder clicked middle contents /name urls / right web page
        index in folers

        dont make it till the end this is a self-development project

        """
        # self.search_box.textChanged.connect(self.filter_items)

        # functionize everything so any change in data structure then do it by calling your special/single function for it
        # dont use labels use folders and - !

        # nice, make folder child look 2 px bigger

        '''
        self.folders = [self.folder, self.folder2,
                        self.child_folder]  # self.child_folder2]
        '''

        # use append to append them in a list when created (see if you can make nested folders ?)
        # self.folders.append(self.folder2)
    '''
    BROKEN NOW !!! - 17/01/2023 fix later - imported all data and cen webview !
    # no parameter passed when fuction is called ?
    def filter_items(self, search_text):
        # search_term = self.search_box.text() and dont use the second parameter / change the logic way and
        # how variables are passed from one point of program to the other

        search_text = search_text.lower()
        print(search_text)

        for folder in self.folders:
            for i in range(folder.childCount()):
                item = folder.child(i)
                item_text = item.text(0).lower()

                """
                if a child doesn't have more than 1 items inside which
                we can check by checking child count if it is above 0 
                then this is definitely a folder
                """
                if item.childCount() > 0:  # check if item is a folder
                    continue  # if it is a folder, skip the rest of the loop

                if search_text.lower() not in item_text:
                    item.setHidden(True)
                else:
                    item.setHidden(False)
    '''

    """
    this onnly checks the first folder - first iteration of search
    def search_links(self, text):
        self.search_results = []
        for i in range(self.folder.childCount()):
            item = self.folder.child(i)
            if text.lower() in item.text(0).lower():
                self.search_results.append(item)
                item.setHidden(False)
            else:
                item.setHidden(True)
    """

    def clear_search(self):
        self.search_box.clear()
        for folder in self.folders:
            for i in range(folder.childCount()):
                item = folder.child(i)
                if item.childCount() == 0:
                    item.setHidden(False)

    # Open in web browser
    def on_open_clicked(self):
        url = self.web.web_view.url().toString()
        QDesktopServices.openUrl(QUrl(url))

    def open_link(self, event, url):
        print(url)
        self.web.web_view.load(QUrl(url))  # "https://" dont need


main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())
