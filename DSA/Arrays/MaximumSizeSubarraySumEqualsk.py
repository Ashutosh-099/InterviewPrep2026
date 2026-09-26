# Prefix Sum
# Maximum Size Subarray Sum Equals k
def maximumSizeSubarraySumEqualsK(nums, k):
    dic = {0: -1}
    prefix = 0
    result = 0

    for i, value in enumerate(nums):
        prefix += value
        remain = prefix - k

        if remain in dic:
            size = i - dic[remain]
            result = max(result, size)

        if prefix not in dic:
            dic[prefix] = i
    
    return result


# Example
nums = [2, 3, 4]
k = 10

print(maximumSizeSubarraySumEqualsK(nums, k))