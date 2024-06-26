available_parts= {
    '1':'computer',
    '2':'monitor',
    '3':'keyboard',
    '4':'mouse',
    '5':'hdmi cable',
    '6':'DVD drive'
    }


current_choice=None
while current_choice !=0:
    if current_choice in available_parts:
        chosen_part=available_parts[current_choice]
        print(f'adding {chosen_part}')
    else:
        for parts in available_parts:
            print(f'{parts}:{available_parts[parts]}')
        print('0 to finish')
        
    current_choice=input('> ')
        
