from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            dp = [[1], [1, 1]]
            for row in range(2, numRows):
                dp.append([0 for _ in range(row + 1)])
                dp[row][0] = 1
                dp[row][row] = 1
                for col in range(1, row):
                    dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1]

            return dp


Solution().generate(5)
