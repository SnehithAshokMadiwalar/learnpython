#lambda function for sorting
nums = [5, 2, 9, 1, 5, 6]
print(sorted(nums))  
     
students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
print(sorted(students, key=lambda x: x[1]))  


words = ["apple", "banana", "kiwi", "cherry"]
print(sorted(words, key=lambda x: len(x)))  
