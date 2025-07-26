from re import L
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        
        
        dp = [[[0, 0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        dp[0][0] = [1, 1] if matrix[0][0] else [0, 0]
        
        ans = matrix[0][0]
        
        for i in range(1, len(matrix)):
            if matrix[i][0]:
                dp[i][0] = [
                    dp[i - 1][0][0] + 1, 
                    1 if any(dp[i - 1][0]) else 0
                ]
                ans = max(ans, dp[i][0][0] * dp[i][0][1])
            else:
                dp[i][0] = [0, 0]
                
        for j in range(1, len(matrix)):
            if matrix[0][j]:
                dp[0][j] = [
                    dp[0][j][1] + 1, 
                    1 if any(dp[j - 1][0]) else 0
                ]
                ans = max(ans, dp[0][j][0] * dp[0][j][1])
            else:
                dp[0][j] = [0, 0]
        
        dp
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    dp[i][j] = [
                        dp[i-1][j][0] + 1,
                        dp[i][j-1][1] + 1
                    ]
                    ans = max(ans, dp[i][j][0] * dp[i][j][1])
                else:
                    dp[i][j] = [0, 0]
        
        return ans
                

print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))