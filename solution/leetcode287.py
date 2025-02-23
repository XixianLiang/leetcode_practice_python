from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

print(Solution().findDuplicate([2, 1, 1]))