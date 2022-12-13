#This program is for Building a Queue Data Type.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")


from queues import Queue


#This section is the initial FIFO.
#fifo = Queue()
#fifo.enqueue("1st")
#fifo.enqueue("2nd")
#fifo.enqueue("3rd")

#fifo.dequeue()
#fifo.dequeue()
#fifo.dequeue()


fifo = Queue("1st", "2nd", "3rd", "4th", "5th")
print("\nQueues: ", len(fifo))

for element in fifo:
    print("\n\tThis is the", element, "element.")

len(fifo)
