import copy


lion_list=['scary','big','cat',]
elephant_list=['big','grey','wrinkled']
teddy_list=['cuddly','stuffed'] 
animals= {
    'lions':lion_list,
    'elephant':elephant_list,
    'teddy':teddy_list      
    
}

#shallow copy
#things=animals.copy()

#deepcopy

things=copy.deepcopy(animals)


print(things['teddy'])
print(animals['teddy'])

print()
teddy_list.append('toy')

print(things['teddy'])
print(animals['teddy'])
