# Prefix Sum
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix = 0
        freq = {0: 1}  # base case: a prefix-odd-count of 0 exists before any elements
        result = 0

        for num in nums:
            prefix += num % 2
            target_prefix = prefix - k
            result += freq.get(target_prefix, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return result