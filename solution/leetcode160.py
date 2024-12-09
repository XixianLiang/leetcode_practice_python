# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:

    def get_len(self, head:ListNode):
        count = 1
        while True:
            if head.next != None:
                count += 1
                head = head.next
            else:
                return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = self.get_len(headA)
        len_B = self.get_len(headB)
        delta = len_A - len_B
        pA = headA
        pB = headB
        if delta > 0:
            for i in range(delta):
                pA = pA.next
        else:
            for i in range(abs(delta)):
                pB = pB.next
        
        while True:
            if pA is pB:
                return pA
            if pA is None or pB is None:
                return None
            pA = pA.next
            pB = pB.next