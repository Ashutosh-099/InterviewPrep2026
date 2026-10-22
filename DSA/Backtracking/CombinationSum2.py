class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        unique = set()
        curr = []

        def makeComb(idx, remain):
            if remain == 0:
                unique.add(tuple(curr[:]))
                return

            if idx == len(candidates) or candidates[idx] > remain:
                return
            
            curr.append(candidates[idx])
            makeComb(idx + 1, remain - candidates[idx])
            curr.pop()
            nxt = idx + 1
            # Important to avoid TLE
            while nxt < len(candidates) and candidates[nxt] == candidates[idx]:
                nxt += 1
            makeComb(nxt, remain)

        makeComb(0, target)
        result = [list(item) for item in unique]
        return result

        
        