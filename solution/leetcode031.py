from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p = -1
        for i in reversed(range(1, len(nums))):
            if nums[i - 1] < nums[i]:
                p = i - 1
                break
        # 全部降序
        if p == -1:
            nums.sort()
            return
        
        for i in reversed(range(p + 1, len(nums))):
            if nums[i] > nums[p]:
                nums[p], nums[i] = nums[i], nums[p]    
                break
        
        def partition(arr, i, j):
            pos = arr[i]
            l = i
            r = j
            while l < r:
                while l < r and arr[r] > pos:
                    r -= 1
                arr[l], arr[r] = arr[r], arr[l]
                while l < r and arr[l] <= pos:
                    l += 1
                arr[l], arr[r] = arr[l], arr[l]
            arr[l] = pos 
            return l

        def quicksort(arr, i, j):
            if i >= j:
                return
            p = partition(arr, i, j)
            quicksort(arr, i, p - 1)
            quicksort(arr, p + 1, j)
        
        quicksort(nums, p + 1, len(nums) - 1)
            

arr = [1, 3, 2]
Solution().nextPermutation(arr)
print(arr) 
       
# def partition(arr, i, j):
#     pos = arr[i]
#     l = i
#     r = j
#     while l < r:
#         while l < r and arr[r] > pos:
#             r -= 1
#         arr[l], arr[r] = arr[r], arr[l]
#         while l < r and arr[l] <= pos:
#             l += 1
#         arr[l], arr[r] = arr[l], arr[l]
#     arr[l] = pos 
#     return l

# def quicksort(arr, i, j):
#     if i >= j:
#         return
#     p = partition(arr, i, j)
#     quicksort(arr, i, p - 1)
#     quicksort(arr, p + 1, j)


# from hypothesis import given, strategies as st
# from copy import deepcopy
# @given(st.lists(st.integers()))
# def test_custom_sort(lt):
#     lt1 = deepcopy(lt)
#     quicksort(lt1, 0, len(lt) - 1)
#     # 验证输出是否是非递减顺序
#     assert lt1 == sorted(lt)
#     # 验证输出是否是相同元素构成
#     assert sorted(lt1) == sorted(lt)
#     print(lt)
#     print(lt1)

# # 在你的主程序或测试框架中运行测试
# if __name__ == "__main__":
#     test_custom_sort()