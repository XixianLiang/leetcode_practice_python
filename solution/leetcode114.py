# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        def flat(root: TreeNode):

            if root.left:
                front_l, rear_l = flat(root.left)
                root.left = None
            else:
                front_l, rear_l = None, None
                
            if root.right:
                front_r, rear_r = flat(root.right)
            else:
                root.right = front_l
                if root.right is None:
                    return root, root
                else:
                    return root, rear_l

            if front_l:
                root.right = front_l
                rear_l.right = front_r
                return root, rear_r
            return root, rear_r
        
        new_root, _ = flat(root)
        return new_root

t = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
Solution().flatten(t)