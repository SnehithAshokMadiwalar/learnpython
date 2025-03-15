# write to file
# with open(/content/testfile.txt:) as a file:
text = input("/content/testfile.txt: ")
with open("file.txt", "w") as file:
    file.write(text)
