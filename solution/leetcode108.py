# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.generate_node(0, len(nums) - 1)

    def generate_node(self, i, j):
        if i > j:
            return None
        m = (i + j) // 2
        head = TreeNode(self.nums[m])
        head.left = self.generate_node(i, m - 1)
        head.right = self.generate_node(m + 1, j)
        return head


a = Solution().sortedArrayToBST([1, 2, 3])
a
