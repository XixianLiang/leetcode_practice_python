import collections
from typing import List



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        positive = (total + target) // 2
        if (total + target) % 2 != 0 or positive < 0:
            return 0
        n = len(nums)
        dp = [[0 for _ in range(positive + 1)] for _ in range(n)]
        # j is the size of the pack
        if nums[0] <= positive:
            dp[0][nums[0]] = 1
        # i is the index of the num
        for i in range(n):
            counts_of_0 = collections.Counter(nums[0: i + 1]).get(0, 0)
            dp[i][0] = 2 ** counts_of_0
        for i in range(1, n):
            for j in range(positive + 1): 
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - nums[i]] if j - nums[i] >= 0 else 0)
        return dp[-1][-1]

print(Solution().findTargetSumWays([100], -200))
# print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
