from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        prev_lt = []
        later_lt = []
        for num in nums:
            acc *= num
            prev_lt.append(acc)
        
        acc = 1
        for num in reversed(nums):
            acc *= num
            later_lt.insert(0, acc)
        
        ans = []
        for i in range(len(nums)):
            prev_acc = prev_lt[i - 1] if i >= 1 else 1
            later_acc = later_lt[i + 1] if i < len(nums) - 1 else 1
            ans.append(prev_acc*later_acc)
        
        print(ans)
        return ans

Solution().productExceptSelf([1,2,3,4])