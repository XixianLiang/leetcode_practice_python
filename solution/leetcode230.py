# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.cur_k = 1
        return self.traverse(root)
    
    def traverse(self, root:Optional[TreeNode]):
        if root is None:
            return None
        a = self.traverse(root.left)
        b = None
        if self.cur_k == self.k:
            b = root.val
        self.cur_k += 1
        c = self.traverse(root.right)
        
        if a is not None:
            return a
        if b is not None:
            return b
        if c is not None:
            return c