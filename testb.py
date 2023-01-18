

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


'''
import json


# can instanlty pull the updated json, maybe write a mechanism to check if all the contents have been changed or not
with open("C:/Users/Mert Arkin/AppData/Local/Google/Chrome/User Data/Default/Bookmarks", "r", encoding="utf8") as f:
    data = json.load(f)

roots = data.get("roots")
bookmark_bar = roots.get("bookmark_bar")
bookmark_folder_contents = bookmark_bar.get("children")

c = 0
for i in range(len(bookmark_folder_contents)):  # 605
    temp = bookmark_folder_contents[i].get("type")
    if (temp == "folder"):  # Only 8 folders
        c += 1
        print(bookmark_folder_contents[i].get("name"))

print("\nWe start below ↓")
print(c)


name_url_pairs = []


def get_items(bookmark_folder_contents, level=0):
    items = []
    for item in bookmark_folder_contents:
        temp = item.get("type")
        if temp == "folder":
            children = get_items(item.get("children"), level + 1)
            items.append({"name": item.get("name"), "children": children})
        else:
            items.append({"name": item.get("name"), "url": item.get("url")})
    return items


name_url_pairs = get_items(bookmark_folder_contents)
# Use json.dump() function to save it as json file
try:
    with open("name_url_pairs.json", "w") as f:
        json.dump(name_url_pairs, f, indent=4)
except Exception as e:
    print("An error occured while saving the json file: " + str(e))
    exit()


def print_folder_info(bookmark_folder_contents, level=0):
    for item in bookmark_folder_contents:
        if item.get("type") == "folder":
            print("\t"*level + item.get("name") +
                  " - items inside: " + str(len(item.get("children"))))
            print_folder_info(item.get("children"), level+1)


try:
    print_folder_info(bookmark_folder_contents)
except Exception as e:
    print("An error occured while printing the folder info: " + str(e))
    exit()
'''


''' 

from PyQt5.QtWidgets import QApplication, QAbstractScrollArea, QTreeWidget, QTreeWidgetItem, QMainWindow, QWidget, QPushButton, QScrollArea, QVBoxLayout, QLabel
import sys
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create the tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        # add a folder to the tree
        self.folder = QTreeWidgetItem(["Folder"])
        self.tree.addTopLevelItem(self.folder)
        # Create a widget to hold the layout and the scroll area

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        # Create the scroll area
        self.scroll = QScrollArea()
        # create a label to hold the content

        self.scroll.setViewport(self.tree)  # add folders

        layout.addWidget(self.scroll)
        self.scroll.show()

        # create a label to hold the content
        self.contentLabel = QLabel()
        self.contentLabel.setText("This is the content\n"*100)

        # self.scroll.setWidget(self.contentLabel)

        # Create a layout for buttons

        # Create a button to scroll to the top
        self.topButton = QPushButton("Scroll to Top")
        self.topButton.clicked.connect(self.scrollToTop)
        layout.addWidget(self.topButton)

        # Create a button to scroll to the bottom
        self.bottomButton = QPushButton("Scroll to Bottom")
        self.bottomButton.clicked.connect(self.scrollToBottom)
        layout.addWidget(self.bottomButton)

        links = ["youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com",
                 "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com",
                 "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org",
                 "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com",
                 "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com",
                 "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org", "support.google.com", "linkedin.com", "microsoft.com",
                 "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com", "mozilla.org", "en.wikipedia.org",
                 "mozilla.org", "en.wikipedia.org", "youtube.com", "www.blogger.com", "www.google.com", "play.google.com", "apple.com", "support.google.com", "linkedin.com", "microsoft.com"]
        for i in range(80):
            link_item = QTreeWidgetItem(self.folder)
            link_item.setText(0, links[i])

    def scrollToTop(self):
        print(self.tree.verticalScrollBar().value())

        bar = self.tree.verticalScrollBar()
        yScroll = bar.value() + 40
        # print(self.scroll.verticalScrollBar().setValue(0))
        # self.tree.scrollContentsBy(0, yScroll)
        self.tree.verticalScrollBar().setValue(yScroll)

    def scrollToBottom(self):
        self.scroll.verticalScrollBar().setValue(
            self.centralWidget().findChild(QScrollArea).verticalScrollBar().maximum())


app = QApplication(sys.argv)
# create the main window
mainWin = MyMainWindow()
mainWin.show()
sys.exit(app.exec_())

'''


# WRITE THE PROGRAM FROM 0 - TEMIZE CEKME ISLERI !?

# CHATGPT ANSWERS:

"""

what is super().__init__() in python def __init__(self): class ?

explain all

super().init() in python refers to the initialization method of the parent class. 
When creating a new class, it is often necessary to inherit properties and methods 
from an existing class. The super() function allows the subclass to call the init 
method of the parent class, which initializes the inherited properties and methods. 
This ensures that the subclass has access to all of the necessary properties and 
methods from the parent class. This can help to simplify the code and reduce the 
need for duplicate code. Overall, super().init() is a way to call the parent class's
 init method and inherit the properties and methods from the parent class.


# self.label.setCursor(Qt.PointingHandCursor)

# self.label.setFixedSize(140, 12)

# self.layout.addWidget(
#    self.label, alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

# self.layout.setSpacing(10)

        # self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # self.left_layout = QVBoxLayout()
        # self.left_layout.addWidget(self.scroll_area)

        # self.left_widget = QWidget()
        # self.left_widget.resize(600, 600)



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


   
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.left_widget)
        self.splitter.addWidget(self.web)
        if self.web.isVisible():
        self.web.setVisible(False)
        self.splitter.setHandleWidth(0)
        self.setCentralWidget(self.splitter)
      



        ###########################
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
        ###########################



                    # link_item.setText(0, item.get("name"))
                    # link_item.setText(0, item.get("url"))




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
        


    # we know how to make folder, how to make a child folder,



    #tasarimi iyi bak buna sonra commentlerde
    def on_link_clicked(self, item, column):
        for folder in self.folders:
            if item.parent() == folder:  # check if the clicked item is a child of the "Folder 1" item
                link = item.text(column)
                # print(link)  # column is 0 # in python methods can be still called even when they have parameters but in this case para. not supllied ? (using self.(methodName))
                url = "https://" + link
                self.web.web_view.load(QUrl(url))




        # self.splitter.setSizes([300, 600])
        # self.splitter.setStretchFactor(1, 4)





continue with adding more labels but not strecth too much ?
under each other nicely ? if mmore scroll bar auto ?
loop and test

make the text consist the linkk and when clicked pass to webview !!!
maybe dont hide at this point just show by clciking2 diffreent labels and open 2 different links
oldu galiba

pass the cookies whenever reponse is made


#check if dynamically suits ?


'''
youtube.com ,, www.blogger.com ,, www.google.com ,, play.google.com ,, apple.com ,, support.google.com ,, linkedin.com ,, microsoft.com ,, mozilla.org ,, en.wikipedia.org
'''

# DONE - 15/01/2023
# added foldre/tree structure view option or list. !!?

# check how to parse maybe object or json(ize) the bookmarks folder data in a different way ? -->
# parse inside into 5 nested folders and save all as name - url pairs
# but if they are inside a folder then this program knows paybe parse folder - type pairs
# stop here continue bookmarks algorithm/backend







"""
