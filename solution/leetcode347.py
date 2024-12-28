from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        ans = []

        c = Counter(nums)
        for m in c.most_common(k):
            ans.append(m[0])

        return ans


Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3], 2)
