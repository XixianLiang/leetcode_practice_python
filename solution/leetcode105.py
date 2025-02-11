from tkinter import NO
from turtle import right
from typing import List, Optional

from sympy import Li


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def divide(preorder: List[int], inorder: List[int]):
            if not preorder:
                return None, [], [], [], []
            root = preorder[0]
            left_inorder = inorder[: inorder.index(root)]
            right_inorder = inorder[inorder.index(root) + 1 :]
            left_preorder = preorder[1 : 1 + len(left_inorder)]
            right_preorder = preorder[len(preorder) - len(right_inorder):len(preorder)]
            return root, left_inorder, right_inorder, left_preorder, right_preorder

        (root, left_inorder, right_inorder, left_preorder, right_preorder) = divide(
            preorder, inorder
        )
        if root is not None:
            r = TreeNode(
                val=root,
                left=self.buildTree(left_preorder, left_inorder),
                right=self.buildTree(right_preorder, right_inorder),
            )
            return r
        return None


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
Solution().buildTree(preorder, inorder)
