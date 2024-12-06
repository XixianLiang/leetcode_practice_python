from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_stage = 0
        current_stage = 0
        while current_stage < max_stage + 1:
            if max_stage + 1 >= len(nums):
                return True
            max_stage = max(max_stage, current_stage + nums[current_stage])
            current_stage += 1
        return False

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))


