# https://www.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1
class Solution:
    def generateBitBinary(self, zeros, ones, n, curr, result):
        if n == 0:
            result.append(curr)
            return result
            
        if ones > zeros:
            self.generateBitBinary(zeros+1, ones, n - 1, curr + "0", result)
        self.generateBitBinary(zeros, ones+1, n - 1, curr + "1", result)
        
	
    def nBitBinary(self, n):
		# code here
        result = []
        self.generateBitBinary(0, 0, n, "", result)
        return result
		