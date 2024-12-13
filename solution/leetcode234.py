# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        seq = []
        while head:
            seq.append(head.val)
            head = head.next
        i = 0
        j = len(seq) - 1
        while i < j:
            if seq[i] != seq[j]:
                return False
            i += 1
            j -= 1
        return True