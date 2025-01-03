from typing import List, Set


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.nums = candidates
        self.ans = []
        self.traceback([], target, 0)
        return self.ans
    
    def traceback(self, cur_lt:List[int], target, i0):
        for i in range(i0, len(self.nums)):
            next_target = target - self.nums[i]
            if next_target < 0:
                return
            cur_lt.append(self.nums[i])
            if next_target == 0:
                self.ans.append(cur_lt[:])
            else:
                self.traceback(cur_lt, next_target, i)
            cur_lt.pop(-1)

print(Solution().combinationSum(candidates=[2,3,6,7], target=7))