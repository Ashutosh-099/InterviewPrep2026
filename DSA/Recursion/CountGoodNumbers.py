# Brute Force Solution
def countGoodNumbers(self, n: int) -> int:
    if n == 1:
        return 5
    if n == 2:
        return 20

    if n % 2 == 0:
        return (4 * self.countGoodNumbers(n-1)) % ((10**9)+7)
    else:
        return 5 * self.countGoodNumbers(n-1) % ((10**9)+7)
    
# Optimized Solution
class Solution:
    def pow(self, x:float, n:int) -> int:
        mod = ((10**9)+7)

        if n == 0:
            return 1

        if n % 2 == 0:
            return self.pow((x * x)%mod, n//2)
        else:
            return (x * self.pow((x*x)%mod, (n-1)//2))%mod

    def countGoodNumbers(self, n: int) -> int:
        mod = ((10**9)+7)
        odd = n // 2
        even = n // 2 + n % 2

        return (self.pow(5, even)%mod * self.pow(4, odd)%mod)%mod