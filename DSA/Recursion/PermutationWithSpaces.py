# Given a string s, generate all possible strings by optionally inserting a single space between every pair of adjacent characters. Return all such strings in lexicographically increasing order.

class Solution:
    def generatePermutation(self, s, curr, result):
        if s == "":
            result.append(curr)
            return
        
        char = s[0]
        self.generatePermutation(s[1:], curr + " " + char, result)
        self.generatePermutation(s[1:], curr + char, result)
        
    def permutation(self, s):
        # code here
        result = []
        
        curr = s[0]
        self.generatePermutation(s[1:], curr, result)
        
        return result
        