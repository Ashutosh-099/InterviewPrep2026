# Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        # Find Pivot element
        pivot = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # Swap with right most element which is bigger than pivot element
        if pivot != -1:
            for i in range(len(nums)-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        else:
            # array in descending order - Reverse
            nums.reverse()
            return

        # Reverse the array after pivot
        p = pivot + 1
        q = len(nums) - 1

        while p <= q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
        return