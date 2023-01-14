
# THIS APPLICATION IS WRITTEN BY MERT ARKIN
# IT ONLY MATCHES THE BOOKMARKS FOLDER STRUCTURE OF HIS, MORE UPGRADES WILL BE ADDED SOON

# VS CODE bookmarks thing


# Import the json module
import json

from tkinter import *

'''
import webview


window = Tk()

name_label = Label(window, text='Username').pack()


window.mainloop()


webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
webview.start()

'''


# Open the file and read the contents
with open("C:/Users/Mert Arkin/AppData/Local/Google/Chrome/User Data/Default/Bookmarks", "r", encoding="utf8") as f:
    # contents = f.read()
    data = json.load(f)

# for d in data:
#    print(d)

# Parse the JSON
# data = json.loads(contents)

# Access the data

# print(data)

# Search for dictionaries with the name "John"
# print(data)

# Access the nested data
# nested_data = data["roots"]["bookmark_bar"]

# key --> key2 --> keys(0) --> ("this one") -->
# [0]["url"]

# Print the nested data
# print(nested_data)

# for element in nested_data:
# print(element)

# all bookmarks until other, (it doesnt inlude other for some reason!)
roots = data.get("roots")

# for r in roots:
#    print(r)


# print("\n")

# bookmarks bar only
bookmark_bar = roots.get("bookmark_bar")

# for b in bookmark_bar:
#    print(b)


'''
******************** BOOKMARKS FOLDER (main)
'''
bookmark_folder_contents = bookmark_bar.get("children")
# prints number of bookmarks
# print(len(bookmark_folder_contents))

# Loop in bookmarks to find the number of folders


# TODO:
# MERGE THESE TOW LOOPS BELOW
# CHECK DYNAMICALLY IF A FOLDER HAS CHILD FOLDERS


# COUNT FOR FOLDERS IN BOOKMARKS FOLDER ITEMS - (also make it dynamic by)
c = 0
for i in range(len(bookmark_folder_contents)):  # 605
    temp = bookmark_folder_contents[i].get("type")
    if (temp == "folder"):  # Only 8 folders
        c += 1
        # print(c)
    # else:
        # print(bookmark_folder_contents[i])
        # print(i, test_folder1[i])
# print("folder count in bookmarks bar: ", c)

# print(bookmark_folder_contents[22].get("name"))

'''
# print(c)
for i in range(c):
    print(str(i) + " " + bookmark_folder_contents[i].get("name"))
'''

# TODO:

# I CAN CHECK THE NESTED FOLDERS BELOW

print()

n = 0
while n != c:
    temp = bookmark_folder_contents[n].get("url")
    if (temp == "chrome://bookmarks/"):
        # print(temp)

        pass
    else:
        # 7 folders
        name = bookmark_folder_contents[n].get("name")

        # n = 1
        # print(n)

        # get children number in folders
        ch = bookmark_folder_contents[n].get("children")
        print("\n" + name + " - items inside:" + str(len(ch)))

        x = 0
        for i in range(len(ch)):
            temp = ch[i].get("type")
            if (temp == "folder"):
                x += 1
        # print(str(x) + " - SUBFOLDERS\n")
        if (x == 0):
            print("subfolder folder num: ", x)

        if (x != 0):
            print("subfolder folder num: ", x)
            for i in range(x):
                sub_ch = bookmark_folder_contents[n].get("children")[
                    i].get("children")
                print("number of items in subfolders", len(sub_ch))
                # for j in range(len(sub_ch)):
                #    print(sub_ch[j].get("name"))

                # one more nested subfolder it is going to be (4) - 12 subfolders on 2022 [1]
                # for

    if (n == 4):
        break
    n += 1

    '''
    if (n == 0):
        temp = bookmark_folder_contents[n].get("url")
        print(temp)

    n += 1
    else
    # print(n)
    '''

'''
x = 0
for i in range(len(b)):
    #temp = ch[i].get("type")
    # print(temp)
    # print(b[i].get("name"))
    if (temp == "folder"):
        x += 1
'''

# contents of crypto folder and len to count items inside
a = bookmark_folder_contents[1].get("children")
# print(len(a))

# contents of 2023
b = bookmark_folder_contents[3].get("children")
# print(len(b))

# this gets the 3rd folder in bookmarks bar, its first children(which first subfolder) and its contents
c = bookmark_folder_contents[3].get("children")[0].get("children")
# print((len(c)))

# porn folder
c1 = bookmark_folder_contents[3].get("children")[1].get("children")


'''
for i in range(x):
    # print(i)
    test = bookmark_folder_contents[3].get("children")[i].get("children")
    print("items in subfolders in: " + str(len(test)))

    for j in range(len(test)):
        print(test[j].get("name"))

# print(i)

'''


