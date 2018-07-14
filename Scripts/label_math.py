'''
The file computes Labels for MATH. 
Pass two arguments: argument 1 - path to the file containing the list of faulty methods in MATH. Uploaded. Please     download and use.
                    argument 2 - path of the matrix and spectra file
'''
from __future__ import division
import os
import re
import sys
import numpy as np
from os import listdir
from os.path import isfile, join

filepath_gzoltar=sys.argv[2]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Math/math/"
def Spectra(file,faultM):
       faultM=faultM.replace('.dot','')
       faultM=faultM.replace('Test','')
       #print "fault method to be searched:",faultM
       line_no=0
       path=filepath_gzoltar+str(file)+'/spectra'
       #print("###################################################################################################")
       with open(path) as f:
           for line in f:
               #print line
               line_no+=1
               if faultM in line:
                   return line_no
       #print("###################################################################################################")
       return 99999

def DStar(file,val):
    #print('file no:',file)
    path=filepath_gzoltar+str(file)
    Ncf = 0 #Number of failed test cases that cover the statement
    Nuf = 0 # Number of failed test cases that do not cover the statement
    Ncs = 0 #Number of successful test cases that cover the statement
    #print val
    arr = np.matrix(np.genfromtxt(path+'/matrix', delimiter=" ", dtype=(int)))
    #print('arr.shape',arr.shape)
    nRows = arr.shape[0]
    nCols = arr.shape[1]
    #print(nRows,nCols)
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

labels=[]
val=0
labelled=[]
path=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/graphs/Math_FaultMethods.txt"
count=0
with open(path, 'r') as myfile:
    content = myfile.readlines()
content = [x.strip() for x in content] 
for data in content:
    if "Math_" in data:
        count+=1
    elif "unknown" in data:
        labels.append((count,99999))
        labelled.append((count,2))
    elif not data is "":
        val=int(Spectra(count,data))
        if not val==99999: 
           labelVal=DStar(count,val)
           if labelVal>=2:
              label=1
           elif labelVal<2:
              label=0
           elif labelVal is 99999:
              label=2
        labels.append((count,labelVal))
        labelled.append((count,label))
for key,val in labelled:
    print(key,val)
        
