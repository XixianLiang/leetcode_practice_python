from typing import List


def _cal_distance(cor1, cor2):
    x1, y1 = cor1
    x2, y2 = cor2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_graph(points: List[int]):
    n = len(points)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph[i][j] = _cal_distance(points[i], points[j])
    return graph

class Solution:
    def get_ans(self, points:List[int], weak_pill:int, strong_pill:int, r1:int, r2:int):
        self.points = points
        self.weak_pill = weak_pill
        self.strong_pill = strong_pill
        self.r1 = r1
        self.r2 = r2
        self.graph = get_graph(points)
        self.used = False
        visited = [False for _ in range(len(points))]
        visited[0] = True
        a = self.bfs(0, visited, 0)
        if a <= weak_pill:
            print(f"0 {a}") 
        
    def bfs(self, i, visited, depth):
        depth += 1
        candidates = []
        for j in range(len(self.points)):
            if not visited[j]:
                if self.graph[i][j] <= self.r1:
                    if j == len(visited) - 1:
                        return depth
                    candidates.append((self.graph[i][j], j))
        candidates.sort()
        ans = float("inf")
        for candidate in candidates:
            visited[candidate[1]] = True
            d = self.bfs(candidate[1], visited, depth)
            visited[candidate[1]] = False
            if d:
                ans = min(ans, d)
        return ans
        


# tests_count = int(input().strip())

s = Solution()

Solution().get_ans(
    [[0,0],[3,4],[6,0],[9,4],[12,0]],
    10,
    3,
    5, 15
)

# for t in range(tests_count):
#     n, weak_pill, strong_pill, r1, r2 = [int(_) for _ in input().split()]
#     points = []
#     for j in range(n):
#         points.append([int(_) for _ in input().split()])
#     s.get_ans(points, weak_pill, strong_pill, r1, r2)