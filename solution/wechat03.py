

from collections import deque


def find_largest(grid):
    h, w = len(grid), len(grid[0])
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    
    def visit(i, j, color):
        nonlocal visited
        ret = 1
        q = deque([(i, j)])
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            if x > 0 and not visited[x-1][y] and color == grid[x-1][y]:
                visited[x-1][y] = True
                ret += 1
                q.append((x-1, y))
            if y > 0 and not visited[x][y-1] and color == grid[x][y-1]:
                visited[x][y-1] = True
                ret += 1
                q.append((x, y-1))
            if x < h - 1 and not visited[x+1][y] and color == grid[x+1][y]:
                visited[x+1][y] = True
                ret += 1
                q.append((x+1, y))
            if y < w - 1 and not visited[x][y+1] and color == grid[x][y+1]:
                visited[x][y+1] = True
                ret += 1
                q.append((x, y+1))
        return ret
            
    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                ans = max(ans, visit(i, j, grid[i][j]))
    
    return ans



color = [
    [(1,1,1), (2,2,2), (1,1,1)],
    [(2,2,2), (2,2,2), (1,1,1)],
    [(1,1,1), (2,2,2), (1,1,1)]
]

print(find_largest(color))
