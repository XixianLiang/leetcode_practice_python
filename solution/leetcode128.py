from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                while cur_num in nums_set:
                    ans = max(ans, cur_num - num + 1)
                    cur_num += 1
        return ans


print(Solution().longestConsecutive([1, 1, 1]))
