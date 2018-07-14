# Script is used to compute DStar value based on 'matrix'. Tested on matrix file produced for Mockito buggy version 37
# using gzoltar. 

# 2 represents pass/+
# 3 represents fail/-
from __future__ import division
import numpy as np
import sys

path=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data-Matrix-spectra/method-data/Lang/Lang/1/"
'''
Not required for current gzoltar versions provided
s = open(path+"matrix", "r").read()
s = s.replace('+', '2')
s = s.replace('-','3')
s = s.replace(' ',',')
f = open(path+"matrix_edited", 'w')
f.write(s)
f.close()
no_of_failed=0
no_of_passed=0
'''
Ncf = 0 #Number of failed test cases that cover the statement
Nuf = 0 # Number of failed test cases that do not cover the statement
Ncs = 0 #Number of successful test cases that cover the statement
arr = np.genfromtxt(path+'matrix', delimiter=" ", dtype=(int))
print(arr.shape)

nRows = arr.shape[0]
nCols = arr.shape[1]
scores = np.zeros((nCols-1,1),)
for i in range(0,nCols-1):
    for j in range(0,nRows):
        if( arr[j][i]==1 and arr[j][nCols-1]==1):
               Ncs=Ncs+1
        if(arr[j][i]==0 and arr[j][nCols-1]==0):
               Nuf=Nuf+1
        if(arr[j][nCols-1]==0):
               Ncf=Ncf+1
    if(Nuf+Ncs !=0):
        dstar = (Ncf**2)/(Nuf+Ncs)
        #print(i,dstar)
        scores[i]=dstar
        Ncf = 0 #Number of failed test cases that cover the statement
        Nuf = 0 # Number of failed test cases that do not cover the statement
        Ncs = 0 #Number of successful test cases that cover the statement
print(scores[13])
