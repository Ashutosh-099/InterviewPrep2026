# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Boores Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        ans = 0

        for i in range(len(nums)):
            if freq == 0:
                ans = nums[i]

            if nums[i] == ans:
                freq += 1
            else:
                freq -= 1

        return ans