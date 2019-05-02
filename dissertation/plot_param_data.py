import sys

data_file = sys.argv[1]

class FullSample:

    def __init__ (self):
        self.data = []
        self.models = []
        self.model_params = {}

    def add_data (self, d):
        self.data.append (d)

    def get_model_sample (self, sample, model):
        return [s for s in sample if s[0] == model]

    def get_iteration_sample (self, sample, iteration):
        return [s for s in sample if s[1] == iteration]

    def add_model (self, model_name, parameters):
        self.models.append (model_name)
        self.model_params[model_name] = parameters

    def get_all_models (self):
        return self.models

    def get_all_model_params (self, model):
        return self.model_params[model]

    
f = open (data_file, 'r')

my_sample = FullSample ()
for line in f:
    v = line.split ()
    if v[0].isdigit ():
    else:
        model_name = v[0]
        parameters = v[1:]
        my_sample.add_model (model_name, parameters)
        
