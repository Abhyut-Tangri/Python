x=0
while x<10:
    print('x is now {0}'.format(x))
    x=x+1
import random
answer=random.randint(0,10)
print('please guess a number between 1 and 10')
print(answer)
guess=int(input())
if guess==answer:
    print('wow {0} is the correct answer'.format(answer))
while guess != answer:
    if guess>answer:
        print('please guess lower')
    else:
        print('guess higher')
    guess=int(input())
    if guess==answer:
        print('wow great job you got it right')
        break
    else:
        continue
    