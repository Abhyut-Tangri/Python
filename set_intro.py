farm_animals={'cow','sheep','hen','horse','goat'}
#sets are unodered
#also cannot INDEX sets
for animal in farm_animals:
    print(animal)
    
    
more_animals={'cow','sheep','hen','horse','goat'}
if more_animals==farm_animals:
    print('sets are equal')
else:
    print('sets are not equal')

#if you make another set that is equal to another, such as more animals and farm animals they will both randomize in parralael to eachother

print(more_animals)
print(farm_animals)