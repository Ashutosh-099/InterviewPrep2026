# Prefix Sum
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        dic = {}
        prefix = 0
        result = 0

        for i, value in enumerate(nums):
            prefix += value
            if prefix == goal:
                result += 1

            remain = prefix - goal
            result += dic.get(remain, 0)
            dic[prefix] = dic.get(prefix, 0) + 1

        return result