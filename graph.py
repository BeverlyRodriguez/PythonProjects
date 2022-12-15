# Object Reprepsentation of the Cities and Roads. 
# Reading sample DOT file using pygraphiz.
# Using 3.9 Python Interpreter

print("\n\t\t********PROGRAMMED BY:********")
print("\t\t***BEVERLY ANN L. RODRIGUEZ***\n")

import networkx as nx

#This is the printing statements.
print("RESULT: \n")
print(nx.nx_agraph.read_dot("roadmap.dot"))