# append file 

text = input("/content/testfile.txt: ")
with open("file.txt", "a") as file:
    file.write(text + "\n")
