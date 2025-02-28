from typing import List

from pandas import pivot
from pyparsing import nums


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        c = list(counts.items())
        
        def quicksort(i, j):
            if i >= j:
                return
            nonlocal c, k
            
            p = partition(i, j)
            if p == len(c) - k:
                return True
            quicksort(i, p-1)
            if p > len(c) - k:
                return
            quicksort(p+1, j)
            
        
        def partition(i, j):
            nonlocal c
            l, r = i, j
            pivot = c[i]
            while l < r:
                while l < r and c[r][1] >= pivot[1]:
                    r -= 1
                c[l], c[r] = c[r], c[l]
                while l < r and c[l][1] <= pivot[1]:
                    l += 1
                c[l], c[r] = c[r], c[l]
            c[l] = pivot
            return l

        quicksort(0, len(c) - 1)
        return [_[0] for _ in c[-k:]]
     
[2, 5, 3, 4, 1]
2

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 7,7,7,7,7, 0], 2))
