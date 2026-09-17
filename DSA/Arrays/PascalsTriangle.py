class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        
        for i in range(1, numRows):
            row = []
            for j in range(i+1):
                if j == 0:
                    value = result[i-1][0]
                elif j == i:
                    value = result[i-1][j-1]
                else:
                    value = result[i-1][j-1] + result[i-1][j]
                row.append(value)
            result.append(row)
        
        print(result)
        return result