from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        squares = []
        i = 1
        while i <= n:
            squares.append(i**2)
            i += 1

        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for j in range(2, n + 1):
            dp[j] = min(dp[j - square] + 1 for square in squares if square <= j)
        return dp[-1]


print(Solution().numSquares(5756))
