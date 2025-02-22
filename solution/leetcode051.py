from typing import List
from copy import deepcopy

from tomlkit import key

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        def place(keyboard: List[List[bool]], x, y):
            n = len(keyboard)
            for i in range(n):
                for j in range(n):
                    if any([
                        x == i,
                        y == j,
                        abs(x - i) == abs(y - j)
                    ]):
                        keyboard[i][j] = False
                
        
        def traceback(keyboard: List[List[bool]], cur_queen: List[List[int]], n):
            if n == 0:
                ans.append(cur_queen[:])
                return
            i = len(keyboard) - n
            for j in range(len(keyboard)):
                if keyboard[i][j]:
                    next_keyboard = deepcopy(keyboard)
                    place(next_keyboard, i, j)
                    cur_queen.append([i, j])
                    traceback(next_keyboard, cur_queen, n-1)
                    cur_queen.pop()
                        
        keyboard = [[True for _ in range(n)] for _ in range(n)]
        traceback(keyboard, [], n)
        keyboard_template = ["." * n] * n
        n_queen = list()
        for a in ans:
            temp = deepcopy(keyboard_template)
            for x, y in a:
                temp[x] = "Q".join([temp[x][:y], temp[x][y+1:]])
            n_queen.append(temp)
        return n_queen
                

print(Solution().solveNQueens(4))