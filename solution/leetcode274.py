from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        for i, cite in enumerate(citations):
            if i + 1 >= cite:
                return max(i, cite)
        return len(citations)
print(Solution().hIndex([4, 4, 0, 0]))