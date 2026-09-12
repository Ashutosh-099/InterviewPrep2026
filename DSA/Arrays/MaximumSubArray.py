# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Kadane's Algorithm is an efficient way to solve this problem in O(n) time complexity.
# Kadane's Algorithm works by iterating through the array and keeping track of the maximum sum of the subarray that ends at the current index. If the current sum becomes negative, we reset it to zero, as a negative sum would not contribute to a maximum subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sumArray = float('-inf')
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            sumArray = max(sumArray, curr)

            if curr < 0:
                curr = 0

        return sumArray