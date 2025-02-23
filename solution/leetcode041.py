from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i, num in enumerate(nums):
            if not 0 < num < len(nums) + 1:
                nums[i] = n + 1
        
        for i, num in enumerate(nums):
            if 1 <= abs(num) <= n:
                nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        
        return n + 1
            
print(Solution().firstMissingPositive([3, 4, -1, 1]))
print(Solution().firstMissingPositive([1, 2, 0]))

# [1, 2, 0]
# [4, 5, 3]

# [3, 4, 0, 1]
# [7, 8, 4, 5]
