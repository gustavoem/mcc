# Studying KEGG API. I'm trying to get a model from the KEGG api.


# URL form
# http://rest.kegg.jp/<operation>/<argument>[/<argument2[/<argument3> ...]]
# <operation> = info | list | find | get | conv | link | ddi
import requests


# This is where we'll make all calls to
domain_prefix = 'http://rest.kegg.jp'


# Lets see if we can find the identifier for Mus Musculus (mouse).
operation = '/list'
database = '/organism'
url = domain_prefix + operation + database
response = requests.get (url)
print (response)
print (response.text)
