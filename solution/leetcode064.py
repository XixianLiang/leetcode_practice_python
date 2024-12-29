from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for col in range(1, len(grid[0])):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
        for row in range(1, len(grid)):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]