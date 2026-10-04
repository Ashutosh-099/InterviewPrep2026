class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i:int, j: int, k:int) -> bool:
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if word[k] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1):
                return True

            board[i][j] = temp

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                    if board[i][j] == word[0] and backtrack(i, j, 0):
                        return True
        
        return False
        