# Given collection of candidate numbers (candidates) and a integer target.Find all unique combinations in candidates where the sum is equal to the target.There can only be one usage of each number in the candidates combination and return the answer in sorted order. E.g : The combination [1, 1, 2] and [1, 2, 1] are not unique.

def combinations(nums, idx, target, curr, result):
    if target == 0:
        result.append(curr)
        return
    
    if idx == len(nums) or target < 0:
        return
    
    
    combinations(nums, idx + 1, target - nums[idx], curr + [nums[idx]], result)
    next_idx = idx + 1
    while next_idx < len(nums) and nums[next_idx] == nums[idx]:
        next_idx += 1
    combinations(nums, next_idx, target, curr, result)

def generateCombinations(nums, target):
    result = []
    nums.sort()
    combinations(nums, 0, target, [], result)
    return result

# Example usage
print(generateCombinations([2, 1, 2, 7, 6, 1, 5], 8))