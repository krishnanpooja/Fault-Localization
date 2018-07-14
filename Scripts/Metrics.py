'''
Computes in-degree and out degree. Filepath needs to be passed as parameter.
Replace the '_bold' to with '_stripped' for data dependency degree centrality.
Please run jdcallgrpah_parser.py to seperate the call graphs before using this file.
'''
from pygraphviz import *
import os
import sys
import pydot
import pyparsing
import json
import re
import networkx as nx
from networkx.drawing.nx_agraph import read_dot
from networkx.algorithms.cluster import clustering
from networkx.algorithms.components.strongly_connected import strongly_connected_components
from networkx.algorithms.components.weakly_connected import weakly_connected_components

def get_strongly_cc(G, node):
    """ get storngly connected component of node""" 
    for cc in nx.strongly_connected_components(G):
        if node in cc:
            return cc
    else:
        return set()

def get_weakly_cc(G, node):
    """ get weakly connected component of node""" 
    for cc in nx.weakly_connected_components(G):
        if node in cc:
            return cc
    else:
        return set()


faultyMethod=""
p = re.compile(r'[a-z]+.+#')
filepath=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Chart/"
path, dirs, files = next(os.walk(filepath))
file_count = len(files)
print 'Number of files found:',file_count
#print file_count
in_list=[]
out_list=[]
parent=[]
for i in range(1,file_count+2):
    ##print i
    if i is 4:
      continue
    path = filepath+'bold/'+str(i)+'_bold.dot'
    with open(path) as f:
        for line in f:
            if (("fillcolor=\"red\"") or  ("fillcolor=\"red:")) in line:
                if p.search(line):
                    faultyMethod=line
    node=[]
    print i,faultyMethod
    G=AGraph(path,directed=True)
    nbunch=G.nodes()
    for n in nbunch:
        if n in faultyMethod:
            node.append(n)
    degree = G.degree(nbunch,True)
    indegree = G.iterindegree(node)
    in_sum=0
    out_sum=0
    for n,d in indegree:
        ##print(n,d)
        in_sum+=d
    in_list.append(in_sum)
    outdegree = G.iteroutdegree(node)
    for n,d in outdegree:
        ##print(n,d)
        out_sum+=d
    out_list.append(out_sum)
    """
    if len(node)>0:
        subgraph_parent=G.subgraph_parent(node[0])
        if subgraph_parent:
            parent.append(len(subgraph_parent))
        else:
            parent.append(0)
    else:
        parent.append(0)
    noden=[]
    g = nx.DiGraph(read_dot(path))
    nnetwork=g.nodes()
    for n in nnetwork:
        if n in faultyMethod:
            noden.append(n)
    print(clustering(g))
    weak_component = get_weakly_cc(g, nnetwork)  # Weakly connected component of node in G
    strong_component = get_strongly_cc(g, nnetwork)
    print(clustering(g,weak_component))
    """
for val in in_list:
    print(val)
print('!!!!!!!!!!out_degree!!!!!!!!!!!!!!')
for val in out_list:
    print(val)
print(parent)
