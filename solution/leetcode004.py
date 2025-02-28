from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2 
        
        sep_total = (len(nums1) + len(nums2) + 1) // 2
        total_is_odd = (len(nums1) + len(nums2)) % 2 == 1
        
        nums1.insert(0, -float("inf"))
        nums1.append(float("inf"))
        nums2.insert(0, -float("inf"))
        nums2.append(float("inf"))
        
        def valid_seperate(m1, m2):
            nonlocal nums1, nums2
            a = nums1[m1] <= nums2[m2 + 1]
            b = nums1[m1 + 1] >= nums2[m2]
            return a and b 
        
        # nums2 is the shorter one
        def bisearch(i, j):
            nonlocal nums1, nums2
            while i < j:
                m2 = (i + j) // 2
                m1 = sep_total - m2
                if valid_seperate(m1, m2):
                    return m2
                else:
                    # 给 nums2 分的少了
                    if nums1[m1] > nums2[m2 + 1]:
                        i = m2 + 1
                    else:
                        j = m2 - 1
            return i
        
        m2 = bisearch(0, len(nums2) - 1) if sep_total > 0 else 0
        m1 = sep_total - m2
        
        left_partition_max = max(nums1[m1], nums2[m2])
        right_partition_min = min(nums1[m1 + 1], nums2[m2 + 1])
        if total_is_odd:
            return left_partition_max
        else:
            return (left_partition_max + right_partition_min) / 2



print(Solution().findMedianSortedArrays([4, 5, 6], [1, 2, 3]))
print(Solution().findMedianSortedArrays([1,2], [3,4]))
print(Solution().findMedianSortedArrays([1], [1]))
print(Solution().findMedianSortedArrays([0,0], [0,0]))
print(Solution().findMedianSortedArrays([1,3], [2]))
