'''
 Script is used to compute density, diversity, and uniqueness value 
 For running the script: Pass filepath as argument(sometimes throws -'Path not found err'. Hard code number of files in folder.
'''
from __future__ import division
import numpy as np
import os
import sys
import ecopy as ep
from collections import Counter

def duplicate(input,nRows):
   species={}
   for t in range(0,nRows):
      my_lst_str = ''.join(map(str, input[t]))
      h=hash(my_lst_str)
      #print "hash",h
      if h in species:
           species[h]=species[h]+1
      else:
           species[h]=1
   n=0.0
   N=0.0
   for key, value in species.iteritems():
          ni=species[key]
          #print ni
          n+=(ni * (ni - 1))
          N += ni
   #print n,N
   diversity = 1.0 if ( (N == 0.0) or ((N - 1) == 0) ) else n / (N * (N - 1))
   return 1-diversity

#Lang: /mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Lang/Lang/
#Chart: /mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Chart/chart/Chart
filepath=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Mockito/mockito/"

path, dirs, files = next(os.walk(filepath))
file_count = len(files)
print 'Number of files Found:',file_count
#file_count=39

density=[]
diversity=[]
unique=[]
for i in range(1,file_count):
    #print i
    G=[]
    arr = np.matrix(np.genfromtxt(filepath+str(i)+'/matrix', delimiter=" ", dtype=(int)))
    #print(arr.shape)
    nRows = arr.shape[0]
    nCols = arr.shape[1]
    #print 'nRows:',nRows,'nCols:',nCols-1
    arr_w=np.array(arr[0:,0:(nCols - 1)], copy=True)    
    #print 'np.sum(arr_w)',np.sum(arr_w)
    rho=np.sum(arr_w)/(nRows*(nCols-1))
    #print 'rho:',rho
    diff=1-2*rho
    diff =(diff*(-1))if diff<0 else diff
    density.append(1-diff)
    diverse=duplicate(arr_w.tolist(),nRows)
    diversity.append(diverse)
    input=arr_w.T.tolist()
    input = map(tuple,input)
    freqDict = Counter(input)
    # print all rows having frequency greater than 1
    for (row,freq) in freqDict.items():
        G.append(row)
    uniqueness=len(G)/(nCols-1)
    unique.append(uniqueness)

for i in density:
    print i
print "\nDiversity@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
for i in diversity:
    print i
print "\Uniqueness!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
for i in unique:
    print i