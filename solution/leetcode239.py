from typing import List
from collections import UserList


class MonoList(UserList):
    
    def push(self, e):
        if len(self) == 0:
            self.append(e)
            return
        if self[-1] >= e:
            self.append(e)
        else:
            for i in reversed(range(len(self))):
                if self[i] >= e:
                    self.append(e)
                    return
                else:
                    del self[i]
            self.clear()
            self.append(e)
        
    
    def pop(self):
        if self:
            del self[0]
    
    @property
    def max(self):
        return self[0] if self else None



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        monolist = MonoList()
        for i in range(k):
            monolist.push(nums[i])
        
        for i in range(len(nums) - k + 1):
            ans.append(monolist.max)
            if i == len(nums) - k:
                break
            if nums[i] == monolist.max:
                monolist.pop()
            monolist.push(nums[i + k])
        return ans    

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
nums = [-7,-8,7,5,7,1,6,0]
k = 4
print(Solution().maxSlidingWindow(nums, k))