def sum_numbers(*args):
    """adds up all numbers given"""
    x=0
    for arg in args:
        x+=arg
    print(x)

sum_numbers(1,2,3)
    
