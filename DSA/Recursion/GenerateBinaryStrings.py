# Generate Binary Strings Without Consecutive 1s
# Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.

class Solution:
    def generate(self, result, s, index, n):
        if index == n:
            result.append(s)
            return
        
        if index != 0:
            if s[-1] == '0':
                self.generate(result, s + '0', index + 1, n)
                self.generate(result, s + '1', index + 1, n)
            else:
                self.generate(result, s + '0', index + 1, n)
        else:
            self.generate(result, '0', index + 1, n)
            self.generate(result, '1', index + 1, n)

    def generateBinaryStrings(self, n):
        # Your code goes here
        result = []
        self.generate(result, "", 0, n)

        print(result)
        return result
    
# Optimization:
class Solution:
    def generate(self, result, s, n):
        if len(s) == n:
            result.append(s)
            return
        
        self.generate(result, s + '0', n)
        if not s or s[-1] != '1':
            self.generate(result, s + '1', n)

    def generateBinaryStrings(self, n):
        # Your code goes here
        result = []
        self.generate(result, "", n)

        print(result)
        return result