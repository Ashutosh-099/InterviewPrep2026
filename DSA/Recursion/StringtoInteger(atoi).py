# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
class Solution:
    def convertToNo(self, s:str, isNeg:bool, isStart:bool, result:int) -> int:
        if s == "":
            return result if not isNeg else result * -1
            
        char = s[0].strip()

        if (char == "-" or char == "+") and isStart:
            isNeg = True if char == "-" else False
            return self.convertToNo(s[1:], isNeg, False, result)

        if (char == '-' or char == "+") and not isStart:
            return result if not isNeg else result * -1

        if char == "" or not char.isdigit():
            return result if not isNeg else result * -1

        result = result * 10 + int(char) 
        return self.convertToNo(s[1:], isNeg, False, result)


    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = self.convertToNo(s, False, True, 0)
        if res < -(2**31):
            return -(2**31)
        elif res > (2**31 - 1):
            return (2**31 - 1)
        else:
            return res