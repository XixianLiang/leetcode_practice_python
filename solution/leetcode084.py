from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 等价于右边有一个高度为0的矩形
        heights.append(0)
        mono_stack = []
        
        ans = 0
        
        for i, height in enumerate(heights):
            
            if len(mono_stack) == 0 or height >= heights[mono_stack[-1]]:
                mono_stack.append(i)
                if i != len(heights):
                    continue
            
            # left_most很关键，要想明白是哪些部分能确定。
            while mono_stack and heights[mono_stack[-1]] > height:
                cur_height_i = mono_stack.pop()
                left_most = -1 if not mono_stack else mono_stack[-1]
                ans = max((i - 1 - left_most) * heights[cur_height_i], ans)
            
            mono_stack.append(i)
        
        return ans

print(Solution().largestRectangleArea([2,1,2]))