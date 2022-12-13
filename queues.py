
#queues.py

from collections import deque

class Queue:
    def __init__(self, *elements):
        self.elements = deque(elements)

    def __len__(self):
        return len(self._elements)
    
    def enqueue(self,element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
        