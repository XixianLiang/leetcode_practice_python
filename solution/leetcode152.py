from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [-float("inf") for _ in range(len(nums) + 1)]
        dp_min = [float("inf") for _ in range(len(nums) + 1)]
        ans = -float("inf")
        for i in range(1, len(nums) + 1):
            cur_num = nums[i - 1]
            if cur_num > 0:
                dp_max[i] = max(dp_max[i - 1] * cur_num, cur_num)
                dp_min[i] = min(dp_min[i - 1] * cur_num, cur_num)
            elif cur_num < 0:
                dp_max[i] = max(dp_min[i - 1] * cur_num, cur_num)
                dp_min[i] = min(dp_max[i - 1] * cur_num, cur_num)
            else:
                dp_max[i] = max(dp_max[i - 1] * cur_num, cur_num)
                dp_min[i] = min(dp_min[i - 1] * cur_num, cur_num)
                if dp_max[i - 1] == -float("inf"):
                    dp_max[i] = 0
                    dp_min[i] = 0
                    
            ans = max(ans, dp_max[i]) 
        return ans

print(Solution().maxProduct([0,0, -3, 1]))