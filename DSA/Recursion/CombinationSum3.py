# Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:
# 1. There is only use of numerals 1 through 9.
# 2. A single use is made of each number.
# Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.
def generateCombinations(k, n, idx, curr, result):
    if len(curr) == k:
        if n == 0:
            result.append(curr)
        return
    
    if n < 0 or idx > 9:
        return
    
    generateCombinations(k, n - idx, idx + 1, curr + [idx], result)
    generateCombinations(k, n, idx + 1, curr, result)


def combinationSum3(k, n):
    result = []
    generateCombinations(k, n, 1, [], result)
    return result

# Example Usage
print(combinationSum3(3, 9))
