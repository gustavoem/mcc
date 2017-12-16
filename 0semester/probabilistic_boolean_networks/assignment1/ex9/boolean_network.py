from gene_function import *

class BooleanNetwork ():

    ''' Default constructor '''
    def __init__ (self, n):
        self.n = n
        self.gene_functions = [None] * n
    
    ''' Sets the Boolean function that governs a gene '''
    def set_gene_function (self, i, gene_function):
