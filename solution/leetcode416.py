from typing import List
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        nums_tuple = tuple(nums)
        return self.traceback(nums_tuple, target)

        
    @cache
    def traceback(self, nums_tuple, target):
        ans = False
        for i in range(len(nums_tuple)):
            if nums_tuple[i] == target:
                return True
            if nums_tuple[i] < target:
                new_nums_tuple = nums_tuple[:i] + nums_tuple[i+1:]
                ans = ans or self.traceback(new_nums_tuple, target-nums_tuple[i])
                
        return ans

print(Solution().canPartition([1, 2, 3]))            
