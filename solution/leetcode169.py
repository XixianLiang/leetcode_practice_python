from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        return counter.most_common(1)[0][0]