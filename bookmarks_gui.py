
import sys
import json

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

        # self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: gray;")
        self.layout = QVBoxLayout()

        # self.label.setCursor(Qt.PointingHandCursor)

        # self.label.setFixedSize(140, 12)

        # self.layout.addWidget(
        #    self.label, alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        # both works below
        # self.layout.setSpacing(10)
        self.layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.setLayout(self.layout)


class WebWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)


class ParseBookmarks():
    def __init__(self):
        super(ParseBookmarks, self).__init__()
        with open("C:/Users/Mert Arkin/AppData/Local/Google/Chrome/User Data/Default/Bookmarks", "r", encoding="utf8") as f:
            data = json.load(f)

        self.roots = data.get("roots")
        self.bookmark_bar = self.roots.get("bookmark_bar")
        self.bookmark_folder_contents = self.bookmark_bar.get("children")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.bookmarks = ParseBookmarks()

        self.setWindowTitle("Bookmarks App")

        self.links_widget = LinksWidget()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.links_widget)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.scroll_area)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search links in current folder")
        self.search_clear_button = QPushButton("clear")
        self.search_clear_button.clicked.connect(self.clear_search)

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_box)
        self.search_layout.addWidget(self.search_clear_button)
        self.links_widget.layout.insertLayout(0, self.search_layout)

        self.left_widget = QWidget()
        self.left_widget.resize(600, 600)

        self.tree_widget = QTreeWidget()
        self.tree_widget .setHeaderHidden(True)

        """
        self.folder = QTreeWidgetItem(self.tree_widget)
        self.folder.setText(0, 'Folder 1')
        self.links_widget.layout.addWidget(self.tree_widget)

        self.folder2 = QTreeWidgetItem(self.tree_widget)
        self.folder2.setText(0, 'Folder 2')
        self.links_widget.layout.addWidget(self.tree_widget)

        # child folder
        self.child_folder = QTreeWidgetItem(self.folder2)
        self.child_folder.setText(0, "Child Folder 1")

        # child folder 2
        # self.child_folder2 = QTreeWidgetItem(self.child_folder)
        # self.child_folder2.setText(0, "Child Folder 1")

        self.left_widget.setLayout(self.left_layout)
        """

        self.web = WebWidget()

        # everything inside main frame - left and right side os qhboxlayout
        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.scroll_area)
        self.central_layout.addWidget(self.web)

        # the layout above is set layout as the widget --> lastly, you have to render widget ?
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.central_layout.setStretch(0, 1)
        self.central_layout.setStretch(1, 1)

        """
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.left_widget)
        self.splitter.addWidget(self.web)
        if self.web.isVisible():
        self.web.setVisible(False)
        self.splitter.setHandleWidth(0)
        self.setCentralWidget(self.splitter)
        """
        self.resize(1200, 600)

        """
        c = 0
        for i in range(len(self.bookmarks.bookmark_folder_contents)):  # 605
            temp = self.bookmarks.bookmark_folder_contents[i].get("type")
            if (temp == "folder"):  # Only 8 folders
                c += 1
                print(self.bookmarks.bookmark_folder_contents[i].get("name"))
                self.folderx = QTreeWidgetItem(self.tree_widget)
                self.folderx.setText(
                    0, self.bookmarks.bookmark_folder_contents[i].get("name"))
                self.links_widget.layout.addWidget(self.tree_widget)
        print(c)
        """
        print("\nWe start below ↓")

        def create_tree(bookmark_folder_contents, parent=None):
            for item in bookmark_folder_contents:
                if item.get("type") == "folder":
                    folderx = QTreeWidgetItem(parent)
                    folderx.setText(0, item.get("name"))
                    create_tree(item.get("children"), folderx)
                else:
                    link_item = QTreeWidgetItem(parent)

                    # link_item.setText(0, item.get("name"))
                    # link_item.setText(0, item.get("url"))

                    url = item.get("url")
                    label = QLabel(url)
                    label.mousePressEvent = lambda event, url=url: self.open_link(
                        event, url)
                    self.tree_widget.setItemWidget(link_item, 0, label)

        # Add the root folder to the tree widget
        root = QTreeWidgetItem(self.tree_widget)
        root.setText(0, "Bookmarks bar")
        create_tree(self.bookmarks.bookmark_folder_contents, root)
        self.links_widget.layout.addWidget(self.tree_widget)

        """
        links = ["youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com",
                 "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com",
                 "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org",
                 "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com",
                 "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com",
                 "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "support.google.com", "linkedin.com", "microsoft.com",
                 "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org",
                 "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com"]
        # print("length of links: " + str(len(links)))

        for i in range(80):
            label = QLabel(links[i] + " " + str(i))

            # it works
            # 550 20 ?
            # label.setFixedSize(QSize(500, 20))
            # label.setMinimumSize(QSize(50, 20))
            # label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # here it adds them to linkwidget ↓

            # self.links_widget.layout.addWidget(label)

            link_item = QTreeWidgetItem(self.folder)
            link_item.setText(0, links[i])  # + " " + str(i))

            link_item2 = QTreeWidgetItem(self.folder2)
            link_item2.setText(0, links[i])  # + " " + str(i))

            link_item3 = QTreeWidgetItem(self.child_folder)
            link_item3.setText(0, links[i])

            # link_item4 = QTreeWidgetItem(self.child_folder2)
            # link_item4.setText(0, links[i])

            label.setCursor(Qt.PointingHandCursor)
            # print(links[i])
            label.mousePressEvent = lambda event, url=links[i]: self.open_link(
                event, url)
        # self.splitter.setStretchFactor(0, 1)  # links widget
        # self.splitter.setStretchFactor(1, 1)  # web widget

        self.folder.setText(
            0, 'Folder 1 (' + str(self.folder.childCount()) + ')')
        
        """

        self.tree_widget.itemClicked.connect(self.on_link_clicked)

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

        # BAK !
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

    # we know how to make folder, how to make a child folder,

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

    def on_link_clicked(self, item, column):
        for folder in self.folders:
            if item.parent() == folder:  # check if the clicked item is a child of the "Folder 1" item
                link = item.text(column)
                # print(link)  # column is 0 # in python methods can be still called even when they have parameters but in this case para. not supllied ? (using self.(methodName))
                url = "https://" + link
                self.web.web_view.load(QUrl(url))

    def open_link(self, event, url):
        print(url)
        self.web.web_view.load(QUrl(url))  # "https://"
        # self.splitter.setSizes([300, 600])
        # self.splitter.setStretchFactor(1, 4)


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())


"""

continue with adding more labels but not strecth too much ?
under each other nicely ? if mmore scroll bar auto ?
loop and test

make the text consist the linkk and when clicked pass to webview !!!
maybe dont hide at this point just show by clciking2 diffreent labels and open 2 different links
oldu galiba

pass the cookies whenever reponse is made


"""

"""
#check if dynamically suits ?
"""
'''
youtube.com ,, www.blogger.com ,, www.google.com ,, play.google.com ,, apple.com ,, support.google.com ,, linkedin.com ,, microsoft.com ,, mozilla.org ,, en.wikipedia.org
'''

# DONE - 15/01/2023
# added foldre/tree structure view option or list. !!?

# check how to parse maybe object or json(ize) the bookmarks folder data in a different way ? -->
# parse inside into 5 nested folders and save all as name - url pairs
# but if they are inside a folder then this program knows paybe parse folder - type pairs
# stop here continue bookmarks algorithm/backend
