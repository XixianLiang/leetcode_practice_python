from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.ans = [-1, -1]
        m = self.bi_search(nums, target)
        if m not in range(0, len(nums)) or nums[m] != target:
            pass
        else:
            self.ans = [self.bi_search(nums, target-0.5),
                        self.bi_search(nums, target+0.5) - 1]
        return self.ans

    def bi_search(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return i
        


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         i, j = 0, len(nums) - 1
#         self.ans = [-1, -1]
#         while i <= j:
#             m = (i + j) // 2
#             if nums[m] == target:
#                 self.get_range(m, nums, target)
#                 break
#             elif nums[m] < target:
#                 i = m + 1
#             else:
#                 j = m - 1
#         return self.ans

#     def get_range(self, m, nums, target):
#         i = j = m
#         while True:
#             if i >= 0 and nums[i] == target:
#                 i -= 1
#             else:
#                 self.ans[0] = i + 1
#             if j < len(nums) and nums[j] == target:
#                 j += 1
#             else:
#                 self.ans[1] = j - 1
#             if all(_ != -1 for _ in self.ans):
#                 break


print(Solution().searchRange([2, 2], 3))
