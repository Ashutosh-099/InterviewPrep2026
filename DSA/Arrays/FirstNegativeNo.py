class Solution:
    def firstNegInt(self, arr, k): 
        # code here 
        left = 0
        negList = []
        result = []
        
        for i in range(len(arr)):
            if arr[i] < 0:
                negList.append(arr[i])
                
            if (i - left + 1) == k:
                # Calculate the answer
                if len(negList) == 0:
                    result.append(0)
                else:
                    result.append(negList[0])
                    if negList[0] == arr[left]:
                        negList.pop(0)
                left += 1
            
        return result    