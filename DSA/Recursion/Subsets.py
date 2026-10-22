class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def generateSubsets(idx, curr, result):
            if idx == len(nums):
                result.append(curr)
                return
        
            generateSubsets(idx + 1, curr + [nums[idx]], result)
            generateSubsets(idx + 1, curr, result)

        generateSubsets(0, [], result)
        return result