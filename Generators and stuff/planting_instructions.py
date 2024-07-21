from data import plants_list





plants_list.sort(key=lambda item: '1' + item.name if item.lifecycle=='Perennial' else '0'+item.name)

with open('planting_instructions.txt','w',encoding='utf-8') as output_file:
    for plant in plants_list:
        where_to_plant,who=('window box','me') if plant.lifecycle=='Perennial' else ('garden','gardener')
        print(f'{plant.name} : {where_to_plant}, {who}',file=output_file)