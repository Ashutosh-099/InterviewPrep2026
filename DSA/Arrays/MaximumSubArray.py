# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Kadane's Algorithm is an efficient way to solve this problem in O(n) time complexity.
# Kadane's Algorithm works by iterating through the array and keeping track of the maximum sum of the subarray that ends at the current index. If the current sum becomes negative, we reset it to zero, as a negative sum would not contribute to a maximum subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxRes = float('-inf')
        startIndex = 0
        endIndex = -1
        count = 0

        for i in range(len(nums)):
            count += nums[i]
            if count > maxRes :
                maxRes = count
                endIndex = i

            if count < 0:
                count = 0
                startIndex = i
        print(f"Start Index: {startIndex + 1}, End Index: {endIndex}")
        return maxRes
    

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))  # Output: 6, Start Index: 3, End Index: 6