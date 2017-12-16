import sys
sys.path.insert (0, '../utils/')

from utils import *

class StateDiagram ():

    ''' Default constructor '''
    def __init__ (self, n):
        self.n = n
        self.edges = []
        n_states = 2 ** n
        for i in range (n_states):
            self.edges.append (-1)

    ''' Defines the diagram string representation '''
    def __str__ (self):
        s = ""
        for i in range (2 ** self.n):
            s += int_to_binary_string (sef.n, i) + " -> " +
                 int_to_binary_string (self.n, self.edges[i]) + "\n"
        return s

    
    ''' Adds an edge '''
    def add_edge (self, state1, state2):
        s1_int = binary_string_to_int (state1)
        s2_int = binary_string_to_int (state2)
        self.edges[s1_int] = s2_int

    
    ''' Verifies if there's a cycle on the diagram '''
    def has_cycle (self):
        S = [0]
        marked = []
        for i in range (2 ** self.n):
            marked = False
        
        for i in range (2 ** self.n):
            if (marked[i] == False):
                S.append (i)
            while (len (S)):
                v = S.pop ()
                if (marked[v]):
                    return True
                next_v = self.edges[v]
                if (next_v != -1):
                    S.append (next_v)
        return False
