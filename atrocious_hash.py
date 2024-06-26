data= [
    ('orange','a sweet orange citrus fruit'),
    ('apple','good for making cider'),
    ('lemon',' a sour yellow citrus fruit'),
    ('grape','a small sweet fruit growing in bunches'),
    ('melon','sweet and juicy')
]
#print(ord('a'))
#print(ord('b'))
#print(ord('z'))

def simple_has(s:str)-> int:
    """A ridicously simple hasing functions"""
    basic_hash=ord(s[0])
    return basic_hash%10


def get(k:str)-> str:
    """return a value for the string if none, retrun none"""
    hash_code=simple_has(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None
    

keys=[""] * 10    
values=keys.copy()


for key,value in data:
    h=simple_has(key)
    print(key,h)
    keys[h]=key
    values[h]=value

print(keys)
print(values)
print()
value=get('grape')
print(value)
