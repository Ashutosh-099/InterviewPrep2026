# Rotate Array by K Positions to the Left
def rotate_array_by_k(nums, k):
    if len(nums) < 2:
            return
    k %= len(nums)
    temp = nums[:k]

    for i in range(k, len(nums)):
        nums[i - k] = nums[i]

    j = 0
    for i in range(len(nums) - k, len(nums)):
        nums[i] = temp[j]
        j += 1

    return


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    print("Original array:", arr)
    rotate_array_by_k(arr, k)
    print(f"Array after left rotation by {k} positions:", arr)