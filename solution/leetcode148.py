# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        lt: List[ListNode] = []
        while head is not None:
            lt.append(head)
            head = head.next

        lt.sort(key=lambda x: x.val)

        head = ListNode()
        for node in lt:
            node.next = None
            head.next = node
            head = head.next

        return head.next
