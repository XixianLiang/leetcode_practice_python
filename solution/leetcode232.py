from collections import deque


class MyQueue:

    def __init__(self):
        self._push = deque()
        self._pop = deque()

    def _switch(self):
        if not self._push and not self._pop:
            return
        if not self._push:
            while self._pop:
                self._push.append(self._pop.pop())
        if not self._pop:
            while self._push:
                self._pop.append(self._push.pop())

    def push(self, x: int) -> None:
        if not self._pop:
            self._switch()
        self._push.append(x)

    def pop(self) -> int:
        if self._push:
            self._switch()
        return self._pop.pop()

    def peek(self) -> int:
        if self._push:
            self._switch()
        if self._pop:
            return self._pop[-1]

    def empty(self) -> bool:
        return not any([self._push, self._pop])


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
param_4 = obj.empty()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_5 = obj.pop()
pass