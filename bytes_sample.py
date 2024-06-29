equation=bytes((207,128,114,194,178))
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b,end=',')
print()
print(equation.decode('utf-8'))