# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Brute Force
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for p in range(len(matrix)):
                        matrix[p][j] = 0.5 if matrix[p][j] != 0 else 0
                    
                    for q in range(len(matrix[i])):
                        matrix[i][q] = 0.5 if matrix[i][q] != 0 else 0


        print(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0.5:
                    matrix[i][j] = 0

        return