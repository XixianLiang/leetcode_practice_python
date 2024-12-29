# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left:TreeNode = left
        self.right:TreeNode = right
from typing import List, Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flattened_lt:List[TreeNode] = []
        self.traverse(root)
        for i, node in enumerate(self.flattened_lt):
            node.left = None
            if i < len(self.flattened_lt) - 1:
                node.right = self.flattened_lt[i + 1]
            else:
                node.right = None
        
    
    def traverse(self, root:TreeNode):
        if root is None:
            return
        self.flattened_lt.append(root)
        self.traverse(root.left)
        self.traverse(root.right)