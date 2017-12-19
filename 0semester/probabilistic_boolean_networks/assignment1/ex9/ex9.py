from gene_set import *
from predictor_set import *
from gene_function import *
from boolean_network import *
from state_diagram import *
from pbn import *
from random import randrange
from sys import stdin
from sys import exit
import copy
import numpy as np
import matplotlib.pyplot as plt 
    
# Algorithm parameters
a1, a2 = 2, 5 # interval of number of attractors
min_l, max_l = 2, 10
min_pred, max_pred = 1, 3
step1_max_reps = 100
step2_max_reps = 100
step4_max_reps = 100
step6_max_reps = 100
n_pbns = 10000
reps_on_attractor_set = 100


def gen_bn (n, attractors, bns):
    found_bn = False
    step2_reps = step2_max_reps
    # Step 2: generate random predictor sets
    while (step2_reps):
        step2_reps -= 1
        step4_reps = step4_max_reps

        gene_functions = []
        for g in range (n):
            predictor = PredictorSet (n)
            for r in range (randrange (min_pred, max_pred + 1)):
                predictor.add_rand_gene ()
            gene_functions.append (GeneFunction (predictor, g, n))

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
        bns.append (bool_net)
    return found_bn


def distribution_mse (dist1, dist2):
    mse = 0.0
    for att in dist1:
        mse += (dist1[att] - dist2[att]) ** 2
    return mse / (len (dist1))


# Reads melanoma data
obs = []
obs_prop = {}
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
    if state_str not in obs_prop:
        obs_prop[state_str] = 1
    else:
        obs_prop[state_str] += 1 
    total_obs += 1
melanoma_attractors = list (obs_prop.keys ())

for s in obs_prop:
    obs_prop[s] /= total_obs

print ("Observation prob: ")
print (obs_prop)

# Generates 10 sets of attractors and BNs for each set
bns = []
for i in range (10):
    bns.append ([])

    # Step 1: generate a random attractor state set
    # TODO: select without repetitions
    step1_reps = step1_max_reps
    while (step1_reps):
        bns[i] = []
        step1_reps -= 1
        N_i = randrange (a1, a2 + 1)
        attractors = []
        for k in range (N_i):
            r = randrange (total_obs)
            attractors.append (obs[r])

        # For this attractor set we should generate 100 BNs
        for j in range (reps_on_attractor_set):
            # this call adds the bn to bns[i]
            found_bn = gen_bn (n, attractors, bns[i])
            if (not found_bn):
                break

        if (not found_bn):
            continue
        else:
            break

    if (len (bns[i]) == 0):
        print ("Sorry, we repreated Algorithms 1 steps too many" + \
               "times and still couldn't find BNs. Try " + \
               "increasing repetition parameters.")
        exit () 

# PBN generation (choose 10 random BNs)
pbns = []
for k in range (n_pbns):
    pbn = PBN ()
    for i in range (10):
        r = randrange (0, len (bns[i]))
        pbn.add_bn (bns[i][r])
    pbns.append (pbn)


# Find PBN with minimum MSE
minbn = 0
minmse = distribution_mse (obs_prop, \
        pbns[0].get_attractors_dist (melanoma_attractors))
for i in range (1, len (pbns)):
    mse = distribution_mse (obs_prop, \
        pbns[i].get_attractors_dist (melanoma_attractors))
    if (mse < minmse):
        minmse = mse
        minbn = i

predicted_dist = pbns[minbn].get_attractors_dist (melanoma_attractors)
print ("Predicted prob: ")
print (predicted_dist)


original_data = []
observed_data = []
for attractor in obs_prop:
    original_data.append (obs_prop[attractor])
    observed_data.append (predicted_dist[attractor])


# Plot attractors distribution
bar_width = .70
n_range = np.arange (len (melanoma_attractors)) * 2
ones = np.ones (len (melanoma_attractors)) * .7

axes = plt.gca ()
bar_label = "Original attractor distribution"
rects = plt.bar (n_range, original_data, bar_width, label=bar_label)
plt.legend ()

axes = plt.gca ()
bar_label = "Predicted attractor distribution"
rects = plt.bar (n_range + ones, observed_data, bar_width, label=bar_label)
plt.legend ()

plt.xlabel ('Attractor state')
plt.ylabel ('Normalized frequency')
plt.title ('')
plt.xticks ([])
plt.show ()
