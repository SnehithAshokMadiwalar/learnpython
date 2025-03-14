#File Handling with OOP:
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, text):
        with open(self.filename, "w") as file:
            file.write(text)
    
    def read(self):
        with open(self.filename, "r") as file:
            return file.read()

file = FileHandler("test.txt")
file.write("Hello OOP!")
print(file.read())
