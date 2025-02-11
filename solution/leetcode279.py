from typing import List
from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        pass

# class Solution:
#     def numSquares(self, n: int) -> int:
#         if n <= 3:
#             return n
#         squares = []
#         for i in range(n // 2, 0, -1):
#             temp = i ** 2
#             if temp == n:
#                 return 1
#             elif temp < n:
#                 squares.append(i ** 2)

#         self.ans = n
        
#         @cache
#         def traceback(target, k):
#             for square in squares:
#                 if square == target: 
#                     self.ans = min(k + 1, self.ans)
#                 if square < target:
#                     traceback(target - square, k + 1)
        
#         traceback(n, 0)
#         return self.ans


print(Solution().numSquares(340))
