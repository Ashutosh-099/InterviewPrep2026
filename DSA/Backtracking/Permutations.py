class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def generate(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                generate(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        generate(0)
        return result