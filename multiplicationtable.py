# multipication table
def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} × {i} = {n * i}")

multiplication_table(5)
