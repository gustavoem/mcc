import libsbml
from libsbml import Reaction
from libsbml import Parameter
from libsbml import SBMLNamespaces

def get_sbml_namespaces(model):
    namespaces = SBMLNamespaces()
    namespaces.addNamespaces(model.getNamespaces())
    return namespaces


def find_sbml_species_ref(model, species_id):
    # all_species = model.getListOfSpecies()
    # for species in all_species:
        # if species_ref.getId() == species_name:
    species_ref = model.getSpeciesReference(species_id) 
    return species_ref


def add_reaction(model, namespace):
    # reaction = Reaction(namespace)
    reaction = model.createReaction()
    reactants = ['RAF_P']
    products = ['RAF']
    kineticlaw_str = 'V * RAF_P / (Km + RAF_P)'
    kineticlaw_params = ['V', 'Km']
    params_initialvalue = {'V': 1, 'Km': 1}
    
    for reactant in reactants:
        reactant_species_ref = find_sbml_species_ref(model, reactant)
        reaction.addReactant(reactant_species_ref)
    for product in products:
        product_species_ref = find_sbml_species_ref(model, product)
        reaction.addProduct(product_species_ref)

    kinetic_law = reaction.createKineticLaw()
    kinetic_law.setFormula(kineticlaw_str)
    for param in params_initialvalue:
        param_obj = kinetic_law.createParameter()
        param_obj.setName(param)
        param_obj.setId(param)
        param_obj.setValue(params_initialvalue[param])
    return reaction


reader = libsbml.SBMLReader()
sbmldoc = reader.readSBML("starting_model.sbml")
if sbmldoc.getNumErrors() > 0:
    print("Oh... smth is wrong on the SBML.")

# converter = libsbml.SBMLFunctionDefinitionConverter()
# converter.setDocument(sbmldoc)
# converter.convert()
model = sbmldoc.model

sbml_namespaces = get_sbml_namespaces(model)
add_reaction(model, sbml_namespaces)

writer = libsbml.SBMLWriter()
writer.writeSBML(sbmldoc, 'test.sbml')
