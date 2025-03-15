# Handle Multiple Exception
 try:
    with open("nonexistent.txt", "r") as file:
        print(int(file.read()))
except (FileNotFoundError, ValueError):
    print("Error: File not found or invalid data")
