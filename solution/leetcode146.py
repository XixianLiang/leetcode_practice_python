from typing import Dict


class BiNode:
    def __init__(self, 
                 key:int=None, 
                 val:int=None, 
                 prev: "BiNode"=None, 
                 next: "BiNode"=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    
    # def __str__(self):
    #     repr_str = []
    #     p = self.head.next
    #     while p.next is not None:
    #         repr_str.append(f" ({p.key}, {p.val}) ")
    #         p = p.next
    #     return "->".join(repr_str)
            
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hash: Dict[int, BiNode] = dict()
        self.head = BiNode()
        self.rear = BiNode(prev=self.head)
        self.head.next = self.rear       

    def get(self, key: int) -> int:
        if self._hash.get(key, None) is None:
            return -1
        target_node = self._hash[key]
        if target_node.prev is self.head:
            return target_node.val
        # 先删除这个节点
        temp = target_node.next
        target_node.next.prev = target_node.prev
        target_node.prev.next = temp
        # 再放到队头
        target_node.next = self.head.next
        target_node.prev = self.head
        self.head.next = target_node
        target_node.next.prev = target_node
        # print(self)
        return target_node.val

    def put(self, key: int, value: int) -> None:
        if self._hash.get(key, None) is not None:
            # 已有的时候放到队头
            self._hash[key].val = value
            target_node = self._hash[key]
            
            target_node.prev.next = target_node.next
            target_node.next.prev = target_node.prev
            target_node.next = self.head.next
            target_node.prev = self.head
        else:
            # 没有的时候添加节点
            if len(self._hash) == self._capacity:
                del_node = self.rear.prev
                self._hash.pop(del_node.key)
                # 删除队尾指针的前一个
                self.rear.prev = del_node.prev
                del_node.prev.next = self.rear
            # 放在队头
            target_node = BiNode(key, value, self.head, self.head.next)
            self._hash[key] = target_node   
        self.head.next = target_node
        target_node.next.prev = target_node
        # print(self)

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