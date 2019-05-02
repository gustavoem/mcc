import os 
import re

models = ['model1', 'model2', 'model3', 'model4']
parameters = {'model1': ['compartment', 'k_1', 'k_2', 'k_3', 'k_4', 'V', 
    'K_m'],
    'model2': ['compartment', 'k_1', 'V_1', 'k_2', 'k_3', 'V_2'],
    'model3': ['compartment', 'V_1', 'k_1', 'V_2', 'k_2'],
    'model4': ['compartment', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6', 
        'k_7']
}

output_file = 'bioinformatics_gamma_abc_results.txt'
out = open (output_file, 'w')

current_dir = os.getcwd ()
pop_number_regex = re.compile ("Population_(\d+)")

# First line of the output is the header:
# model1_name parameters_of_the_model1
# model2_name parameters_of_the_model2
# ...
# modelm_name parameters_of_the_modelm

for m in models:
    line = m + ' ' + ' '.join (parameters[m][1:]) + '\n'
    out.write (line)


for m in models:
    all_pop_names = \
        [x for x in os.walk (current_dir + '/results_' + m)][0][1]
    n_params = len (parameters[m])
    model_idx = models.index (m)
    
    for pop in all_pop_names:
        pop_num = pop_number_regex.match (pop).group (1)
        pop_dir = current_dir + '/results_' + m + '/' + pop
        f = open (pop_dir + '/data_Population' + str (pop_num) + '.txt')
        for line in f:
            v = line.split ()
            # removing compartments 
            params = v[1:n_params]
            # model_idx iteration parameter_values
            line = str (model_idx) + ' ' + pop_num + ' ' + \
                    ' '.join (params) + '\n'
            out.write (line)
