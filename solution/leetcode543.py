# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.traverse(root)
        return self.max_d

    def traverse(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.traverse(root.left)
        right_depth = self.traverse(root.right)

        self.max_d = max(self.max_d, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
