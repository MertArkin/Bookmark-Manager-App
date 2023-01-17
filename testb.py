

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
