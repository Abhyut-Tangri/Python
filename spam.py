#check how to format properly
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

"""for food in menu:
    if 'spam' not in food:
        print(food)
    else:
        
        print(food)
"""
for yolk in menu:
    for item in yolk:
        if item=='spam':
            yolk.remove(item)
    print(yolk, end='')


"""
for meal in menu:
    items=','.join((item for item in meal if item != 'spam))
    print(items)"""

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=='spam':
            del meal[index]
    print(','.join(meal))