# for i in range(len(c)):
#    print(c[i].get("name"))

# porn folder names
# for i in range(len(c1)):
# print(c1[i].get("name"))
# print(c[j])
# print(len(c1))

'''

folder_names = []
for i in range(len(bookmark_folder_contents[1])):
    temp = bookmark_folder_contents[i].get("type")
    if (temp == "folder"):
        temp = bookmark_folder_contents[i].get("name")
        folder_names.append(temp)
        # if(folder_names)

# print("FOLDER NAMES ARE: ", folder_names)
'''

'''
for i in range(c):
    temp = bookmark_folder_contents[i]
    # print(temp.get("children"))
    if (temp.get("children")):
        print(i, "yes")
'''

# test_folder1 = bookmark_folder_contents[2].get("bookmark_folder_contents")
# for i in range(len(test_folder1)):
#    print(test_folder1[i].get("type"))


test_folder = bookmark_folder_contents[2].get("children")[279].get("name")
# print(test_folder)

# you can find types of folders like this (***)
test_folder1 = bookmark_folder_contents[2].get("type")
# print(test_folder1)
'''
********************
'''

# for i in range(len(test_folder1)):
#    print(test_folder1[i].get("type"))
# print(i, test_folder1[i])


'''
******************** CRYPTO FOLDER
'''
# prints crypto folders name
crypto_folder = bookmark_folder_contents[1].get("name")
# print("FOLDER NAME IS: ", crypto_folder)

# prints crypto folder contents
crypto_folder_contents = bookmark_folder_contents[1].get(
    "children")

# prints crypto folder first element of contents
# print(crypto_folder_contents[0].get("name"))

# prints all the names of the elements in that folder
# for i in range(len(crypto_folder_contents)):
# print(crypto_folder_contents[i].get("name"))
#   print(i)

# prints number of elements in that folder
# print(len(crypto_folder_contents))


'''
********************
'''


# for c in bookmark_folder_contents:
#    print(c)


subFolders = json.dumps(bookmark_folder_contents[8])
# print(subFolders)
# print(len(subFolders))

# print((bookmark_folder_contents[].get("name")))

# print(len(bookmark_folder_contents))
# for s in range(len(bookmark_folder_contents)):
#    print(s)

# for s in subFolders:
#    print(s)


# this one gets the subfolders !!! - how to make it dynamic ??
# count the sub folders first then do accordingly - man if's here
# get 3rd folders children where it is children is arrays x element
# gets 2023 first folder
subFolders1 = bookmark_folder_contents[3].get("children")[0]
# print(subFolders1)

# gets 2024 first folder
subFolders2 = bookmark_folder_contents[4].get("children")[0]

# prints first subfolder inside first folder
# print(subFolders2.get("bookmark_folder_contents")[0])

# print(len(roots))
# print(bookmark_bar)


# HOW TO COUNT FOLDERS

# HOW TO COUNT ITEMS IN EACH FOLDER

# THEN KNOW WHICH FOLDER THEY BELONG TO

# PRINT FOLDERS BASED ON NAME OR CHOOSE 1,2,3,...

# ^ NAME AND LINKS

# THINK !!!...


# first the folders then the parents one contents !!
# but maybe chnage bookmarks folder layout, do like 2 most nested
# cant go further than 3 the bookmarks (probably chrome makes it 3 at most) after

# print(json.dumps(children[3], indent=2))  # sort_keys=True

# sorts them by children, children[0] is my bookmarks bar, 1 is crypro folder, 2 is 2024 and so on...
# print(json.dumps(children[0], indent=2))  # sort_keys=True

# now that we sorted, only diplsya name and url of each folder,
# then continue with dipsplaying gui.
# but in between make sure all the folders(size) & contents match!


# 48767th line
# for element in children:
#    print(len(element))


'''
for element in children:
    name = element.get("name")
    url = element.get("url")
    print(name)  # url

for element1 in nested_data1:
    print(json.dumps(element1, indent=2, sort_keys=True))
'''

# path to bookmarks google chrome#
# "C:\Users\Mert Arkin\AppData\Local\Google\Chrome\User Data\Default"

# chrome://bookmarks/

'''

chrome: // bookmarks /?id = 1215
Crypto Extensions & info general

chrome: // bookmarks /?id = 3797
2024

chrome: // bookmarks /?id = 3576
2023

chrome: // bookmarks /?id = 1776
2022

chrome: // bookmarks /?id = 961
2021

chrome: // bookmarks /?id = 191
CODINGGG

chrome: // bookmarks /?id = 2819
psychology - topics & info

chrome: // bookmarks /?id = 1284
Info about old stuff(mostly wiki)(sonra okumalık)

'''
