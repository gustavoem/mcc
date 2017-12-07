from gene_set import *
from predictor_set import *
from gene_function import *
from random import randrange
from sys import stdin

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

# Step 1: generate a random attractor state set
N_1 = randrange (2, 5 + 1)
attractors = []
for i in range (N_1):
    r = randrange (total_obs)
    attractors.append (obs[r])

# Step 2: generate random predictor sets
gene_functions = []
for g in range (n):
    predictor = PredictorSet (n)
    for r in range (randrange (1, 3 + 1)):
        predictor.add_rand_gene ()
    gene_functions.append (GeneFunction (predictor, g, n))
    

# Step 3: verify if predictor set is compatible with attractor state
# This block also sets up gene functions partially
for attractor in attractors:
    for g in range (n):
        gene_function = gene_functions[g]
        print ("\nState " + str (attractor))
        print ("Predictors of gene " + str (g))
        print (gene_function.get_predictor_list ())
        gene_function.check_compatibility (attractor)
