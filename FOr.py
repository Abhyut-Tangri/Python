sum=0
for x in range (1,11,2):
    #print(x)
    sum=sum+x
    if x==5:
        print(x)
        break
    
print(sum)
x=0
while x<11:
    print(x)
    x=x+1
    break
list1=(1,2,3)
print(type(list1))
list2=[1,2,3]
print(type(list2))
list3={1,2,3}
print(type(list3))
list5=list2+list2
print(list5)
x='hello world'

for i in range (0,11):
    print(x[i])
for c in x:
    print(c)


for j in range(0,10):
    if j%2==0:
        print(j)
zy=[1,5,532,123]
print(zy[:-1])
print(len(zy))
print(sorted(zy))
print(zy.pop(1))
set2=(2,3,54,6,123,2,123)
print(set2[2])
#set2[2]=11
popsd=[1,2,3,4,5]
popsd[2]=5
print(popsd)
dict1={1:3,'hello':3,1.3:3}
print(dict1)
dict2={'apple':4,'orange':2,'banna':5}
print(dict2['orange'])
dict2['orange']=4
print(dict2['orange'])
dict2['peach']=6
print(dict2)
print(dict2['peach'])
for k in dict2:
    print(k)
    print(dict2[k])
print(dict2.keys())
for i in range(1,13):
    print('No {0} squared is {1} and cubed is {2}'.format(i,i**2,i**3))
name=input('whats yo name big dawg')
age=input('i aint no josh giddy but still whats your age')
print(name + f' is {age} years old')