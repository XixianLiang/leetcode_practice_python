# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last_val = -float("inf")
        return self.traverse(root)

    def traverse(self, root: TreeNode):
        if root is None:
            return True
        bool_a = self.traverse(root.left)
        bool_c = self.last_val < root.val
        bool_b = self.traverse(root.right)
        self.last_val = root.val
        return bool_a and bool_b and bool_c


# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         _, _, ans = self.traverse(root)
#         return ans

#     def traverse(self, root: Optional[TreeNode]):
#         if root is None:
#             return -float("inf"), float("inf"), True

#         left_min, left_max, left_bool = self.traverse(root.left)
#         right_min, right_max, right_bool = self.traverse(root.right)

#         if right_min == root.val or left_max == root.val:
#             return 0, 0, False

#         if left_min == -float("inf"):
#             left_min = left_max = root.val
#         if right_min == -float("inf"):
#             right_min = right_max = root.val

#         if right_min < root.val or left_max > root.val:
#             return 0, 0, False
#         else:
#             return left_min, right_max, left_bool and right_bool
