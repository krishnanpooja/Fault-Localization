'''
Some matrix files contain TABS instead of space. The code below replaces these TABS with spaces. 
WARNING: Ideally needs to be run only once.
'''
import sys
path=sys.argv[1]#"/mnt/c/Users/Pooja/Desktop/2ndsem/Praktikum/method-data/method-data/Closure/closure/120/"

s = open(path+"matrix", "r").read()
s = s.replace('	',' ')
f = open(path+"matrix_edited", 'w')
f.write(s)
f.close()