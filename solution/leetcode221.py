from typing import List
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         self.matrix = matrix
#         self.max_square_a = 0
#         self.a = len(matrix[0])
#         self.h = len(matrix)
#         for i0 in range(self.h):
#             if i0 + self.max_square_a >= self.h:
#                 continue
#             for j0 in range(self.a):
#                 if j0 + self.max_square_a >= self.a:
#                     continue
#                 if self.matrix[i0][j0] == "1":
#                     self.max_square_a = max(self.max_square_a, 1)
#                     self.max_square_a = self.get_bigger_square(i0, j0)

#         print(self.max_square_a)
#         return self.max_square_a ** 2


#     def get_bigger_square(self, i0, j0):
#         for i in range(self.max_square_a):
#             for j in range(self.max_square_a):
#                 if self.matrix[i0 + i][j0 + j] != "1":
#                     return self.max_square_a
                
#         try_a = self.max_square_a + 1
#         while i0 + try_a <= self.h and j0 + try_a <= self.a:
#             for i in range(try_a):
#                 if self.matrix[i0 + try_a - 1][i + j0] != "1":
#                     return self.max_square_a
#                 if self.matrix[i + i0][j0 + try_a - 1] != "1":
#                     return self.max_square_a
#             self.max_square_a = try_a
#             try_a += 1
        
#         return self.max_square_a


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        
        max_a = 0
        for i in range(len(matrix)):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            if dp[i][0]:
                max_a = 1
        for j in range(len(matrix[0])):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            if dp[0][j]:
                max_a = 1
 

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                elif dp[i-1][j] == dp[i-1][j-1] and dp[i-1][j-1] == dp[i][j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_a = max(max_a, dp[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        
        return max_a ** 2

temp = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# temp = [["0","1"],["1","0"]]

Solution().maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])
Solution().maximalSquare(temp)