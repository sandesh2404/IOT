

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(f"Factorial = {fact(5)}")