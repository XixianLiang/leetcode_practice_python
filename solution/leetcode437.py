from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.targetSum = targetSum
        self.pre_stack = []
        self.target_map = dict()
        self.ans = 0
        self.target_map[targetSum] = 1
        self.dfs(root)
        return self.ans
    
    def dfs(self, root: TreeNode):
        if root is None:
            return
        
        cur_val = root.val
        cur_prefix = cur_val + (self.pre_stack[-1] if self.pre_stack else 0)
        self.pre_stack.append(cur_prefix)
        if self.target_map.get(cur_prefix, 0):
            self.ans += self.target_map[cur_prefix]
        
        self.target_map[cur_prefix + self.targetSum] = (
            self.target_map.get(cur_prefix + self.targetSum, 0) + 1
        )
        self.dfs(root.left)
        self.dfs(root.right)
        self.pre_stack.pop()
        self.target_map[cur_prefix + self.targetSum] -= 1

t = TreeNode(0, left=TreeNode(1), right=TreeNode(1))
print(Solution().pathSum(t, 1))