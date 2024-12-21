from typing import List
import random

class FoundExecption(Exception):
    def __init__(self, *args, ans):
        self.ans = ans
        super().__init__(*args)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        try:
            self.quickSort(nums, 0, len(nums) - 1, k)
            return nums[-k]
        except FoundExecption as e:
            return e.ans


    def quickSort(self, nums: List[int], left: int, right, k):
        if left >= right:
            return
        
        base_index = random.randint(left, right)
        nums[base_index], nums[left] = nums[left], nums[base_index]
        target_index = self.partition(nums, left, right)
        if target_index == len(nums) - k:
            raise FoundExecption(ans=nums[target_index])
        self.quickSort(nums, left, target_index-1, k)
        self.quickSort(nums, target_index+1, right, k)


    def partition(self, nums: List[int], left, right) -> int:
        pivot = nums[left]
        i = left + 1
        j = right

        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        # i is the target index of the element nums[base_index]
        nums[left], nums[j] = nums[j], nums[left]
        return j

# import random
# from typing import List

# class FoundExecption(Exception):
#     def __init__(self, ans):
#         self.ans = ans

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         try:
#             self.quickSort(nums, 0, len(nums) - 1, k)
#         except FoundExecption as e:
#             return e.ans

#     def quickSort(self, nums: List[int], left: int, right: int, k: int):
#         if left >= right:
#             return
        
#         base_index = random.randint(left, right)
#         # 将基准元素放到左边
#         nums[left], nums[base_index] = nums[base_index], nums[left]
#         target_index = self.partition(nums, left, right)

#         # 找到目标元素
#         if target_index == len(nums) - k:
#             raise FoundExecption(ans=nums[target_index])
        
#         # 继续查找
#         self.quickSort(nums, left, target_index - 1, k)
#         self.quickSort(nums, target_index + 1, right, k)

#     def partition(self, nums: List[int], left: int, right: int) -> int:
#         pivot = nums[left]  # 使用左边的元素作为基准
#         i = left + 1
#         j = right

#         while i <= j:
#             while i <= j and nums[i] <= pivot:
#                 i += 1
#             while i <= j and nums[j] >= pivot:
#                 j -= 1
#             if i < j:
#                 nums[i], nums[j] = nums[j], nums[i]

#         # 将基准元素放到正确的位置
#         nums[left], nums[j] = nums[j], nums[left]
#         return j  # 返回基准元素的新位置


print(Solution().findKthLargest([3,2,1,5,6,4], 4))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
        