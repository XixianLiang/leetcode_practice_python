from typing import Dict

class BiNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):

        self.front = BiNode()
        self.rear = BiNode(prev = self.front)
        self.front.next = self.rear
        self.hash_map = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.hash_map.get(key, None) is None:
            return -1
        node = self.hash_map[key]
        if self.front.next == node:
            return node.val
        
        prev_node = node.prev
        node.prev.next = node.next
        node.next.prev = prev_node

        node.next = self.front.next
        node.prev = self.front
        self.front.next.prev = node
        self.front.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.hash_map.get(key, None):
            self.hash_map[key].val = value
            if self.front.next == self.hash_map[key]:
                return
            node = self.hash_map[key]
            prev_node = node.prev
            node.prev.next = node.next
            node.next.prev = prev_node

            node.prev = self.front
            node.next = self.front.next
            self.front.next = node
            node.next.prev = self.front
            return
        if len(self.hash_map) == self.capacity:
            rm_node = self.rear.prev
            self.hash_map.pop(rm_node.key)
            self.rear.prev = rm_node.prev
            rm_node.prev.next = self.rear
            del rm_node

        node = BiNode(key=key, val=value, prev=self.front, next=self.front.next)
        self.front.next = node
        node.next.prev = node
        self.hash_map[key] = node

["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

obj = LRUCache(2)
obj.get(2)
obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
obj.get(1)
obj.get(2)