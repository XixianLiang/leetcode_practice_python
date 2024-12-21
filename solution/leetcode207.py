from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        graph = [[0] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a][b] = 1
        return self.bfs(numCourses, graph)

    def bfs(self, nodes_num: int, graph):
        not_visited_nodes = set(node for node in range(nodes_num))
        next_node = []
        while not_visited_nodes or next_node:
            if next_node:
                visit = next_node.pop()
                if visit not in not_visited_nodes:
                    return False
                not_visited_nodes.remove(visit)
            else:
                visit = not_visited_nodes.pop()
            for j in range(nodes_num):
                if graph[visit][j]:
                    next_node.append(j)

        return True


print(Solution().canFinish(2, [[1, 0]]))
