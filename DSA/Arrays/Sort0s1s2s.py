# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
# The sorting must be done in-place, without making a copy of the original array.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        twos = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
            
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos -= 1

    