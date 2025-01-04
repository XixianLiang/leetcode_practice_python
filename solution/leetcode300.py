from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        
        ans = 1
        
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j] + 1)
            dp[i] = temp
            ans = max(ans, dp[i])
        
        return ans
                


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))