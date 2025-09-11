from collections import Counter
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1 = Counter(basket1)
        total = Counter(basket1 + basket2)
        
        target = dict()
        for k, v in total.items():
            if v % 2 != 0:
                return -1
            target[k] = v // 2
        
        swaps = 0
        for k, v in target.items():
            swaps += abs(b1.get(k, 0) - v)
        
        swaps = swaps // 2 
        
        if swaps == 0:
            return 0
        
        min_value = min(target.keys())
        
        ans = 0
        for k, v in sorted(target.items()):
            counts_abstract = abs(b1[k] - v)
            if counts_abstract == 0:
                continue
            takes = min(counts_abstract, v)
            ans += counts_abstract * min(k, 2*min_value)
            swaps -= takes
            if swaps == 0:
                break
        return ans


print(
        Solution().minCost(
        [84,80,43,8,80,88,43,14,100,88],
        [32,32,42,68,68,100,42,84,14,8]
    )
)