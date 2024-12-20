from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i
                
        
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
print(Solution().removeElement([3, 2, 2, 3], 3))