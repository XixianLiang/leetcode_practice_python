from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = dict()
        for num in nums:
            ans[num] = ans.get(num, 0) + 1
            if ans[num] == 2:
                del ans[num]
        return list(ans.keys()).pop()
