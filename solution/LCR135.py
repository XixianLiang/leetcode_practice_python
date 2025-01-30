from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        return [_ for _ in range(1, 10 ** cnt)]

print(Solution().countNumbers(2))