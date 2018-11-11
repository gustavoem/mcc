# URL form
# http://rest.kegg.jp/<operation>/<argument>[/<argument2[/<argument3> ...]]
# <operation> = info | list | find | get | conv | link | ddi
import requests

# This is where we'll make all calls to
domain_prefix = 'http://rest.kegg.jp'


# Get a list of all organisms
operation = '/list'
database = '/organism'
url = domain_prefix + operation + database
response = requests.get (url)
response_lines = response.text.split ('\n')

# Now we get the line that has information about Mus musculus
# Lines examples:
# T05435  kst Candidatus Kuenenia stuttgartiensis Prokaryotes;Bacteria;Planctomycetes;Kuenenia
# T01800  phm Phycisphaera mikurensis Prokaryotes;Bacteria;Planctomycetes;Phycisphaera
organism_search_query = 'musculus'
matches = []
for line in response_lines:
    if organism_search_query in line:
        print ("We found your query  for \'" + organism_search_query + 
                "\'! Here is the line that contains information about" +
                " this organism:")
        print (line)
        matches.append (line)


if len (matches) == 0:
    print ("No matches for your query!")
elif len (matches) > 1:
    print ("You got more than one matches. Can you specify a " + 
            "little more?")
else:
    organism_line = matches[-1]
    organism_code = organism_line.split ()[1]
    print ("\nOrganism code: " + organism_code)
