print(__file__)

numbers=[1,2,3,4,5,6]

number=int(input('please enter a number and i will tell you the square'))

squares=[]
for number in numbers:
    squares.append(number**2)
print(squares)

index_pos=numbers.index(number)    
print(squares[index_pos])