# This program is for Representing Priority Queues with a Heap (heappush).

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

# The point of a heap isn’t so much about sorting elements but rather keeping them in a
# certain relationship to allow for quick lookup.

from heapq import heappush

fruits = []
heappush(fruits, "Orange")
heappush(fruits, "Apple")
heappush(fruits, "Banana")
heappush(fruits, "Mango")
heappush(fruits, "Grapes")


# Fruit names in the resulting heap don’t follow alphabetical order.
print("\nThese are the elements being sorted:\n\n\t", fruits)