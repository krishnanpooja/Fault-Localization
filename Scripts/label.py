'''
The file computes Labels for all projects except for MATH. 
Pass two arguments: argument 1 - path of the graph file for the projects
                    argument 2 - path of the matrix and spectra file.
'''
from __future__ import division
import os
import re
import sys
import numpy as np

filepath_gzoltar=sys.argv[2]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Lang/lang/"
def Spectra(file,faultM):
   faultM=faultM.replace('\"','')
   faultM=faultM.replace('\n','')
   faultM=faultM.replace('\t','')
   faultM=faultM.replace(' ','')
   line_no=0
   path=filepath_gzoltar+str(file)+'/spectra'
   with open(path) as f:
        for line in f:
            #print line
            line_no+=1
            if faultM in line:
                return line_no
   return 99999

def DStar(file,val):
    print('file no:',file)
    path=filepath_gzoltar+str(file)
    Ncf = 0 #Number of failed test cases that cover the statement
    Nuf = 0 # Number of failed test cases that do not cover the statement
    Ncs = 0 #Number of successful test cases that cover the statement
    print val
    arr = np.matrix(np.genfromtxt(path+'/matrix', delimiter=" ", dtype=(int)))
    print('arr.shape',arr.shape)
    nRows = arr.shape[0]
    nCols = arr.shape[1]
    print(nRows,nCols)
    dstar = 0.0
    #for i in range(0,nCols-1):
    i=val
    
    for j in range(0,nRows):
            if( arr[j,i]==1 and arr[j,nCols-1]==1):
                Ncs=Ncs+1
            if(arr[j,i]==0 and arr[j,nCols-1]==0):
               Nuf=Nuf+1
            if(arr[j,nCols-1]==0):
               Ncf=Ncf+1
    #print Nuf,Ncs,Ncf
    if(Nuf+Ncs !=0):
            dstar = (float)((Ncf**2)/(Nuf+Ncs))
    return dstar


faultyMethod=""
p = re.compile(r'[a-z]+.+#')
filepath=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Lang/"
path, dirs, files = next(os.walk(filepath))
file_count = len(files)
#print file_count

faultyMethod=""
faulty=[]
for i in range(1,file_count-1):
    if i is 4:
        continue
    path=filepath+str(i)+".dot"
    with open(path) as f:
        for line in f:
            if (("fillcolor=\"red")) in line:
                if p.search(line):
                    faultyMethod=line.split()
                    print faultyMethod[0]
                    faulty.append((i,faultyMethod[0]))
#print((faulty))
labels=[]
val=0
labelVal=99999
highestDscore=0
labelled=[]
for key,faultM in faulty:
    val=int(Spectra(key,faultM))
    #print key,val
    if not val==99999: 
        labelVal=DStar(key,val)
        if labelVal>=2:
           label=1
        elif labelVal<2:
           label=0
        elif labelVal is 99999:
           label=2
    labels.append((key,labelVal))
    labelled.append((key,label))
print(labels)
for fileno,label in labelled:
    print(fileno,label)
avg=0.0
sum=0
for fileno,dstarVal in labels:
    sum+=dstarVal
avg=sum/len(labels)
print 'avg:',avg
	
'''
key,faultM = faulty[0]
val=int(Spectra(key,faultM))
print key,val
if not val==99999: 
   labelVal=DStar(key,val)
labels.append((key,labelVal))
'''