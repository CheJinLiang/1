def digui(n):
    if n == 1:
        return 1
    return n*digui(n-1)
print(digui (5))