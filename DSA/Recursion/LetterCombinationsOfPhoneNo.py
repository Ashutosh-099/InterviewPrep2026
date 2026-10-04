class Solution:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def generateCombinations(self, digits: str, curr: str, result:list[str]) -> list[str]:
        if digits == "":
            result.append(curr)
            return

        dig = digits[0]
        keys = Solution.letters[dig]
        for value in keys:
            self.generateCombinations(digits[1:], curr + value, result)


    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        self.generateCombinations(digits, "", result)

        return result