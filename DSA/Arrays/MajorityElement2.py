# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        numeric1 = numeric2 = None
        count1 = count2 = 0

        for value in nums:
            if numeric1 == None and value != numeric2:
                numeric1 = value
                count1 = 1
            elif numeric2 == None and value != numeric1:
                numeric2 = value
                count2 = 1
            elif value == numeric1:
                count1 += 1
            elif value == numeric2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        threshold = len(nums) // 3


        count1 = count2 = 0
        for value in nums:
            if value == numeric1:
                count1 += 1
            elif value == numeric2:
                count2 += 1

        result = []
        if count1 > threshold:
            result.append(numeric1)
        if count2 > threshold:
            result.append(numeric2)

        return result