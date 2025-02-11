
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional, Dict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p_new = copy_head = Node(0)
        node_map: Dict[Node:"old", Node:"new"] = dict()
        p_old = head
        while p_old:
            p_new.next = Node(p_old.val)
            node_map[p_old] = p_new.next

            p_old = p_old.next
            p_new = p_new.next
        
        # set the random pointer
        p_new = copy_head.next
        p_old = head
        while p_old:
            if p_old.random is not None:
                p_new.random = node_map[p_old.random]
            p_old = p_old.next
            p_new = p_new.next
        return copy_head.next