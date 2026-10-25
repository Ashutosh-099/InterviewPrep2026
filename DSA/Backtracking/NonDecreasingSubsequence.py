class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        curr = []
        unique = set()

        def generateSub(start):
            if len(curr) >= 2:
                unique.add(tuple(curr))

            if start == len(nums):
                return

            for i in range(start, len(nums)):
                if len(curr) == 0 or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                    generateSub(i + 1)
                    curr.pop()
            return

        generateSub(0)
        return [list(item) for item in unique]

        
# Avoid Duplicate with Optimization: Set inside each recursion
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        curr = []
        res = []

        def generateSub(start):
            if len(curr) >= 2:
                res.append(curr[:])

            unique = set()
            for i in range(start, len(nums)):
                if len(curr) == 0 or nums[i] >= curr[-1]:
                    if nums[i] not in unique:
                        unique.add(nums[i])
                        curr.append(nums[i])
                        generateSub(i + 1)
                        curr.pop()
            return

        generateSub(0)
        return res

        