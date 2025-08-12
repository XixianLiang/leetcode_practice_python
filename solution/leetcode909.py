from collections import deque
from typing import List


class Solution:
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        max_step = n * n
        mapping = dict()
        
        def cal_steps(i, j):
            nonlocal n
            rows_steps = (n - 1 - i) * n
            cols_steps = j + 1 if (n - 1 - i) % 2 == 0 else n - j
            return rows_steps + cols_steps
        
        for i in range(n):
            for j in range(n):
                mapping[cal_steps(i, j)] = (i, j)
                
        ans = float("inf")
        
        q = deque()
        q.append(1)
        visited = set()
        steps = 0

        while q:
            width = len(q)
            steps += 1
            for i in range(width):
                node_i = q.popleft()
                visited.add(node_i)
                for j in reversed(range(node_i + 1, min(node_i + 7, max_step + 1))):
                    x, y = mapping[j]
                    if board[x][y] != -1:
                        j = board[x][y]
                    if j == max_step:
                        ans = min(ans, steps)
                    if j not in visited:
                        q.append(j)

        return ans if ans != float("inf") else -1



# Solution().snakesAndLadders(
#     [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# )

Solution().snakesAndLadders(
    [
        [-1,-1,-1],
        [-1,9,8],
        [-1,8,9]
    ]
)