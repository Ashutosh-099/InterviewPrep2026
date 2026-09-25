# Swap Sort
def findMissingRepeatingNumbers(nums):
    for i in range(len(nums)):
        # print("Index", i)
        # print("Index Value", nums[i])
        # print("Swap Value", nums[nums[i] - 1])
        while nums[i] != i + 1:
            if nums[nums[i]-1] == nums[i]:
                break
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp
            # print("After swap", nums)
            
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]


nums = [3, 5, 4, 1, 1]

print(findMissingRepeatingNumbers(nums))