numbers=set()
print(numbers,type(numbers))
numbers.add(1)

while len(numbers)<4:
    next_value=int(input('Please enter your next value'))
    numbers.add(next_value)
    
print(numbers)


data=['blue','red','blue','green','red','blue','white']

unique_date=set(data)
print(unique_date)

print()
print(dict.fromkeys(data))
