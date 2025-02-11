from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        ans = int(10e6)
        i = 0
        j = 0
        while j <= len(nums):
            while cur_sum < target and j < len(nums):
                cur_sum += nums[j]
                j += 1
            if cur_sum >= target:
                ans = min(ans, j - i)
            if i >= len(nums):
                break
            cur_sum -= nums[i]
            i += 1
        
        return ans if ans < 10e6 else 0
    
lt = [1, 2, 3, 4, 5]
target = 11
print(Solution().minSubArrayLen(target, lt))