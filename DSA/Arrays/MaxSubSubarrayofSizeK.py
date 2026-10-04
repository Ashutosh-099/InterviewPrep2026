class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        window = sum(arr[:k])
        best = window
        
        for right in range(k, len(arr)):
            window += arr[right] - arr[right - k]
            best = max(best, window)
            
        return best
    
# Alternative Code
class Solution:
    def maxSubarraySum(self, arr, k):
        window = 0
        result = 0
        left = 0
        
        for index, value in enumerate(arr):
            window += value
                
            if (index - left + 1) == k:
                result = max(result, window)
                
                window -= arr[left]
                left += 1
                
        return result