import shelve

print(dir())
print()
print(dir(shelve))

help(shelve)
for obj in dir(shelve.Shelf):
    if obj[0]!='_':
        print(obj)
        
shelve.Shelf()