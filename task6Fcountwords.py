# count  words in file snehith
with open("/content/testfile.txt", "r") as file:
    print(len(file.read().split()))
