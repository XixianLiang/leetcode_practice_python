# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        inc = 0
        head = ListNode()
        p = head
        while l1 is not None or l2 is not None:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            p.next = ListNode((inc + a + b) % 10)
            inc = 1 if a + b + inc >= 10 else 0
            p = p.next
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        if inc:
            p.next = ListNode(1)
        return head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(Solution().addTwoNumbers(l1, l2))
