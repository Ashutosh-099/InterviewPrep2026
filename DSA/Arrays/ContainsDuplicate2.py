class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq and i - freq[nums[i]] <= k:
                return True
            else:
                freq[nums[i]] = i

        return False    