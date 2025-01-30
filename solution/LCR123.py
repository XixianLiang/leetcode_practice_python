from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return head
        self.new_head = None
        def reverse_node(node:ListNode, prev:ListNode):
            if node.next is None:
                node.next = prev
                return node
            
            new_head = reverse_node(node.next, node)
            node.next = prev
            return new_head

        return reverse_node(head, None)


# 1 (-> 2 -> 3 -> 4)


def traverse(p: ListNode):
    while p:
        print(p.val, end=" ")
        p = p.next
    print()
    
l = ListNode(3, ListNode(6, ListNode(4, ListNode(1))))

traverse(l)
h = Solution().reverseBookList(l)
traverse(h)