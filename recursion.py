def fibonacci(n):
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def reverse_string(string):
    if len(string) == 1:
        return string[0]
    return reverse_string(string[1:]) + string[0]

print(reverse_string("hello"))