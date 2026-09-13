# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    

print(fibonacci(10))  # Output: 55