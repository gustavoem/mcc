from random import randrange

class GeneSet:
 
    ''' Default constructor '''
    def __init__ (self, n):
        self.n = n
        self.genes = []

    
    ''' Defines default string representation '''
    def __str__ (self):
        s = ""
        for i in range (self.n):
            if  i in self.genes:
                s += "1"
            else:
                s += "0"
        return s

    
    ''' Adds a gene '''
    def add_gene (self, i):
        self.genes.append (i)
        self.genes.sort ()

    
    ''' Removes a gene '''
    def remove_gene (self, i):
        self.genes.remove (i)


    ''' Returns a list of genes '''
    def get_genes (self):
        return self.genes
    

    ''' Returns true if has gene g '''
    def has_gene (self, g):
        if g in self.genes:
            return True
        else:
            return False

    
    ''' Adds a random gene to the set. Does nothing if all genes 
        already in the set '''
    def add_rand_gene (self):
        ''' Adds a random gene to this gene set '''
        candidates = [g for g in range (self.n) if g not in self.genes]
        r = randrange (len (candidates))
        self.genes.append (candidates[r])
        self.genes.sort ()


    ''' Returns a gene set that is the intersection of two gene sets '''
    def get_intersection_with (self, other):
        inter = GeneSet (self.n)
        for g in range (self.n):
            if self.has_gene (g) and other.has_gene (g):
                inter.add_gene (g)
        return str (inter)
