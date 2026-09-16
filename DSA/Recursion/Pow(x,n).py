# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
            
        if n % 2 == 0:
            return self.myPow(x * x, n//2)
        else:
            return self.myPow(x * x, (n-1)//2) * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.pow(x, -n)
        else:
            return self.pow(x, n)