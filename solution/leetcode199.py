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
        ans = []
        while queue:

            for i in range(len(queue)):
                node = queue.pop(0)
                if i == len(queue) - 1:
                    ans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        return ans