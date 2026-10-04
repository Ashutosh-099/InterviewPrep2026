from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k = len(p)
        count = len(p)
        freq = Counter(p)
        left = 0
        result = []

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] -= 1
                if freq[s[i]] >= 0:
                    count -= 1

            if (i - left + 1) == k:
                if count == 0:
                    result.append(left)

                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        count += 1
                left += 1
                

        return result