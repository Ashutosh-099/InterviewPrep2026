class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0

        def calculate(idx, curr):
            if idx == len(nums):
                # print("Ending Index, " + str(idx), " Curr", str(curr), " Array" + str(nums))
                return curr

            # print("Index, " + str(idx), " Curr", str(curr), " Array" + str(nums))
            return calculate(idx + 1, curr ^ nums[idx]) + calculate(idx + 1, curr)

        result = calculate(0, 0)
        return result