
#queues.py

from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()
    
    def enqueue(self,element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
        