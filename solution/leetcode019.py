# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = head
        post = head

        for _ in range(n):
            post = post.next

        if post is None:
            prev.next = prev.next.next
            return head

        if head.next is None and n == 1:
            return None

        while post.next is not None:
            prev = prev.next
            post = post.next

        prev.next = prev.next.next

        self.traverse(head)

        return head

    def traverse(self, head):
        while head is not None:
            print(head.val)
            head = head.next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a = ListNode(1, ListNode(2))
print(Solution().removeNthFromEnd(a, 2))
