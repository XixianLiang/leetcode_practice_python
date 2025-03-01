from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row_0 = col_0 = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                col_0 = True
        
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                row_0 = True

        
        print(col_0, row_0)
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        # for row in row_0:
        #     for j in range(len(matrix[0])):
        #         matrix[row][j] = 0
                
        # for col in col_0:
        #     for i in range(len(matrix)):
        #         matrix[i][col] = 0
        
        if col_0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if row_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
# nums = [[0,1,2,0],
#         [3,4,5,2],
#         [1,3,1,5]]

nums = [[1, 0]]

Solution().setZeroes(nums)
for row in nums:
    print(row)