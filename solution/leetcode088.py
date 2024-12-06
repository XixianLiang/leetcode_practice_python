from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        import copy
        nums1_ = copy.copy(nums1)
        i = j = 0
        while i + j < m + n:
            if i == m:
                for _ in range(m + n - i - j):
                    nums1[i + j] = nums2[j]
                    j += 1
                return
            if j == n:
                for _ in range(m + n - i - j):
                    nums1[i + j] = nums1_[i]
                    i += 1
                return
            if nums1_[i] < nums2[j]:
                nums1[i + j] = nums1_[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

# print(Solution().merge(nums1, 3, nums2, 3))    
print(Solution().merge([2, 0], 1, [1], 1))    