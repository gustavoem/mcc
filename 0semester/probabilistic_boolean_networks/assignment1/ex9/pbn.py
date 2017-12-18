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
   
