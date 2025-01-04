from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
            
        p = len(nums) - 1
        for j in reversed(range(len(nums))):
            if nums[j] == 2:
                nums[p], nums[j] = nums[j], nums[p]
                p -= 1
        
        print(nums)

Solution().sortColors([2,1,0,1,2,1,0])