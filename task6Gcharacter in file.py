#Count Characters in a File snehith

with open("/content/testfile.txt", "r") as file:
    print(len(file.read()))
