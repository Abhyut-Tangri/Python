print(__file__)

numbers=[1,2,3,4,5,6]

#squares=[number**2 for number in numbers]
squares=[number **2 for number in range(1,7)]

print(squares)

screen_width=int(input('screen layout'))

if screen_width==500:
    print('tablet layout')
elif screen_width<700:
    print('mobile layout')
else:
    print('desktop layout')


message='tablet layout' if screen_width==500  else 'desktop layout'
print(message)