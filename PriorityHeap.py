# This program is for Representing Priority Queues with a Heap.


# The point of a heap isn’t so much about sorting elements but rather keeping them in a
# certain relationship to allow for quick lookup.

from heapq import heappush

fruits = []
heappush(fruits, "Orange")
heappush(fruits, "Apple")
heappush(fruits, "Banana")
heappush(fruits, "Mango")
heappush(fruits, "Grapes")


# Fruit names in the resulting heap in the example don’t follow alphabetical order.
print("These are the elements being sorted:\n", fruits)