def power(x, n):
    return 1 if n == 0 else (1 / power(x, -n) if n < 0 else x * power(x, n - 1))

print(power(2, 3))   
print(power(2, -2))  
