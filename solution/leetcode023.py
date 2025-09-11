# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        
        new_head = h = ListNode(0)
        while heap:
            _, i = heapq.heappop(heap)
            h.next = lists[i]
            lists[i] = lists[i].next
            h = h.next
            h.next = None
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return new_head.next