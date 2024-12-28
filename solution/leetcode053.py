from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [-float("inf") for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])

        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prefix_sum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        max_sum = float("-inf")

        min_prefix = float("inf")
        for j in range(1, len(prefix_sum)):
            # 计算之前最小子数组和
            min_prefix = min(min_prefix, prefix_sum[j - 1])
            # 计算当前子数组和
            current_sum = prefix_sum[j] - min_prefix
            # 更新最大和
            max_sum = max(max_sum, current_sum)

        return max_sum


# print(Solution().maxSubArray([5, 4, -1, 7, 8]))
print(Solution().maxSubArray([-2, -1]))
