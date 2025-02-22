from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_stack = list()
        n = len(nums)
        ans = [-1 for _ in range(n)]
        for i in range(2 * n):
            num = nums[i % n]
            while mono_stack and nums[mono_stack[-1] % n] < num:
                ans_i = mono_stack.pop()
                ans[ans_i % n] = num
            mono_stack.append(i)
        
        return ans

print(Solution().nextGreaterElements([2, 1, 3, 2]))