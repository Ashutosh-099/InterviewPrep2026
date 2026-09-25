class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = set()

        for i in range(len(nums)-2):
            p = i + 1
            q = len(nums) - 1

            while p < q: 
                total = nums[i] + nums[p] + nums[q]
                if total == 0:
                    results.add((nums[i], nums[p], nums[q]))
                    p += 1
                    q -= 1
                elif total > 0:
                    q -= 1
                else:
                    p += 1
        
        print(results)
        final = [list(item) for item in results]
        return final