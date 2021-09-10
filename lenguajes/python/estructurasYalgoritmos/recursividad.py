
def fibonacci(n):
    if n <= 1:
        return n
    print(n)
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(5)




