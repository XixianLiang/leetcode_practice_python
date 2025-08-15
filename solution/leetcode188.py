from typing import List


class Solution:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(2*k + 1)]
        
        for i in range(1, 2*k+1, 2):
            dp[i][0] = -prices[0]
            dp[i][0] = - prices[0]
        
        for i in range(1, 2*k+1):
            for j in range(1, n):
                # buy something
                if i % 2 == 1:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j] - prices[j])
                # sell something
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j] + prices[j])
        
        return dp[-1][-1]