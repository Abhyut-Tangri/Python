#write a program that asks for name and age, if they are between ages 18-30 allow them entry otherwise refuse them 
name=input('hi what is your name?')
age=int(input('what is your age'))
if age>=18 and age<31:
    print('Hi,{0} welcome to our hotel vaction'.format(name))
elif age<18: 
    print('sorry {0} you may come in {1} years'.format(name,18-age))
else:
    print('you are too old sorry {0}'.format(name))