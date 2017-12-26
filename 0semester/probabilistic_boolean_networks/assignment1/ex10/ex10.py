from algorithm1 import *
import numpy as np


def final_cost (state):
    if (state.has_gene (0)):
        return 10000
    else:
        return 10


def get_all_states (n):
    states = []
    for i in range (0, 2 ** n):
        x = i
        s = GeneSet (n)
        j = n - 1
        while (x > 0):
            if (x % 2):
                s.add_gene (j)
            x //= 2
            j -= 1
        states.append (s)
    return states


def get_planning (pbns, M):
    n = pbns[0].get_number_of_genes ()
    all_states = get_all_states (n)
    two_tothe_n = 2 ** n
    plan = np.zeros ((two_tothe_n, M))
    costs = np.zeros ((two_tothe_n, M + 1))
    
    # final costs
    for i in range (two_tothe_n):
        costs[i, M] = final_cost (all_states[i])
        
    # intermediate costs
    for m in range (M - 1, -1, -1):
        for i in range (two_tothe_n):
            state = all_states [i]
            t0 = np.array (pbns[0].get_next_state_prob (state))
            t1 = np.array (pbns[1].get_next_state_prob (state))
            v = costs[:, m + 1]
            u0_cost = 2 * m + np.dot (t0, v) 
            u1_cost = 10 * m + np.dot (t1, v) 
            if (u0_cost < u1_cost):
                plan[i, m] = 0
                costs[i, m] = u0_cost
            else:
                plan[i, m] = 1
                costs[i, m] = u1_cost
    
    print ("Costs:")
    print (costs)
    return plan



# Melanoma data processing
both_net_obs = [[], []]
both_net_obs_prop = [{}, {}]
both_net_total_obs = [0, 0]
both_net_melanoma_attractors = [[], []]

for line in stdin:
    line = line.split ()
    pirin = int (line.pop (0))
    n = len (line)
    state = GeneSet (n)
    for i in range (n):
        if (int (line[i])):
            state.add_gene (i)
    both_net_obs[pirin].append (state)
    state_str = str (state)
    if state_str not in both_net_obs_prop[pirin]:
        both_net_obs_prop[pirin][state_str] = 1
    else:
        both_net_obs_prop[pirin][state_str] += 1
    both_net_total_obs[pirin] += 1
for i in range (2):
    for s in both_net_obs_prop[i]:
        both_net_obs_prop[i][s] /= both_net_total_obs[i]
    both_net_melanoma_attractors[i] = \
            list (both_net_obs_prop[i].keys ())

# print ("Observed prob with pirin off: ")
# print (both_net_obs_prop[0])
# print ("Observed prob with pirin on: ")
# print (both_net_obs_prop[1])



# Finds a PBN for both contexts (pirin on or off)
pbns = []
for pirin in (0, 1):
    pbns.append (get_min_mse_pbn (n, both_net_obs[pirin], \
        both_net_obs_prop[pirin], both_net_total_obs[pirin]))

# predicted_dist = pbns[0].get_attractors_dist (both_net_melanoma_attractors[0])
# print ("Predicted prob with pirin off: ")
# print (predicted_dist)
# predicted_dist = pbns[1].get_attractors_dist (both_net_melanoma_attractors[1])
# print ("Predicted prob with pirin on: ")
# print (predicted_dist)

plan = get_planning (pbns, 5)
print ("\nTreatment plan:")
print (plan)
