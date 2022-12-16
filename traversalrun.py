# Shortest Path Using Breadth-First Traversal.
# Using networkx to reveal all the shortest paths between two cities.
# Traversing the graph using the breadth-first approach will produce a path guaranteed to have the fewest nodes. 
# There are two such shortest paths between Aberdeen and Perth when you disregard the road distances. 

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

import networkx as nx
from graphmain3 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))
