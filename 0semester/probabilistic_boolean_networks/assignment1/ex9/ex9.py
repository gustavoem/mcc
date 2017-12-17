from gene_set import *
from predictor_set import *
from gene_function import *
from boolean_network import *
from state_diagram import *
from random import randrange
from sys import stdin
import copy

def gen_bn (n, obs, total_obs, bns):
    # Algorithm parameters
    a1, a2 = 2, 5 # interval of number of attractors
    min_l, max_l = 2, 10
    min_pred, max_pred = 1, 3
    step1_max_reps = 10
    step2_max_reps = 10
    step4_max_reps = 10
    step6_max_reps = 10
     
    found_bn = False
    # Step 1: generate a random attractor state set
    # TODO: select without repetitions
    
    step1_reps = step1_max_reps
    while (step1_reps):
        step1_reps -= 1
        step2_reps = step2_max_reps
        # print ("\nStarted step 1!")
        N_1 = randrange (a1, a2 + 1)
        attractors = []
        for i in range (N_1):
            r = randrange (total_obs)
            attractors.append (obs[r])
            # print ("Attractor: " + str (obs[r]))

        # Step 2: generate random predictor sets
        while (step2_reps):
            step2_reps -= 1
            step4_reps = step4_max_reps
            # print ("\nStarted step 2!")
            gene_functions = []
            for g in range (n):
                predictor = PredictorSet (n)
                for r in range (randrange (min_pred, max_pred + 1)):
                    predictor.add_rand_gene ()
                gene_functions.append (GeneFunction (predictor, g, n))
                # print ("Predictors of gene " + str (g))
                # print (gene_functions[g].get_predictor_list ())

            # Step 3: verify if predictor set is compatible with 
            # attractor state. This block also sets up gene functions 
            # partially
            is_compatible = True
            for attractor in attractors:
                if (not is_compatible):
                    break
                for g in range (n):
                    gene_function = gene_functions[g]
                    is_compatible = gene_function.check_compatibility \
                        (attractor)
                    # print ("Predictors of gene " + str (g) + 
                            # " are compatible: " + str (is_compatible))
                    if (not is_compatible):
                        break
            # If predictor set is not compatible we should generate 
            # another one
            if (not is_compatible):
                continue
            
            bool_net = BooleanNetwork (n)
            for g in range (n):
                bool_net.set_gene_function (g, gene_functions[g])
            partial_defined_bn = copy.deepcopy (bool_net)
            
            # Step 4: complete function
            # this is done automatically on step 5
            while (step4_reps):
                step4_reps -= 1
                bool_net = copy.deepcopy (partial_defined_bn)
                # Step 5: verify for cycles
                state_diagram = bool_net.get_state_diagram ()
                # print ("Finding state diagram (and completing BN)")
                if (state_diagram.has_cycle ()):
                    # print ("There's a cycle")
                    continue
                else:
                   l = state_diagram.max_level ()
                   # print ("Max level: "  +str (l))
                   if (min_l <= l and l <= max_l):
                       found_bn = True
                       break
                   else:
                       # print ("Too many or too less levels")
                       continue
            if (found_bn):
                break # step 2
        if (found_bn):
            break # step 1
    bns.append (bool_net)
            

# Reads melanoma data
obs = []
obs_count = {}
total_obs = 0
n = 0

for line in stdin:
    line = line.split ()
    n = len (line) 
    state = GeneSet (n)
    for i in range (n):
        if (int (line[i])):
            state.add_gene (i)
    
    obs.append (state)
    state_str = str (state)
    if state_str not in obs_count:
        obs_count[state_str] = 1
    else:
        obs_count[state_str] += 1 
    total_obs += 1

bns = []
gen_bn (n, obs, total_obs, bns)
