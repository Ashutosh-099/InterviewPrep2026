class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []

        def makePermutation(start):
            if start == len(nums):
                result.append(nums[:])
                return
            unique = set()
            for i in range(start, len(nums)):
                if nums[i] not in unique:
                    unique.add(nums[i])
                    nums[i], nums[start] = nums[start], nums[i]
                    makePermutation(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]

        makePermutation(0)
        return result