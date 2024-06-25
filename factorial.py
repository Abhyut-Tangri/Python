#def factorial_numbers(x):
def factorial(int):
    """ returning the factorial in n!

    Args:
        int (number): input value
        Returns: factorial
        _type_: integer
    """
    if int<=1:
        return 1
    result=2
    for i in range(2,int+1 ):
        result*=i
    return result

for j in range(36):
    print(j, factorial(j))
           