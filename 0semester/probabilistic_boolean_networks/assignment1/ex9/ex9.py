from gene_set import *
from predictor_set import *
from gene_function import *
from random import randrange
from sys import stdin
import copy

def gen_bn (n, obs, total_obs):
    step1_max_reps = 100
    step2_max_reps = 100
    step4_max_reps = 100

    # Step 1: generate a random attractor state set
    # TODO: select without repetitions
    while (step1_max_reps):
        step1_max_reps -= 1
        print ("\nStarted step 1!")
        N_1 = randrange (2, 5 + 1)
        attractors = []
        for i in range (N_1):
            r = randrange (total_obs)
            attractors.append (obs[r])
            print ("Attractor: " + str (obs[r]))

        # Step 2: generate random predictor sets
        while (step2_max_reps):
            step2_max_reps -= 1
            print ("\nStarted step 2!")
            gene_functions = []
            for g in range (n):
                predictor = PredictorSet (n)
                for r in range (randrange (1, 3 + 1)):
                    predictor.add_rand_gene ()
                gene_functions.append (GeneFunction (predictor, g, n))
                print ("Predictors of gene " + str (g))
                print (gene_functions[g].get_predictor_list ())

            # Step 3: verify if predictor set is compatible with 
            # attractor state. This block also sets up gene functions 
            # partially
            is_compatible = True
            for attractor in attractors:
                if (not is_compatible):
                    break
                for g in range (n):
                    gene_function = gene_functions[g]
                    is_compatible = gene_function.check_compatibility (attractor)
                    print ("Predictors of gene " + str (g) + " are compatible: " + str (is_compatible))
                    if (not is_compatible):
                        break
            # If predictor set is not compatible we should generate 
            # another one
            if (not is_compatible):
                continue
            
            print ("great!")
            return

            # bool_net = BooleanNetwork (n)
            # for g in range (n):
                # bool_net.set_gene_function (g, gene_functions[g])
            # partial_defined_bn = copy.deepcopy (bool_net)
            
            # while (step4_max_reps):
                # bool_net = copy.deepcoopy (partial_defined_bn)
                # Step 4: complete function
                # this is done automatically on step 5
                # Step 5: verify for cycles





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


gen_bn (n, obs, total_obs)
