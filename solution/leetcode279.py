from math import sqrt
from typing import List
from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [0]
        i = 1
        while i < n + 1:
            if sqrt(i) % 1 == 0:
                dp.append(1)
            else:
                dp.append(
                    min([dp[i - j ** 2] + 1 for j in range(1, int(sqrt(i)+1))])
                )
            i += 1
        
        return dp[-1]

# class Solution:
#     def numSquares(self, n: int) -> int:
#         if n <= 3:
#             return n
        
#         cur_ans = 0
#         ans = 10e6
#         def greedy_search(n):
#             nonlocal cur_ans
#             nonlocal ans
#             if n == 0:
#                 ans = min(cur_ans, ans)
#             for i in reversed(range(1, int(sqrt(n) + 1))):
#                 if cur_ans >= ans:
#                     break
#                 cur_ans += 1
#                 if n >= (factor := i ** 2):
#                     greedy_search(n - factor)
                
#                 cur_ans -= 1
                
        
#         greedy_search(n)
        
#         return ans

print(Solution().numSquares(6175))
print(Solution().numSquares(12))
print(Solution().numSquares(13))

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


