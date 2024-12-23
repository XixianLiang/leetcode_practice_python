from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.length = len(nums)
        self.nums = nums
        self.backtracking(0, [])
        return self.ans

    def backtracking(self, begin, ans: List[int]):
        self.ans.append(ans[:])
        for i in range(begin, self.length):
            ans.append(self.nums[i])
            self.backtracking(i + 1, ans)
            ans.pop(-1)


print(Solution().subsets([3, 2, 1]))
