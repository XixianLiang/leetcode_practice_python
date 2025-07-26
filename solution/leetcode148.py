# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:

    def mergeList(self, head1:Optional[ListNode], head2:Optional[ListNode]):

        
        p = new_head = ListNode(val=0)
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        
        return new_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        fast = slow = head
        fast = fast.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(temp)
        return self.mergeList(l, r)
    
h = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
def print_list(head: ListNode):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return res

print(print_list(Solution().sortList(h)))