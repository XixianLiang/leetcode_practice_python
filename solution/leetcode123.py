from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def calProfit(_prices):
            n = len(_prices)
            ans = 0

            max_price = [0 for _ in range(n)]
            max_price[-1] = _prices[-1]

            for i in reversed(range(n-1)):
                max_price[i] = max(max_price[i+1], _prices[i])
            
            for j in range(n - 1):
                ans = max(ans, max_price[j+1] - _prices[j])
            return ans
        
        ans = calProfit(prices)
        
        # 左闭右开
        for i in range(2, len(prices) - 1):
            ans = max(
                ans,
                calProfit(prices[:i]) + calProfit(prices[i:])
            )
        return ans


Solution().maxProfit([3,3,5,0,0,3,1,4])
