def subsets(nums, idx, sum, result):
    if idx == len(nums):
        result.append(sum)
        return
    subsets(nums, idx + 1, sum + nums[idx], result)
    subsets(nums, idx + 1, sum, result)

def subsetSum(nums) -> list[int]:
    result = []
    subsets(nums, 0, 0, result)
    return result


# Example usage
print(subsetSum([5, 2, 1]))  # Output: [0, 2, 3, 5]