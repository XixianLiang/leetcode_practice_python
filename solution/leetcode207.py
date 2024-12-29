from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 创建邻接表和入度数组
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # 填充邻接表和入度数组
        for target, requisite in prerequisites:
            graph[requisite].append(target)
            indegree[target] += 1
        
        # 使用队列来进行 BFS
        queue = list()
        
        # 将所有入度为 0 的节点加入队列
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            visit = queue.pop(0)
            for target in graph[visit]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    queue.append(target)
        
        return all([_ == 0 for _ in indegree])



print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))

[[0, 1],
 [1, 0]]