from typing import List, Dict


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]

        for i in range(1, len(dp)):
            for j in range(len(1, dp[0])):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
        
    