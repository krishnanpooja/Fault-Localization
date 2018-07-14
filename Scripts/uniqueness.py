'''
Code to test the uniquness code used as DYNAMIC matrix. Python script created for TESTING.
'''
# Function to find duplicate rows in a binary matrix
from collections import Counter
import ecopy as ep
import numpy as numpy
import math
def duplicate(input):
   species={}
   for t in range(0,4):
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
   


# Driver program
if __name__ == "__main__":
    input = [[1,1,0,0],
             [0,0,1,1],
             [1,1,1,0],
             [0,0,0,1]]
    '''
    input = [[1,1,0,0],
             [1,1,0,0],
             [1,1,0,0],
             [1,1,0,0]]
    '''
    print(duplicate(input))
