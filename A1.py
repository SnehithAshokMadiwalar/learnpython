# prime checker
def is_prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(n**0.5) + 1)):
        return False
    return True

print(is_prime(7))  
print(is_prime(10))
