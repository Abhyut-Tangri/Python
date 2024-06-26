import copy
from sahllow_copy import animals
new_dict={}
your_dict={}
def deep_copy(d:dict) -> dict:
    for key,value in d.items():
        new_value=value.copy()
        your_dict[key]=new_value
    
    return new_dict
    

new=deep_copy(animals)
print(new)
