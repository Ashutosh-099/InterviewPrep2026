class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        curr = []

        def generate(idx):
            if len(curr) == k:
                result.append(curr[:])
                return

            for i in range(idx, n+1):
                curr.append(i)
                generate(i + 1)
                curr.pop()

        generate(1)
        return result