# Definition for a binary tree node.
from operator import ge
from platform import node
import re
from tkinter import NO
from turtle import right
from typing import Optional

import retry


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def rob(self, root: Optional[TreeNode]) -> int:
#         pick = dict()
#         not_pick = dict()
        
#         def dfs(root: Optional[TreeNode]):
#             if root is None:
#                 return
#             dfs(root.left)
#             dfs(root.right)
#             pick[root] = root.val + not_pick.get(root.left, 0) + not_pick.get(root.right, 0)
#             not_pick[root] = (max(pick.get(root.left, 0), not_pick.get(root.left, 0)) +
#                               max(pick.get(root.right, 0), not_pick.get(root.right, 0)))

#         dfs(root)
#         return max(pick.get(root, 0), not_pick.get(root, 0))


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0, 0
            pick_left, not_pick_left = dfs(root.left)
            pick_right, not_pick_right = dfs(root.right)
            pick = root.val + not_pick_left + not_pick_right
            not_pick = (max(pick_left, not_pick_left) +
                        max(pick_right, not_pick_right))
            return pick, not_pick

        return max(dfs(root))