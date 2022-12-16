# Depth-First Search Using a LIFO Queue.
# The depth-first traversal follows a path from the source node by 
# plunging into the graph as deeply as possible before backtrackinG
# to the last edge crossing and trying another branch.

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

import networkx as nx
from graphmain3 import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")