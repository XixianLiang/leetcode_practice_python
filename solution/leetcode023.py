# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def mergeList(self, head1, head2):
        p = new_head = ListNode()
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        new_list = []
        for i in range((len(lists)) // 2):
            l = lists[2 * i]
            r = lists[2 * i + 1]
            new_list.append(self.mergeList(l, r))
        if len(lists) % 2 == 1:
            new_list.append(lists[-1])
        return self.mergeKLists(new_list)


a = ListNode(1, ListNode(4, ListNode(5)))

b = ListNode(1, ListNode(3, ListNode(4)))

c = ListNode(2, ListNode(6))

m = Solution().mergeKLists([a, b, c])

while m:
    print(m.val)
    m = m.next
