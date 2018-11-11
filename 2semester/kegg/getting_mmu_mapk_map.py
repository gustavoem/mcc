# URL form
# http://rest.kegg.jp/<operation>/<argument>[/<argument2[/<argument3> ...]]
# <operation> = info | list | find | get | conv | link | ddi
import requests

# This is where we'll make all calls to
domain_prefix = 'http://rest.kegg.jp'

# First, lets get the list of all maps
operation = '/list'
database = '/pathway'
organism = '/mmu' # Mus muscular code
url = domain_prefix + operation + database + organism
response = requests.get (url)
response_lines = response.text.split ('\n')

# Now we get the line that has information about RAS/MAPK pathway
# Line examples:
# path:mmu05219  Bladder cancer - Mus musculus (mouse)
# path:mmu05220   Chronic myeloid leukemia - Mus musculus (mouse)
pathway_query = 'MAPK'
matches = []
for line in response_lines:
    if pathway_query.lower () in line.lower ():
        print ("We found your query  for \'" + pathway_query + 
                "\'! Here is the line that contains information about" +
                " this pathway:")
        print (line)
        matches.append (line)

if len (matches) == 0:
    print ("No matches for your query!")
elif len (matches) > 1:
    print ("You got more than one matches. Can you specify a " + 
            "little more?")
else:
    pathway_line = matches[-1]
    pathway_code = pathway_line.split ()[0].replace ('path:', '')
    print ("\nPathway code: " + pathway_code)

# Gets the first matched pathway kgml and save file
operation = '/get'
database = '/' + pathway_code
option = '/kgml'
url = domain_prefix + operation + database + option
response = requests.get (url)
f = open("mmu_mapk.kgml", "w")
f.write (response.text)
f.close
