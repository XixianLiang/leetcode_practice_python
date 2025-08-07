class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
import heapq
heapq.nsmallest()
from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = dict()
        def clone(node):
            if self.visited.get(node.val, None) is not None:
                return self.visited[node.val]

            ret = Node(
                val=node.val
            )
            self.visited[node.val] = ret
            for n in node.neighbors:
                ret.neighbors.append(clone(n))
            return ret
        
        return clone(node)

a = Node(0)
b = Node(1)
c = Node(2)

a.neighbors = [b, c]
b.neighbors = [a, c]
c.neighbors = [a, b]

Solution().cloneGraph(
    a
)