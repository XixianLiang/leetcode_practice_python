from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = self.bi_search(nums, 0, len(nums) - 1)
        return nums[i]

    def bi_search(self, nums, i, j):
        while i <= j:
            m = (i + j) // 2
            if nums[m] < nums[(m - 1)%len(nums)]:
                return m
            if nums[m] > nums[0] or nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[0] or nums[m] < nums[j]:
                j = m - 1
        return 0


print(Solution().findMin([2, 1]))
