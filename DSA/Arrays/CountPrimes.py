# Count no of primes between 1 to n(inclusive)
# Brute force approach
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def countPrimes(n):
    if n == 0 or n == 1:
        return 0

    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
    return count


# Optimized Approach - Sieve of Eratosthenes
def countPrimesOptimized(n):
    if n == 0: return 0
    if n == 1: return 0

    isPrime = [True] * (n + 1)
    count = 0
    isPrime[0] = isPrime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, n+1):
        if isPrime[i]:
            count += 1
            for j in range(i, n +1, i):
                isPrime[j] = False

    return count


print(countPrimesOptimized(50))