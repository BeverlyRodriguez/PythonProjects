# Object Reprepsentation of the Cities and Roads. 
# A graph comprising nodes and edges

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

from grapmain2 import City, load_graph


nodes, graph = load_graph("roadmap.dot", City.from_dict)

nodes["london"]
print("\nThese are the nodes and edges: \n")
print(graph)
