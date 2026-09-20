def checkSubsequenceWithSumK(arr, idx, k, sum):
    if idx == len(arr):
        return 1 if sum == k else 0
    
    return checkSubsequenceWithSumK(arr, idx + 1, k, sum + arr[idx]) + checkSubsequenceWithSumK(arr, idx + 1, k, sum)
    checkSubsequenceWithSumK(arr, idx + 1, k, sum, count)


def isSubsequenceWithSumK(arr, k) -> bool:
    count = checkSubsequenceWithSumK(arr, 0, k, 0)
    return count

# Example usage
arr = [4, 9, 2, 5, 1]
k = 10
print(isSubsequenceWithSumK(arr, k))