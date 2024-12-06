from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        current_stage = max_stage = steps = 0

        while current_stage < max_stage + 1:
            if nums[current_stage] + current_stage > max_stage:
                for i in range(current_stage, max_stage + 1):
                    current_stage = i
                    max_stage = max(nums[current_stage] + current_stage, max_stage)
                steps += 1
            current_stage += 1

            if max_stage >= len(nums) - 1:
                return steps

print(Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(Solution().jump([2,3,0,1,4]))