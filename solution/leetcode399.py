from traitlets import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        cnt = 0
        mapping = dict()
        for equation in equations:
            for var in equation:
                if mapping.get(var, None) is None:
                    mapping[var] = cnt
                    cnt += 1

        graph = [[0 for _ in range(cnt)] for _ in range(cnt)]
        
        for i, equation in enumerate(equations):
            a, b = equation
            src = mapping[a]
            target = mapping[b]
            graph[src][target] = values[i]
            graph[target][src] = 1.0 / values[i]
        
        def bfs(query):
            src, target = query
            if src not in mapping or target not in mapping:
                return -1.0
            if src == target:
                return 1.0
            nonlocal cnt
            src = mapping[src]
            target = mapping[target]
            visited = [False for _ in range(cnt)]
            queue = [(src, 1.0)]
            visited[src] = True
            while queue:
                level = len(queue)
                for i in range(level):
                    src, cur = queue[i]
                    for j in range(cnt):
                        if not visited[j] and graph[src][j] != 0:
                            visited[j] = True
                            if j == target:
                                return cur * graph[src][j]
                            queue.append((j, cur * graph[src][j]))
                queue = queue[level:]
            return -1.0
        
        ans = []
        for query in queries:
            ans.append(bfs(query))
        return ans
    
Solution().calcEquation(
    equations=[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
    values=[3.0,4.0,5.0,6.0],
    queries=[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
)