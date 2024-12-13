# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, ans = self.dfs(root, p, q)
        return ans

    def dfs(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> List[bool]:
        if node is None:
            return [False, False], None
        p_exist = q_exist = False
        ans_node = None
        res1, ans_node1 = self.dfs(node.left, p, q)
        if node is p:
            p_exist = True
        if node is q:
            q_exist = True
        res2, ans_node2 = self.dfs(node.right, p, q)

        p_exist = p_exist | res1[0] | res2[0]
        q_exist = q_exist | res1[1] | res2[1]

        if p_exist and q_exist:
            if ans_node1 is not None:
                ans_node = ans_node1
                return [True, True], ans_node
            if ans_node2 is not None:
                ans_node = ans_node2
                return [True, True], ans_node
            ans_node = node
        
        return [p_exist, q_exist], ans_node