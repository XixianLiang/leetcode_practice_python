from typing import List
import random
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify([-(_) for _ in nums])
        ans = None
        for i in range(k):
            ans = heapq.heappop()
        return ans
    
    
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(i, j):
#             if i >= j:
#                 return
#             nonlocal nums, k
#             p = random.randint(i, j)
#             nums[p], nums[i] = nums[i], nums[p]
#             pivot = nums[i]
#             l, r = i, j
#             while l < r:
#                 while l < r and nums[r] >= pivot:
#                     r -= 1
#                 nums[l], nums[r] = nums[r], nums[l]
#                 while l < r and nums[l] <= pivot:
#                     l += 1
#                 nums[l], nums[r] = nums[r], nums[l]
#             nums[l] = pivot
#             return l

#         def quicksort(i, j):
#             nonlocal nums, k
#             if i >= j:
#                 return
#             p = partition(i, j)
#             if p == len(nums) - k:
#                 return
#             if p > len(nums) - k:
#                 quicksort(i, p-1)
#             if p < len(nums) - k:
#                 quicksort(p+1, j)
        
#         quicksort(0, len(nums) - 1)
#         return nums[-k]
    
print(Solution().findKthLargest([3,2,1,5,6,4], 2))