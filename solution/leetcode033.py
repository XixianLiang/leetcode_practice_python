from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        k = self.find_switch(nums)
        if nums[0] <= target:
            return self.bi_search(nums, 0, k, target)
        else:
            return self.bi_search(nums, k+1, len(nums)-1, target)
        
    def bi_search(self, nums, i, j, target):
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return -1

    def find_switch(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if m + 1 == len(nums) or nums[m + 1] < nums[m]:
                return m
            elif nums[m] > nums[i] and nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[i] and nums[m] < nums[j]:
                j = m - 1
            else:
                # 数组是严格顺序的
                return j


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([0, 1, 2, 4, 5, 6, 7], 3))
