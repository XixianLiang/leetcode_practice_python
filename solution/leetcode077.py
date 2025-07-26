from collections import deque
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def traceback(i, n, k, cur: deque):
            if k == 0:
                ans.append(list(cur))
                return
            for j in range(i, n - k + 1):
                cur.append(j + 1)
                traceback(j + 1, n, k - 1, cur)
                cur.pop()
        
        traceback(0, n, k, deque())
        return ans


Solution().combine(4, 2)