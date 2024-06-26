d= {
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}


pantry_items=['chicken','spam','egg','bread','lemon']

d2={
    7:'lucky seven',
    10:'ten',
    3:'this the new 3'
}

d.update(d2)

for key, value in d.items():
    print(key,value)


print()

d.update(enumerate(pantry_items))
for key,value in d.items():
    print(key,value)


v=d.values
print(v)

d[10]='ten'
print(v)

#print('four' in v)
#print('eleven' in v)

keys=list(d.keys())
value=list(d.values)

if 'four' in value:
    index= value.index('four')
    key=key[index]
    print(f'{d[key]} was found with the key {key}')
