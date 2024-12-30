# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue:List[TreeNode] = list()
        queue.append(root)
        floor_vals = []
        while queue:
            temp_vals = list()
            for i in range(len(queue)):
                node = queue.pop(0)
                temp_vals.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            floor_vals.append(temp_vals)
        
        ans = [_[-1] for _ in floor_vals]
        return ans