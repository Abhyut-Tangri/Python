newnum=(input('Enter the three values seperated by commas'))
newnumbers=(newnum.split(','))
print(newnumbers)
for index in range(len(newnumbers)):
    newnumbers[index]=int(newnumbers[index])
print(newnumbers)

a=newnumbers[0]
b=newnumbers[1]
c=newnumbers[2]
print(a+b-c)