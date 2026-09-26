# Prefix Sum
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = {0: -1} # -1 because we are dealing with index not count
        prefix = 0

        for j, value in enumerate(nums):
            prefix += value
            remain = prefix % k

            if remain in remainder:
                gap = j - remainder[remain]
                if gap >= 2:
                    return True
            else:
                remainder[remain] = j
        
        return False