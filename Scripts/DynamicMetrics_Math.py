'''
Returns Dynamic Metric for MATH project. Update the filepath for MATH call graphs. Please use jdcallgrpah_parser.py script 
for the call graphs before using this code.
If CallGraphs for certain buggy versions are not available then please add the buggy version number in the 'if' clause below.
'''
from pygraphviz import *
import os
import pydot
import pyparsing
import json
import re
import networkx as nx
from networkx.drawing.nx_agraph import read_dot
from networkx.algorithms.cluster import clustering
from networkx.algorithms.components.strongly_connected import strongly_connected_components
from networkx.algorithms.components.weakly_connected import weakly_connected_components
from os import listdir
from os.path import isfile, join

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

path, dirs, files = next(os.walk("/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Math_onlyFailingTests/Math_onlyFailingTests/"))
file_count = len(files)
print file_count
in_list=[]
out_list=[]
parent=[]
for i in range(1,107):
    ##Call Graphs not available for these versions
    if i in (3,4,6,15,16,18,19,20,59,63,79):
      continue
    path = '/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Math_onlyFailingTests/Math_onlyFailingTests/'+str(i)+'/ddg/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print onlyfiles
    in_sum=0
    out_sum=0
    node=[]
    for f in range(len(onlyfiles)):
        mypath=path+onlyfiles[f]
        print('mypath:',mypath)
        if os.stat(mypath).st_size is 0:
           continue
        G=AGraph(mypath,directed=True)
        nbunch=G.nodes()
        for n in nbunch:
            if n in onlyfiles[f].replace('.dot',''):
               node.append(n)
        degree = G.degree(nbunch,True)
        indegree = G.iterindegree(node)
        for n,d in indegree:
        ##print(n,d)
            in_sum+=d
        in_list.append(in_sum)
        outdegree = G.iteroutdegree(node)
        for n,d in outdegree:
            ##print(n,d)
            out_sum+=d
        out_list.append(out_sum)
for val in in_list:
    print(val)
print('!!!!!!!!!!out_degree!!!!!!!!!!!!!!')
for val in out_list:
    print(val)
#print(parent)
