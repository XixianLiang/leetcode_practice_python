from collections import deque
from typing import List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [set() for _ in range(numCourses)]
        
        for target, pre in prerequisites:
            graph[target].add(pre)
        
        to_visit = {_ for _ in range(numCourses)}
        
        def traceback(cur:List[int], to_visit: Set[int]):
            if not to_visit:
                return cur
            candidates = []
            for i in to_visit:
                if not graph[i]:
                    candidates.append(i)
            
            if not candidates:
                return []

            for c in candidates:
                to_visit.discard(c)
                for links in graph:
                    links.discard(c)
                cur.append(c)
            return traceback(cur, to_visit)
        
        return traceback([], to_visit)


print(Solution().findOrder(
    4, [[1,0],[2,0],[3,1],[3,2]]
))