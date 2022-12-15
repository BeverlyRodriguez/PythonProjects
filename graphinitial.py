# This program shows the Object Representation of the Cities and Roads.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print("\nHere is the map information: \n")
print(graph.nodes["london"])
