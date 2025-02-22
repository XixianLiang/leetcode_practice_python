from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        q = dict()
        for i, num in enumerate(nums2):
            while mono_stack and nums2[mono_stack[-1]] < num:
                r = mono_stack.pop()
                q[nums2[r]] = num
            mono_stack.append(i)
        
        return [q.get(_, -1) for _ in nums1]

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))