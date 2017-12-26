from enum import Enum
from gene_set import *

class PredictorType (Enum):
    INACTIVATION = -1
    UNKNOWN = 0
    ACTIVATION = 1


class PredictorSet (GeneSet):
    
    ''' Predictor Set constructor. All types of predictors are 
        considered UNKOWN '''
    def __init__ (self, n):
        super ().__init__ (n)
        self.prediction_types = []
        for i in range (n):
            self.prediction_types.append (PredictorType.UNKNOWN)

    
    ''' Sets the type of a predictor '''
    def set_predictor_type (self, i, t):
        self.prediction_types[i] = t


    ''' Returns a list with indexes of gene predictors '''
    def get_predictor_list (self):
        return super ().get_genes ()
