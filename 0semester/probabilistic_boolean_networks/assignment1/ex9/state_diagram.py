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
            s += int_to_binary_string (sef.n, i) + " -> " + \
                 int_to_binary_string (self.n, self.edges[i]) + "\n"
        return s

    
    ''' Adds an edge '''
    def add_edge (self, state1, state2):
        s1_int = binary_string_to_int (state1)
        s2_int = binary_string_to_int (state2)
        self.edges[s1_int] = s2_int

    
    ''' Verifies if there's a cycle on the diagram '''
    def has_cycle (self):
        S = []
        # mark = -1 (not visited)
        #         0 (visited and present on current branch)
        #         1 (visited and not in the current branch)
        mark = [-1] * (2 ** self.n)
        
        for i in range (2 ** self.n):
            if (mark[i]== -1):
                S.append (i)
            while (len (S) > 0):
                v = S[-1]
                mark[v] = 0
                next_v = self.edges[v]
                # print (int_to_binary_string (self.n, v) + " -> " + \
                        # int_to_binary_string (self.n, next_v))
                if (next_v == self.edges[next_v] or mark[next_v] == 1):
                    break
                if (mark[next_v] == 0): # return arc
                    return True
                else:
                    if (mark[next_v] == -1):
                        S.append (next_v)
            while (len (S) > 0):
                v = S.pop ()
                mark[v] = 1
        return False
    

    ''' Calculates the maximum level of a state 
        (distance to an attractor) '''
    def max_level (self):
        level = [-1] * (2 ** self.n)
        S = []

        for s in range (2 ** self.n):
            while (level[s] == -1):
                S.append (s)
                s = self.edges[s] 
                if (s == self.edges[s]):
                    level[s] = 0
            # inv: level[s] != -1 
            while (len (S) > 0):
                s_ant = S.pop ()
                level[s_ant] = level[s] + 1
                s = s_ant
        
        max_level = 0
        for s in range (2 ** self.n):
            if (level[s] > max_level):
                max_level = level[s]
        return max_level


    ''' Returns a dictionary with attractors as keys and basins sizes
        as values '''
    def get_basins (self):
        visited = [False] * (2 ** self.n)
        vertice_basins = [-1] * (2 ** self.n)
        basins = {}
        for i in range (2 ** self.n):
            if (not visited[i]):
                v = i
                S = []
                while (True):
                    visited[v] = True
                    next_v = self.edges[v]
                    S.append (v)
                    if (next_v == v):
                        bstr = int_to_binary_string (self.n, v)
                        if bstr not in basins:
                            basins[bstr] = 0
                        while (len (S) > 0):
                            x = S.pop ()
                            vertice_basins[x] = v
                            basins[bstr] += 1
                        break
                    if (vertice_basins[next_v] != -1):
                        att_v = vertice_basins[next_v]
                        bstr = int_to_binary_string (self.n, att_v)
                        while (len (S) > 0):
                            x = S.pop ()
                            vertice_basins[x] = att_v
                            basins[bstr] += 1
                        break
                    v = next_v
        return basins

                        
                
