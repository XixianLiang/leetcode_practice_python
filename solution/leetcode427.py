from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def merge_leafs(self, node: Node):
        values = [node.topLeft.val, node.topRight.val, node.bottomLeft.val, node.bottomRight.val]
        isLeaves = [node.topLeft.isLeaf, node.topRight.isLeaf, node.bottomLeft.isLeaf, node.bottomRight.isLeaf]
        if all(isLeaves):
            if all(_ == 0 for _ in values) or all(_ for _ in values):
                return Node(isLeaf=True, val=values[0], topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        return node

    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) > 2:
            m = len(grid) // 2
            topLeft = [grid[i][:m] for i in range(m)] 
            topRight = [grid[i][m:] for i in range(m)] 
            bottomLeft = [grid[i+m][:m] for i in range(m)]
            bottomRight = [grid[i+m][m:] for i in range(m)]
            return self.merge_leafs(Node(
                val = 0,
                isLeaf=False,
                topLeft=self.construct(topLeft),
                topRight=self.construct(topRight),
                bottomLeft=self.construct(bottomLeft),
                bottomRight=self.construct(bottomRight)
            ))

        node = Node(
            val=1,
            isLeaf=False,
            topLeft=Node(val=grid[0][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
            topRight=Node(val=grid[0][1], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
            bottomLeft=Node(val=grid[1][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
            bottomRight=Node(val=grid[1][1], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        )
        return self.merge_leafs(node)
        
                
Solution().construct([[0,0],[0,0]])
tree = Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
tree