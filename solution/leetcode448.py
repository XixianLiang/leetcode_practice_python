from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = set([_ for _ in range(1, len(nums) + 1)])
        for num in nums:
            r.discard(num)
        return list(r)
