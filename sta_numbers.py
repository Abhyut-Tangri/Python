numbers=(1,2,3,4,5)
print(numbers,sep=';')
#* before tuple values unpacks them
print(*numbers,sep=';')
# semicolon only applies to the individual values so the first print does not use the semicolon

def tes_star(*args):
    print(args)
    for x in args:
        print(x)

tes_star(0,1,2,3,4,5)
print()
tes_star()
