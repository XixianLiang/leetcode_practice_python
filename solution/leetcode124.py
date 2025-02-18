from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -10000
        
        def get_max_sum(root: TreeNode):
            if root is None:
                return 0
            s1 = get_max_sum(root.left)
            s2 = get_max_sum(root.right)
            self.ans = max(self.ans, s1 + s2 + root.val)
            return max(0, root.val + s1, root.val + s2)
        
        get_max_sum(root)
        
        return self.ans


t = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().maxPathSum(t))