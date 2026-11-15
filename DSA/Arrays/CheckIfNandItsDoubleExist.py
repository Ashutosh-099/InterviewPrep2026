class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        unique = {}

        for i in range(len(arr)):
            can1 = arr[i] * 2
            can2 = arr[i] // 2

            if can1 in unique:
                return True
            
            if arr[i] % 2 == 0 and can2 in unique:
                return True

            unique[arr[i]] = i

        return False