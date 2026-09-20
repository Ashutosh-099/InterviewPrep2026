def checkSubsequenceWithSumK(arr, idx, k, sum) -> bool:
    if idx == len(arr):
        return sum == k
    
    return checkSubsequenceWithSumK(arr, idx + 1, k, sum + arr[idx]) or checkSubsequenceWithSumK(arr, idx + 1, k, sum)


def isSubsequenceWithSumK(arr, k) -> bool:
    return checkSubsequenceWithSumK(arr, 0, k, 0)

# Example usage
arr = [4, 3, 9, 2]
k = 10
print(isSubsequenceWithSumK(arr, k))