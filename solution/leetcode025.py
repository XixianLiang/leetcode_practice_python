# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next

from typing import Optional, List


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        h = ListNode(val=0, next=head)
        self.reverseK(h, k)
        self.traverse(h.next)

    def traverse(self, head:ListNode):
        while head:
            print(head.val, end=", ")
            head = head.next
        

    def reverseK(self, head:ListNode, k):
        lt:List[ListNode] = []
        p = head.next
        for i in range(k):
            if p is not None:
                lt.append(p)
                p = p.next
            else:
                return 
        
        next_p = lt[-1].next
        for i in reversed(range(1, k)):
            lt[i].next = lt[i - 1]
        
        lt[0].next = next_p
        head.next = lt[k - 1]
        return self.reverseK(lt[0], k)

h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

Solution().reverseKGroup(h, 3) 