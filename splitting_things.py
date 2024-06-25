panagram='''The quick brown
fox jumps \t over the lazy dog'''
words=panagram.split()
print(words)

numbers=['9',' ','2','2','3',' ','4','5','8',' ','7','9','0',]
values="".join(numbers)
print(values)
values_list=values.split()
print(values_list)

for index in range(len(values_list)):
    values_list[index]=int(values_list[index])

print(values_list) 

newnum=int(input('enter a value'))
