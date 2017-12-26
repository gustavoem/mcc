import sys
sys.path.insert (0, '../utils/')

from utils import *
from gene_function import *
from state_diagram import *

class BooleanNetwork ():

    ''' Default constructor '''
    def __init__ (self, n):
        self.n = n
        self.gene_functions = [None] * n
        self.state_diagram = None

    
    ''' Sets the Boolean function that governs a gene '''
    def set_gene_function (self, i, gene_function):
        self.gene_functions[i] = gene_function


    ''' Returns the next state '''
    def next_state (self, state):
        next_state = GeneSet (self.n) 
        for g in range (self.n):
            if (self.gene_functions[g].next_state (state)):
                next_state.add_gene (g)
        return next_state
    

    ''' Creates the state diagram of the Boolean network '''
    def create_state_diagram (self):
        self.state_diagram = StateDiagram (self.n)
        for i in range (2 ** self.n):
            state1 = GeneSet (self.n)
            x = i
            g = 0 
            while (x > 0):
                if (x % 2):
                    state1.add_gene (self.n - 1 - g)
                x //= 2
                g += 1
            state2 = self.next_state (state1)
            self.state_diagram.add_edge (str (state1), str (state2))


    ''' Returns the state diagram '''
    def get_state_diagram (self):
        if (self.state_diagram == None):
            self.create_state_diagram ()
        return self.state_diagram


    ''' Returns the basins of the BoolNet '''
    def get_basins (self):
        return self.state_diagram.get_basins ()


    ''' Returns the number of genes '''
    def get_number_of_genes (self):
        return self.n
