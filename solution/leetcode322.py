from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # 初始化 dp 数组，大小为 amount + 1，初始值为 inf
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # 0 元需要 0 个硬币

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


print(Solution().coinChange([1, 2, 5], 11))
