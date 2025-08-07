import heapq
from typing import List

class ProjectManager:
    def __init__(self, profits, capital):
        self.n = len(profits)
        self.projects = list(zip(capital, profits))
        self.projects.sort()
        self._cur_i = 0
        self.heap = []

    
    def find_best_project(self, cur_capital):
        while self._cur_i < self.n:
            proj_capital, proj_profits = self.projects[self._cur_i]
            if proj_capital <= cur_capital:
                heapq.heappush(self.heap, (-proj_profits))
                self._cur_i += 1
            else:
                break
        if not self.heap:
            return -1
        return -heapq.heappop(self.heap)


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        p = ProjectManager(profits, capital)
        if w >= p.projects[-1][-1]:
            w += sum(_[1] for _ in heapq.nlargest(k, p.projects))
            return w

        for _ in range(k):
            gain = p.find_best_project(w)
            if gain < 0:
                break
            w += gain
        return w


Solution().findMaximizedCapital(
    k=1,
    w=10,
    profits=[1,2,3],
    capital=[0,0,0]
)