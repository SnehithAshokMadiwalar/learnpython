#Handle Multiple Exceptions
try:
    with open("file.txt", "r") as file:
        num = int(file.read())
except (FileNotFoundError, ValueError):
    print("Error occurred.")
