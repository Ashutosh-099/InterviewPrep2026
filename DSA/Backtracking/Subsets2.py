class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        unique = set()
        curr = []

        def makeSub(idx):
            if idx == len(nums):
                tup = tuple(curr[:])
                unique.add(tup)
                return
            
            curr.append(nums[idx])
            makeSub(idx + 1)
            curr.pop()
            makeSub(idx + 1)

        makeSub(0)
        result = [list(item) for item in unique]
        return result