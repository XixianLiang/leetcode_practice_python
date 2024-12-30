from typing import List


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 初始化左右指针
        left_p = 0
        right_p = len(height) - 1
        
        # 初始化左右边界的高度
        left_height = height[left_p]
        right_height = height[right_p]
        
        # 用于存储总的雨水量
        ans = 0
        
        # 每次计算一个单位上的雨水量
        while left_p < right_p:
            # 如果左边的高度小于右边的高度，左边的雨水量确定。
            if left_height < right_height:
                # 计算当前左侧能存储的雨水量
                ans += (min(left_height, right_height) - height[left_p])
                # 移动左指针向右
                left_p += 1
                # 更新左边的最大高度
                left_height = max(left_height, height[left_p])
            else:
                ans += (min(left_height, right_height) - height[right_p])
                right_p -= 1
                right_height = max(right_height, height[right_p])
        
        # 返回总的雨水量
        return ans

# 测试示例，输入高度列表并输出计算的雨水量
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
