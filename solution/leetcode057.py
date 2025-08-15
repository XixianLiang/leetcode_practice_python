from typing import List


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         if not intervals:
#             return [newInterval]
        
#         def bisearch(target, index):
#             nonlocal intervals
#             i, j = 0, len(intervals) - 1
            
#             while i <= j:
#                 m = (i + j) // 2
#                 if intervals[m][index] == target:
#                     return m
#                 elif intervals[m][index] < target:
#                     i = m + 1
#                 else:
#                     j = m - 1
#             return i

#         left_A = bisearch(newInterval[0], 0)
#         right_A = bisearch(newInterval[1], 0)
#         left_B = bisearch(newInterval[0], 1)
#         right_B = bisearch(newInterval[1], 1)
        
#         if left_A == right_A == left_B == right_B:
#             intervals.insert(left_A, newInterval)
        
#         if left_A != left_B:
#             left_most = right_A
        
#         if right_A != right_B:
            
        
#         return intervals
        


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        _start, _end = intervals[0]
        ans = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= _end:
                _end = max(intervals[i][1], _end)
                continue
            ans.append([_start, _end])
            _start, _end = intervals[i]
        ans.append([_start, _end])
        
        return ans
            



print(Solution().insert([[1, 3], [6, 9]], [0, 1]))