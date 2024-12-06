from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        print(id(nums))

        k = k % len(nums)
        temp = nums[-k:]
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]
        
        for i, num in enumerate(temp):
            nums[i] = num
        
        print(nums)
        print(id(nums))

Solution().rotate([1,2,3,4,5,6,7], 3)
        