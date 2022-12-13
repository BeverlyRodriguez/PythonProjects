# This program shows Building a Priority Queue Data Type.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

from queues3 import PriorityQueue

# Priority levels: critical, important, and neutral.
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

#Message Deque with the lowest priority. 
print("\nThis is the lowest prioity:  \n")
print("\t", messages.dequeue())