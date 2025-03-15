#Find and Replace in a File

word_to_find = "old"
replacement = "new"
with open("file.txt", "r") as file:
    content = file.read()
with open("file.txt", "w") as file:
    file.write(content.replace(word_to_find, replacement))
