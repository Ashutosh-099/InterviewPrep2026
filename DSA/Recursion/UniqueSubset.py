# Given an integer array nums, which can have duplicate entries, provide the power set.

def unique(nums, idx, curr, result):
    if len(nums) == idx:
        result.add(tuple(curr))
        return

    unique(nums, idx + 1, curr + [nums[idx]], result)
    unique(nums, idx + 1, curr, result)

def unique_subsets(nums):
    result = set()
    unique(nums, 0, [], result)

    print([list(item) for item in result])


# Example usage
nums = [1, 2, 2]
unique_subsets(nums)