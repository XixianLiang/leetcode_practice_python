# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
from typing import Optional, List
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     prev = None  # 初始化前一个节点为 None
    #     current = head  # 当前节点从头节点开始
        
    #     while current:
    #         next_node = current.next  # 保存当前节点的下一个节点
    #         current.next = prev  # 反转当前节点的指针
    #         prev = current  # 移动 prev 到当前节点
    #         current = next_node  # 移动到下一个节点
        
    #     return prev  # prev 现在是新的头节点
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
