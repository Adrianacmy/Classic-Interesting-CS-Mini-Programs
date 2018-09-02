'''
python -m pdb some.py

l: list current program code
n: next step
c: continue, till the end of the program or next breakpoint
b 7: break at line7
clear 7: clear the 7th breakpoint
cl: clear breakpoint
s: step into a funciton
p a: print the value of parameter a
a: print all args
q: quit
r: return excu to the last line of the code

-----------------------------------------------

debug interactively

import pdb
pdb.run("func(args)")
l
s

----------------------------------------------

import pdb
# add below line in the code where breakpoint needed
pdb.set_trace() # program will stop at this line

'''

def sum(a, b):
    return a + b


a = 100
b = 200
sum(a, b)