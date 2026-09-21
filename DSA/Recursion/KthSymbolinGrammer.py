# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10. Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
class Solution:
    def buildGrammer(self, n:int, k:int):
        if n == 1 and k == 1:
            return 0

        length = 2 ** (n-1)
        mid = length // 2

        if k <= mid:
            return self.buildGrammer(n - 1, k)
        else:
            return 1 if self.buildGrammer(n - 1, k - mid) == 0 else 0


        
    def kthGrammar(self, n: int, k: int) -> int:
        return self.buildGrammer(n, k)