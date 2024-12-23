# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        self.traverse(root1, root2)
        return root1

    def traverse(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return

        if not root1:
            root1 = root2

        root1.val = root1.val + root2.val if root2 else root1.val

        if not root1.left:
            if root2 and root2.left:
                root1.left = TreeNode(0)
        if not root1.right:
            if root2 and root2.right:
                root1.right = TreeNode(0)

        self.traverse(root1.left, root2.left if root2 else None)
        self.traverse(root1.right, root2.right if root2 else None)
