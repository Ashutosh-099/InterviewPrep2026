# Prefix Sum
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftPivot = [0] * (len(nums) + 1)
        rightPivot = [0] * (len(nums) + 1)
 
        for i in range(1, len(nums)+1):
            leftPivot[i] = leftPivot[i-1] + nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            rightPivot[j] = rightPivot[j+1] + nums[j+1]

        print(leftPivot)
        print(rightPivot)
        for i in range(len(leftPivot)):
            if leftPivot[i] == rightPivot[i] and i != len(nums):
                return i
        return -1


# Optimal Approach
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]

        return -1