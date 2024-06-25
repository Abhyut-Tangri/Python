"""#current_choice='-'
computer_parts=[]
while current_choice != '0':
    if current_choice in '123456':
        print('adding {}'.format(current_choice))
        if current_choice=='1':
            computer_parts.append('computer')
        elif current_choice=='2':
            computer_parts.append('monitor')
        elif current_choice=='3':
            computer_parts.append('keyboard')
        elif current_choice=='4':
            computer_parts.append('mouse')
        elif current_choice=='5':
            computer_parts.append('mousemat')    
        elif current_choice=='6':
            computer_parts.append('hdmi cable')        
    else:
        print('please add options from list below')
        print('1:computer')
        print('2:monitor')
        print('3:keyboard')
        print('4:mouse')
        print('5:mousemat')
        print('6:hdmi cable')
        print('0:to finish')
    current_choice = input()
print('these are all your parts {}'.format(computer_parts))"""
valid_choice=[]
available_parts=['computer','monitor','mouse', 'keyboard', 'mousemat','hdmi cable']
for i in range(1,len(available_parts)+1):
    valid_choice.append(str(i)) 
print(valid_choice)
current_choice="-"
computer_parts=[]
while current_choice!='0':
    if current_choice in valid_choice:
        print('adding {}'.format(current_choice))
        index=int(current_choice)
        chosen_part=available_parts[index]
        if chosen_part in available_parts:
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
            
                    
    else:
        print('please add options from the list below:')
        for number, part in enumerate(available_parts):
                print("{0}: {1}".format(number + 1, part ))
