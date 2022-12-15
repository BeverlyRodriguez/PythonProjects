# The immediate neighbors of a given city.
# Object Reprepsentation of the Cities and Roads. 


print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")


from grapmain2 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)
print("These are the neighbors of the LONDON: \n")
for neighbor, weights in graph[nodes["london"]].items():

    print(weights["distance"], neighbor.name)