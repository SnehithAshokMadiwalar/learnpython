#largest number
Q=float(input("Enter first number:"))
W=float(input("Enter second number:"))
E=float(input("Enter third number:"))
if Q>W and Q>E:
 print("largest number is",Q)
elif W>Q and W>E:
 print("largest number is",W)
else:
 print("largest number is",E)
