#value error
try:
    num = int("hello")  # This will raise a ValueError
except ValueError:
    print("Error: Invalid input! Please enter a number. ")
