class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        curr = []

        def makeComb(idx, tar):
            if tar == 0:
                result.append(curr[:])
                return

            if tar < 0 or idx == len(candidates):
                return

            curr.append(candidates[idx])
            makeComb(idx, tar - candidates[idx])
            curr.pop()
            makeComb(idx + 1, tar)

        makeComb(0, target)
        return result