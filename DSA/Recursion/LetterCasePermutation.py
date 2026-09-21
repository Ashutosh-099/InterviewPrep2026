# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def generatePermutations(self, s, curr, result) -> list[str]:
        if s == "":
            result.append(curr)
            return

        char = s[0]
        if char.isdigit():
            self.generatePermutations(s[1:], curr + char, result)
        else:
            self.generatePermutations(s[1:], curr + char.upper(), result)
            self.generatePermutations(s[1:], curr + char.lower(), result)

    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        self.generatePermutations(s, "", result)
        return result