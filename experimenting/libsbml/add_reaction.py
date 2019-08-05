import libsbml
from libsbml import Reaction
from libsbml import Parameter
from libsbml import SBMLNamespaces

def get_sbml_namespaces(model):
    namespaces = SBMLNamespaces()
    namespaces.addNamespaces(model.getNamespaces())
    return namespaces


def find_sbml_species(model, species_name):
    all_species = model.getListOfSpeciesTypes()
    for species in all_species:
        if species.getId == species_name:
            return species


def create_reaction(model, namespace):
    reaction = Reaction(namespace)
    reactants = ['RAF_P']
    products = ['RAF']
    kineticlaw_str = 'V * RAF_P / (Km + RAF_P)'
    kineticlaw_params = ['V', 'Km']
    params_initialvalue = {'V': 1, 'Km': 1}
    
    for reactant in reactants:
        reactant_species = find_sbml_species(model, reactant)
        reaction.addReactant(reactant_species)
    for product in products:
        product_species = find_sbml_species(model, reactant)
        reaction.addProduct(product_species)

    kinetic_law = reaction.createKineticLaw()
    kinetic_law.setFormula(kineticlaw_str)
    for param in params_initialvalue:
        param_obj = Parameter(namespace)
        param_obj.setName(param)
        param_obj.setId(param)
        param_obj.setValue(params_initialvalue[param])
        kinetic_law.addParameter(param_obj)
    print(reaction.getKineticLaw().getFormula())
    return reaction


reader = libsbml.SBMLReader()
sbmldoc = reader.readSBML("starting_model.sbml")
if sbmldoc.getNumErrors() > 0:
    print("Oh... smth is wrong on the SBML.")


converter = libsbml.SBMLFunctionDefinitionConverter()
converter.setDocument(sbmldoc)
converter.convert()
model = sbmldoc.model

sbml_namespaces = get_sbml_namespaces(model)
reaction = create_reaction(model, sbml_namespaces)

print(model.addReaction(reaction))
print(model)

print(libsbml.LIBSBML_INVALID_OBJECT)

writer = libsbml.SBMLWriter()
writer.writeSBML(sbmldoc, 'test.sbml')
