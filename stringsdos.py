parrot='Norwegian Blue'
#python starts from 0
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
#slicing, you can also do negative indexing, does not incluide final
print(parrot[:6])
print(parrot[6:])
print(parrot[:6]+ parrot[6:])
#you can also use negatives 
print(parrot[-4:-2])
print(parrot[-4:12])
#also you can slice with steps where the third val is how much you skip by
print(parrot[0:6:3])
alphabet='abcdefghijklmnopqrstuvwxyz'
print(alphabet[16:13:-1])
age=24
print('my age is {0} tommorow'.format(age))
print('there are {0} days in {1}'.format(28,'Feb'))