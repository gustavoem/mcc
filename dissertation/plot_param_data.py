import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import numpy as np

data_file = sys.argv[1]

class FullSample:

    def __init__ (self):
        self.data = []
        self.models = []
        self.model_params = {}

    def add_data (self, d):
        self.data.append (d)
    
    def get_full_sample (self):
        return list (self.data)
    
    def get_model_sample (self, sample, model):
        model_idx = self.models.index (model)
        return [s for s in sample if s[0] == model_idx]

    def get_iteration_sample (self, sample, iteration):
        return [s for s in sample if s[1] == iteration]

    def add_model (self, model_name, parameters):
        self.models.append (model_name)
        self.model_params[model_name] = parameters

    def get_all_models (self):
        return self.models

    def get_model_params (self, model):
        return self.model_params[model]


def plot_parameter_distribution (param_sample, param_name, fig_name):
    x = np.array (param_sample)
    sns_plot = sns.kdeplot (x, label=param_name)
    fig = sns_plot.get_figure ()
    plt.legend ()
    fig.savefig (fig_name)
    plt.clf ()


# Process data
f = open (data_file, 'r')
sample_obj = FullSample ()
for line in f:
    v = line.split ()
    if v[0].isdigit ():
        model = int (v[0])
        iteration = int (v[1])
        data = [model, iteration]
        data += [float (p) for p in v[2:]]
        sample_obj.add_data (data)
    else:
        model_name = v[0]
        parameters = v[1:]
        sample_obj.add_model (model_name, parameters)
        
# Plot data
all_models = sample_obj.get_all_models ()
full_sample = sample_obj.get_full_sample ()

for model in all_models:
    parameters = sample_obj.get_model_params (model)
    sample = sample_obj.get_model_sample (full_sample, model)
    # sample = sample_obj.get_iteration_sample (sample, 2)
    
    for p in parameters:
        p_idx = parameters.index (p)
        param_sample = [obs[2 + p_idx] for obs in sample]
        fig_name = model + '_p' + str (p_idx) + '_' + p + '.png'
        plot_parameter_distribution (param_sample, p, fig_name)
