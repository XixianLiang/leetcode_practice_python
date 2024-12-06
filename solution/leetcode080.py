from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = j = 2
        while(j < len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# print(Solution().removeDuplicates([1,   1,   1,   2, 2, 3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))