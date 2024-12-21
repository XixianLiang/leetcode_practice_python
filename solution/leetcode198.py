from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i < 2:
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        print(dp)
        return dp[-1]


Solution().rob([2, 1, 1, 2])
