#Handle ValueError in Input
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input, please enter a number")
