import fizzbuzz
input('play fizz buzz')
print()

next_number=0
while next_number<99:
    next_number+=1
    print(fizzbuzz.fizz_buzz(next_number))
    next_number+=1
    correct_answer=fizzbuzz.fizz_buzz(next_number)
    players_answer=input()
    if players_answer!=correct_answer:
        print('you lose the correct answer was {}'.format(correct_answer))
        break
else:
    print('well done you reaced {}'.format(next_number))     
    
    