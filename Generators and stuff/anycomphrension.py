from data import people,plants_dict,plants_list

#people=[]

if bool(people) and all([person[1] for person in people]):
    print('sending email')
else:
    print('User must edit the list of recipients')

if any([plant.plant_type=='Grass' for plant in plants_list]):
    print('this pack contains grass')
else:
    print('No grasses in this pack')
    

if any([plant.plant_type=='Grass' for plant in plants_dict.values()]):
    print('this pack contains grass')
else:
    print('No grasses in this pack')


if any([plant.plant_type=='Cactus' for plant in plants_dict.values()]):
    print('this pack contains cacti')
else:
    print('No cacti in this pack')
