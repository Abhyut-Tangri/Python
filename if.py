name=input('whats your name?')
age=int(input('what is your age, {0} ?'.format(name)))
if age <18:
    print('you are {0} years too young to vote'.format(18-age))
elif age>900:
    print('die already fr')
else:
    print('you are eligible to vote')

#guess game
answer=43
print('guess a number between 1 and 100')
guess=int(input('what is your guess'))
if answer>guess:
    print('guess higher')
    hint=input('would you like a hint')
    if hint=='yes':
        print('guess higher by {0}'.format(answer-guess))
elif answer==43:
    print('wow you got it right')
else: 
    print('you got it wrong try less')
    hint2=input('would you like a hint')
    if hint2=='yes':
        print('try something a little lower from your value closer to {0} less'.format(guess-answer))
if age==15 or age==10:
    print('go back to bed bucko')