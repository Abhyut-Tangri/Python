import sys
def factorial(n):
    #n! cam also be definded as n*(n-1)
    """ Calculates n! recursively""" 
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
#print(factorial(900))

try:
    print(factorial(1000))
except (RecursionError,OverflowError):
    print('This program cannot calculate factorials not that large')
except ZeroDivisionError:
    print('no dividing by zero')
print('programing terminating')

n=(input('please insert a number'))
e=(input('Please insert a number to divide the first number by'))

try:
    print(int(n)/int(e))
except ZeroDivisionError:
    print('change your second number from zero')
    sys.exit(2)
except ValueError:
    print('only type valid numbers into the prompt')
finally:
    print('division performed succesfully')