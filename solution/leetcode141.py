from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while True:
            slow = slow.next
            if slow is None:
                return False
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast is None:
                return False
            if fast is slow:
                return True
