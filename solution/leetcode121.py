from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i, price in enumerate(prices):
            min_price = min(price, min_price)
            max_profit = max(price, min_price)
        
        return max_profit

Solution().maxProfit([7,1,5,3,6,4])