class Solution:
    def isVowel(self, char: str) -> bool:
        return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        curr = 0
        left = 0

        for i in range(len(s)):
            if self.isVowel(s[i]):
                curr += 1

            if (i - left + 1) == k:
                result = max(result, curr)
                if result == k:
                    return result

                if self.isVowel(s[left]):
                    curr -= 1
                left += 1

        return result