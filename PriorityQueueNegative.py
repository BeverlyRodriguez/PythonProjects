# This code shows Building a Priority Queque Data Type.
# This code is for dequeue.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

from queues4 import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

#These are the printing statements for dequeue.
print("\nThese are the results: \n")
print("\t", messages.dequeue())
print("\t", messages.dequeue())
print("\t", messages.dequeue())
print("\t", messages.dequeue())