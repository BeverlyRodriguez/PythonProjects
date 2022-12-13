# This program is for Representing Priority Queues with a Heap (heappush).

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

# The point of a heap isn’t so much about sorting elements but rather keeping them in a
# certain relationship to allow for quick lookup.

from heapq import heappush

vegetables = []
heappush(vegetables, "Squash")
heappush(vegetables, "Letuce")
heappush(vegetables, "Eggplant")
heappush(vegetables, "Cucumber")
heappush(vegetables, "Celery")


# Vegatables names in the resulting heap don’t follow alphabetical order.
print("\nThese are the elements being sorted:\n\n\t", vegetables)