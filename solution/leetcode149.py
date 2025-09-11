from fractions import Fraction

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def cal_K(a, b):
            if a[0] == b[0]:
                return float("inf")
            return Fraction(
                a[1] - b[1], a[0] - b[0]
            )
        
        ans = 2
        for i in range(len(points)):
            hash_map = dict()
            for j in range(len(points)):
                if i == j:
                    continue
                k = cal_K(points[i], points[j])
                hash_map[k] = hash_map.get(k, 0) + 1
            
            ans = max(ans, max(hash_map.values()) + 1)
        return ans
    

print(Solution().maxPoints([[1,1],[2,2],[3,3]]))