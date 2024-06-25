parrot='Norwegian Blue'
letter=input('give me a letter')
if letter in parrot:
    print('{0} is a letter in {1}'.format(letter,parrot))
else:
    print('need a new letter')
