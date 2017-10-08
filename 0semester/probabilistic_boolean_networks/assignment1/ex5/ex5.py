import sys
sys.path.insert (0, '../ex4/')
sys.path.insert (0, '../utils/')

from ex4.py import buffered_input
from utils.py import *


n = int (buffered_input ())
p = float (buffered_input ())
M = []
for i in range (n):
    M.append ([])
    for j in range (n):
        M[i].append (int (buffered_input ()))

print (M)
