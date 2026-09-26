class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        dic = {}
        dic[0] = -1
        result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in dic:
                result = max(result, i - dic[count])
            else:
                dic[count] = i

        return result