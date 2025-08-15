"""
https://mp.weixin.qq.com/s/9KRAsTYGwG2ejIoxYhw-FQ
"""

from collections import Counter, deque
from typing import List


class Solution:

    def find_max(self, nums:List[int]):
        
        counts = dict()
        digits = list()
        
        def counts_num(num):
            nonlocal counts
            n = len(str(num))
            for i in reversed(range(n)):
                counts[i] = counts.get(i, 0) + 1
        
        for num in nums:
            counts_num(num)
            
            for k, v in Counter(str(num)).items():
                digits.extend(int(k) for _ in range(v))
                
        digits = deque(sorted(digits))
        # print(digits)
        
        ans = 0
        # bit for 数位
        for bit, n in sorted(counts.items(), key= lambda x: x[0], reverse=True):
            for _ in range(n):
                # print(f"bit:{bit}, n:{n}, deque:{digits}")
                ans += pow(10, bit) * digits.pop()
        
        return ans
            
print(Solution().find_max([4, 7, 1, 9]))
    