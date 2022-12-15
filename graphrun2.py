# Object Reprepsentation of the Cities and Roads. 
# Graph for neighboring cities.



print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

from grapmain2 import City, load_graph

# This is for neighbor cities with no distance.
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print("\n\nNeighbors Cities: \n")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)


