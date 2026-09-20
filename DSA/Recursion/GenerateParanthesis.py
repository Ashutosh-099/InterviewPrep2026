class Solution:
    def generate(self, s: str, opening:int, closing:int, size:int, result: list[str]) -> None:
        if len(s) == 2 * size:
            result.append(s)
            return

        if opening < size:
            self.generate(s + "(", opening + 1, closing, size, result)
        if closing < opening:
            self.generate(s + ")", opening, closing + 1, size, result)

    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.generate("", 0, 0, n, result)

        return result