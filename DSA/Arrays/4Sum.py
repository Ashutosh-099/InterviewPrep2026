class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)-3):
            firstNo = nums[i]
            for j in range(i + 1, len(nums)-2):
                secondNo = nums[j]
                p = j + 1
                q = len(nums)-1

                while p < q:
                    value = firstNo + secondNo + nums[p] + nums[q]
                    if value > target:
                        q -= 1
                    elif value < target:
                        p += 1
                    else:
                        sorted_tuple = tuple(sorted((firstNo, secondNo, nums[p], nums[q])))
                        result.add(sorted_tuple)
                        p += 1
                        q -= 1

        final_result = [list(item) for item in result]

        return final_result    