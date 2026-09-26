class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        dic = {0: 1}
        result = 0

        for i in range(len(nums)):
            prefix += nums[i]
            remaining = prefix - k
            
            result += dic.get(remaining, 0)
            
            dic[prefix] = dic.get(prefix, 0) + 1

        return result