from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.pick([], [False] * len(nums))
        return self.res

    def pick(self, cur_res: List[int], picked: List[bool]):
        if all(picked):
            self.res.append(cur_res[:])
        for i, has_picked in enumerate(picked):
            if not has_picked:
                picked[i] = True
                cur_res.append(self.nums[i])
                self.pick(cur_res, picked)
                cur_res.pop(-1)
                picked[i] = False


print(Solution().permute([0, 1, 2]))
