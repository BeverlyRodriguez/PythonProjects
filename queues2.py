#This queues is for Building Stack Data Type

from collections import deque

class Queue:
    def init(self, *elements):
        self._elements = deque(elements)

    def len(self):
        return len(self._elements)

    def iter(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()