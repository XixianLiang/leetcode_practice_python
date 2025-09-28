from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        to_visit = deque(rooms[0])
        while to_visit:
            next_visit = to_visit.popleft()
            if not visited[next_visit]:
                visited[next_visit] = True
                for n in rooms[next_visit]:
                    if not visited[n]:
                        to_visit.append(n)
        return all(visited)

print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))