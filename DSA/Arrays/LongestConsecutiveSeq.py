# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        result = curr = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr += 1
            elif nums[i] - nums[i - 1] == 0:
                continue
            else:
                result = max(result, curr)
                curr = 1
        result = max(result, curr)
        return result