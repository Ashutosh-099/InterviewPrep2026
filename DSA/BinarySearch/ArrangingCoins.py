class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            val = (mid * (mid + 1)) // 2
            if val == n: return mid
            elif val > n: high = mid - 1
            else:
                ans = max(ans, mid) 
                low = mid + 1

        return ans