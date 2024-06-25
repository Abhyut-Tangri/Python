data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]

"""
del data[0:2]
print(data)
#make sure to account for new places of value if intending to delete
del data[14:]
"""

# be careful when changing the size of a object being iterated over 
min_valid=100
max_valid=200
stop=0
for index,value in enumerate(data):
    if (value>=min_valid) :
        stop=index
        break
         
print(stop)
del data[:stop]


start=0

for index in range(len(data)-1,-1,-1):
    if data[index] <= max_valid:
        #we have the index of the last item to keep
        #set start to the position of the first 
        #item to delete which is 1 after the index
        start=index+1
        break
print(start)
del data[start:]
print(data)

