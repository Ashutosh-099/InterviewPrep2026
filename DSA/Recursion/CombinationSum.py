def generateCombinations(nums, idx, target, curr, result):
    if target == 0:
        result.append(curr)
        return
    
    if idx == len(nums) or target < 0:
        return
    
    # Include the element one time
    generateCombinations(nums, idx, target - nums[idx], curr + [nums[idx]], result)
    # Not Include the element
    generateCombinations(nums, idx + 1, target, curr, result)


def combinationSum(nums, target):
    result = []
    generateCombinations(nums, 0, target, [], result)
    print(result)


# Example Usage
combinationSum([2, 3, 5], 8)
