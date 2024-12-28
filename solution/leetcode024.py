# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


from typing import Optional


# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head

#         _head = ListNode()
#         _head.next = head

#         prev = head
#         post = head.next
#         temp = _head

#         while post is not None:
#             prev.next = post.next
#             temp.next = post
#             post.next = prev

#             prev, post = post, prev

#             for i in range(2):
#                 if post is None:
#                     break
#                 post = post.next
#                 prev = prev.next
#                 temp = temp.next

#         return _head.next

#     def traverse(self, head: ListNode):
#         while head is not None:
#             print(head.val)
#             head = head.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head

    def traverse(self, head: ListNode):
        while head is not None:
            print(head.val)
            head = head.next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

Solution().traverse(Solution().swapPairs(a))
