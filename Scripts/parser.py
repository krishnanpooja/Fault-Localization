'''
Returns Dynamic Metric for all projects except for MATH. Please use jdcallgrpah_parser.py script for the call graphs before using this code.Update the  '_stripped' to '_bold' to generate out and in degree of data dependency graph
'''
from pygraphviz import *
import pydot
import sys
import pyparsing
import json

path = sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Closure/stripped/1_stripped.dot"
#G=pg.AGraph("/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Lang/1.dot")
G=AGraph(path,directed=True)

#G=AGraph()
nbunch=G.nodes()
print nbunch
degree = G.degree(nbunch,True)
indegree = G.iterindegree(nbunch)
in_sum=0
out_sum=0
for n,d in indegree:
    #print(n,d)
    in_sum+=d
print(in_sum)
outdegree = G.iteroutdegree(nbunch)
for n,d in outdegree:
    #print(n,d)
    out_sum+=d
print(out_sum)
#print(degree)

'''
graph = pydot.graph_from_dot_file('/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Closure/1.dot')
#(node for node, out_degree in graph.out_degree_iter() if out_degree == 0)
print(graph)
edgeList = graph[0].get_edges() 
print(len(edgeList))
'''
'''
graph = pydot.graph_from_dot_file(path)
edgeList = graph.get_edge_list() 
for e in edgeList:
      tempAttr = json.dumps(e.get_attributes())
      edgeAttr = json.loads(tempAttr)
print(edgeAttr)

in_sum=0
out_sum=0
for n,d in indegree:
    #print(n,d)
    in_sum+=d
#print(in_sum)
outdegree = G.iteroutdegree(nbunch)
for n,d in outdegree:
    print(n,d)
    out_sum+=d
print(out_sum)
#print(degree)

print(G.styles['nodes'])
'''