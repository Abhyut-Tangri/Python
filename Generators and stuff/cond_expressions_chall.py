age=int(input('how old are you'))

message='you are old enough to vote' if age>=18 else 'Please come back in {} years'.format(18-age)
print(message)