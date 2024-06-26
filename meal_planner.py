from contents import recipes, pantry
need_to_buy={}
display_dict={}
for index, key in enumerate(recipes):
    display_dict[str(index+1)]=key
while True:
    print('please choose your recipe')
    print('-------------------------')
    for key, value in display_dict.items():
        print(f'{key}-{value}')
    
    choice= input(': ')
    
    if choice=='0':
        break
    elif choice in display_dict:
        selected_item=display_dict[choice]
        print(f'you have selected {selected_item}')
        print('checking ingredients')
        ingredients=recipes[selected_item]
        print(ingredients)
        for food_item,required_quantity in ingredients.items():
            quantity_in_pantry=pantry.get(food_item,0)
            if required_quantity <= quantity_in_pantry:
                print(f'{food_item} ok')
            else:
                quantity_to_buy=required_quantity-quantity_in_pantry
                print(f'you need to buy {quantity_to_buy} of {food_item}')
                need_to_buy[food_item]=quantity_to_buy
                
        print(f'you need {need_to_buy}')
            