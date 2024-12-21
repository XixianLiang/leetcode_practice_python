from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                # size = self.getRingSize(fast)
                # return self.getFistNode(head, size)
                return self.getFistNode2(head, slow)

        return None

    def getFistNode2(self, head: ListNode, meet: ListNode):
        while head is not meet:
            head = head.next
            meet = meet.next
        return head

    def getFistNode(self, head: ListNode, ring_size):
        index = 0
        while True:
            temp = head
            for _ in range(ring_size):
                temp = temp.next
            if temp is head:
                return index
            head = head.next
            index += 1

    def getRingSize(self, meet: ListNode) -> int:
        size = 0
        slow = meet
        fast = meet
        while True:
            slow = slow.next
            fast = fast.next.next
            size += 1
            if slow is fast:
                return size


a3 = ListNode(3)
a2 = ListNode(2)
a0 = ListNode(0)
a4 = ListNode(4)

a3.next = a2
a2.next = a0
a0.next = a4
a4.next = a2

print(Solution().detectCycle(a3))
