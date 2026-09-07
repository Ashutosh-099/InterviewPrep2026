# GCD of two numbers

# Brute force approach
def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a
    

    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

# Optimized approach using Euclidean algorithm
# Euclidean algorithm states that GCD of two numbers a and b is the same as GCD of b and a % b. The process is repeated until b becomes 0. The GCD is then the last non-zero value of a.
# GCD(a, b) = GCD(a - b, b) if a > b else GCD(a, b - a)...
# GCD(a, b) = GCD(a % b, b) if a > b else GCD(a, b % a)
def gcd_euclidean(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

print(gcd_euclidean(20, 28))  # Output: 4
