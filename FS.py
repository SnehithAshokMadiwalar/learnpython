# fibopnaci series
def fibonacci(n):
  a,b=0,1
  for i in range(n):
    a,b=b,a+b
n=int(input("enter the number")) 
fibonacci(n)
