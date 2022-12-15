# This program shows the Object Representation of the Cities and Roads.
# Using 3.9 Python Interpreter.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

# Networkx represents graph nodes using textual identifiers 
# that can optionally have an associated dictionary of attributes
import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print("\nHere is the map information: \n")
print(graph.nodes["london"])
