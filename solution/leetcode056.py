from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        _start, _end = intervals[0]
        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i]
            if new_start > _end:
                ans.append([_start, _end])
                _start, _end = new_start, new_end
            else:
                _end = max(_end, new_end)
            if i == len(intervals) - 1:
                ans.append([_start, _end])
        return ans


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
