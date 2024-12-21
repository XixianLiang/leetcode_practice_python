# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.p_lt = [_ for _ in lists]
        self.cache_val = [p.val if p is not None else 10e5 for p in self.p_lt]

        head = p = ListNode()

        while any([_ != 10e5 for _ in self.cache_val]):
            val = min(self.cache_val)
            i = self.cache_val.index(val)

            p.next = self.p_lt[i]

            self.p_lt[i] = self.p_lt[i].next

            p = p.next

            self.cache_val[i] = self.p_lt[i].val if self.p_lt[i] else 10e5

        return head.next


a = ListNode(2, ListNode(3))

b = ListNode(1, ListNode(5))

m = Solution().mergeKLists([a, b])

while m:
    print(m.val)
    m = m.next
