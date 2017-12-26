from predictor_set import *
import random

class GeneFunction ():

    ''' Gene Function constructor '''
    def __init__ (self, pred_set, g, n):
        self.predictors = pred_set
        self.n = n
        self.gene = g
        self.function = {}


    ''' Checks compatibility with a state '''
    def check_compatibility (self, state):
        predictors_s = self._get_predictor_state_str (state)
        gene_s = state.has_gene (self.gene)
        if (predictors_s not in self.function):
            self.function[predictors_s] = gene_s
        else:
            if (self.function[predictors_s] != gene_s):
                return False
        return True
    
    ''' Returns gene next state according to current state '''
    def next_state (self, state):
        predictors_s = self._get_predictor_state_str (state)
        if (predictors_s in self.function):
            gene_s = self.function[predictors_s]
        else:
            # this is the case where we complete the boolean functions
            # randomly
            gene_s = random.choice ([True, False]) 
            self.function[predictors_s] = gene_s
        return gene_s
        
    
    ''' Given the system state and the predictor set, calculates the
        string of the predictor state '''
    def _get_predictor_state_str (self, state):
        predictors = self.predictors
        inter_str = predictors.get_intersection_with (state)
        pred_state_str = ''. join ([inter_str[i] for i in 
                self.predictors.get_predictor_list ()])
        return pred_state_str

    
    ''' Returns a list with indexes of gene predictors '''
    def get_predictor_list (self):
        return self.predictors.get_predictor_list ()
