class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [[]]
        queue: List[TreeNode] = list()
        cached_queue: List[TreeNode] = list()
        queue.append(root)
        ans = []

        while queue or cached_queue:
            temp = []
            while queue:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    cached_queue.append(node.left)
                if node.right:
                    cached_queue.append(node.right)
            queue.extend(cached_queue)
            cached_queue = []
            ans.append(temp)

        return ans
