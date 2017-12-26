from utils import *

class PBN ():
    
    ''' Default Constructor '''
    def __init__ (self):
        self.bns = []
    

    ''' Adds a BN '''
    def add_bn (self, bn):
        self.bns.append (bn)


    ''' Estimates stationary distribution of informed attractors '''
    def get_attractors_dist (self, attractors):
        stationary_dist = {}
        for att in attractors:
            stationary_dist[str (att)] = 0.0
        
        attr_mass = 0
        for bn in self.bns:
            basins = bn.get_basins ()
            for bn_att in basins:
                if bn_att in stationary_dist:
                    attr_mass += basins[bn_att]
                    stationary_dist[bn_att] += basins[bn_att]
        for att in stationary_dist:
            stationary_dist[att] /= attr_mass

        return stationary_dist


    ''' Returns an array containing the probabilities of transitioning
        to each state '''
    def get_next_state_prob (self, current_state):
        n = len (str (current_state))
        m = len (self.bns)
        p = [0.0] * (2 ** n)
        for bn in self.bns:
            next_state = bn.next_state (current_state)
            s = binary_string_to_int (str (next_state))
            p[s] = 1 / m
        return p
    

    ''' Returns the number of genes '''
    def get_number_of_genes (self):
        if len (self.bns) > 0:
            return self.bns[0].get_number_of_genes ()
        else:
            return 0 
