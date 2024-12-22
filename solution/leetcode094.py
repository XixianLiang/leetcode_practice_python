# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
