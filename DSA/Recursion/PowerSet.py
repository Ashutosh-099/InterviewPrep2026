class Solution:
    def power(self, input, idx, output, result):
        if len(input) == idx:
            result.append(output)
            print(output)
            return

        temp = input[idx]

        self.power(input, idx + 1, output, result)
        self.power(input, idx + 1, output + [temp], result)

    def powerSet(self, nums):
        #your code goes here
        if len(nums) == 0:
            return []
        
        result = []
        self.power(nums, 0, [], result)
        return result
        
# Example Usage
sol = Solution()
sol.powerSet([1, 2, 3])