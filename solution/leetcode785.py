from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_A = set([0])
        set_B = set()
        process = deque([0])
        next_set, cur_set = set_B, set_A
        while process:
            for _ in range(len(process)):
                n = process.popleft()
                for next_node in graph[n]:
                    if next_node in cur_set:
                        return False
                    if next_node not in next_set:
                        process.append(next_node)
                        next_set.add(next_node)
            cur_set, next_set = next_set, cur_set
        return True
                
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))