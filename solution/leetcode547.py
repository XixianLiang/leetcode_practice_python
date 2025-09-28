from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = [False for _ in range(n)]
        
        def visit(i):
            nonlocal visited
            visited[i] = True
            for j in range(n):
                if not visited[j] and isConnected[i][j]:
                    visit(j)
        
        cnt = 0
        for i in range(n):
            if not visited[i]:
                cnt += 1
                visit(i)
        
        return cnt
