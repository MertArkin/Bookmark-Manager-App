
# THIS APPLICATION IS WRITTEN BY MERT ARKIN
# IT ONLY MATCHES THE BOOKMARKS FOLDER STRUCTURE OF HIS, MORE UPGRADES WILL BE ADDED SOON

# VS CODE bookmarks thing


# Import the json module
import json

'''
from tkinter import *
window = Tk()
window.mainloop()
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


bookmark_folder_contents = bookmark_bar.get("children")
# prints number of bookmarks
# print(len(bookmark_folder_contents))

# Loop in bookmarks to find the number of folders


# TODO:
# s#f#
# dsf


# COUNT FOR FOLDERS IN BOOKMARKS FOLDER ITEMS - (also make it dynamic by)
c = 0
for i in range(len(bookmark_folder_contents)):
    temp = bookmark_folder_contents[i].get("type")
    if (temp == "folder"):
        c += 1
    # else:
        # print(bookmark_folder_contents[i])
        # print(i, test_folder1[i])
print(c)

for i in range(c):
    print(bookmark_folder_contents[i].get("children")[c].get("name"))

# test_folder1 = bookmark_folder_contents[2].get("bookmark_folder_contents")
# for i in range(len(test_folder1)):
#    print(test_folder1[i].get("type"))


test_folder = bookmark_folder_contents[2].get("children")[279].get("name")
# print(test_folder)

# you can find types of folders like this (***)
test_folder1 = bookmark_folder_contents[2].get("type")
# print(test_folder1)


# for i in range(len(test_folder1)):
#    print(test_folder1[i].get("type"))
# print(i, test_folder1[i])


'''
******************** CRYPTO FOLDER
'''
# prints crypto folder and its name
crypto_folder = bookmark_folder_contents[1].get("name")
# print(crypto_folder)

# prints crypto folder contents
crypto_folder_bookmark_folder_contents = bookmark_folder_contents[1].get(
    "children")

# prints crypto folder first element of contents
# print(crypto_folder_bookmark_folder_contents[0].get("name"))

# for i in range(len(crypto_folder_bookmark_folder_contents)):
# prints all the names of the elements in that folder
# print(crypto_folder_bookmark_folder_contents[i].get("name"))
#   print(i)

# prints number of elements in that folder
# print(len(crypto_folder_bookmark_folder_contents))


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
'''


# for element1 in nested_data1:
#    print(json.dumps(element1, indent=2, sort_keys=True))

# print(json.dumps(data, indent=2, sort_keys=True))

# path to bookmarks google chrome#
# "C:\Users\Mert Arkin\AppData\Local\Google\Chrome\User Data\Default"

# chrome://bookmarks/

'''

chrome://bookmarks/?id=1215
Crypto Extensions & info general

chrome://bookmarks/?id=3797
2024

chrome://bookmarks/?id=3576
2023

chrome://bookmarks/?id=1776
2022

chrome://bookmarks/?id=961
2021

chrome://bookmarks/?id=191
CODINGGG

chrome://bookmarks/?id=2819
psychology - topics & info

chrome://bookmarks/?id=1284
Info about old stuff (mostly wiki) (sonra okumalık)

'''
