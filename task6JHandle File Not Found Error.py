import os
filename = "/content/testfile.txt"
print("/content/testfile.txt" if os.path.exists(filename) else "File does not exist")
