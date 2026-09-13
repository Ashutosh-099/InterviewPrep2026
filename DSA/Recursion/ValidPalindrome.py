# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def check(self, s:str, index:int) -> bool:
        if index >= len(s) - index - 1:
            return True

        return s[index] == s[len(s) - index - 1] and self.check(s, index+1)

    def removeSpace(self, s:str) -> str:
        if s == "":
            return ''

        value = s[-1].lower() if s[-1].isalnum() else ""
        return self.removeSpace(s[:-1]) + value

    def isPalindrome(self, s: str) -> bool:
        s = s.strip()

        if s == "" or len(s) == 1:
            return True

        s = self.removeSpace(s)
        return self.check(s, 0)
        