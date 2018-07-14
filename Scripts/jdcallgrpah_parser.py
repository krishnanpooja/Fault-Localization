'''
Splits the callgraph files into bold and stripped to represent the call dependency and data dependency graphs respectively
Pass filename as argument. 
'''
import os
import re
import sys

faultyMethod=""
p = re.compile(r'[a-z]+.+#')

filepath=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Lang/"
path, dirs, files = next(os.walk(filepath))
file_count = len(files)
print file_count
"""
faultyMethod=""
faulty=[]
for i in range(1,file_count):
    path="/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Lang/"+str(i)+".dot"
    with open(path) as f:
        for line in f:
            if "fillcolor=\"red\"" in line:
                if p.search(line):
                    faultyMethod=line.replace("[style=striped shape=box fillcolor=\"red\"];","")
                    faulty.append((i,faultyMethod))
print((faulty))
"""
#Snippet to split the jdcallgraphs into stripped and bold graphs
for i in range(1,file_count+1):
    print i
    if not i is 4: # add file you dont have call graphs for over here.
         f_bold = open('/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/bold/'+str(i)+'_bold.dot', 'a')
         f_stripped = open('/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/stripped/'+str(i)+'_stripped.dot', 'a')
         with open(filepath+str(i)+'.dot') as f:
             for line in f:
                 if "->" in line:
                     if "[style=bold];" in line:
                         f_bold.write(line)
                     else:
                         f_stripped.write(line)
                 else:
                     f_stripped.write(line)
                     f_bold.write(line)
         f_stripped.close()
         f_bold.close()
