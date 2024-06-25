import random


highest = int(input('how high would you like the game to go to (please enter a number)'))


def get_integer(prompt):
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print('{} is invalid try a number less than {}'.format(temp,highest))
        
answer = random.randint(1, highest)
print(answer)
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))
 
while guess != answer:
    guess = get_integer(': ')
    if guess == 0:
        break
    elif guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
