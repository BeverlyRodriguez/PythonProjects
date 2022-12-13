# This program is for Representing Priority Queues with a Heap (heappop).

from heapq import heappush
from heapq import heappop

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

# The first element on a heap always has the smallest (min-heap) or the highest (max-heap) 
# value, depending on how you define the condition for the mentioned relationship. 
vegetables = []
heappush(vegetables, "Squash")
heappush(vegetables, "Letuce")
heappush(vegetables, "Eggplant")
heappush(vegetables, "Cucumber")
heappush(vegetables, "Celery")


# When you pop an element from a heap, you’ll always get the first one, 
# while the remaining elements might shuffle a little bit
print(heappop(vegetables))
print("These are the remaining elements: \n\t",vegetables)


