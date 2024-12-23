from typing import List
from collections import Counter


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp


print(Solution().countBits(3))
