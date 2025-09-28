from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        cnt = [0 for _ in range(len(nums))]
        cnt[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 >= dp[i]:
                        dp[i] = dp[j] + 1
                        if dp[j] + 1 > dp[i]:
                            cnt[i] = 1
                        else:
                            cnt[i] = cnt[i] + cnt[j]
        return max(cnt)


Solution().findNumberOfLIS([1,3,5,4,7])