def multiply(x,y):
    result=x*y
    return result
    """_summary_ multiplies x and y value given in parentheses, for example in answer=multiply(10.5,4)
        the returned result after multiplying is 42
        
        Return: returns result of multiplication
        
    """

def palindrome_true(string):
    backward=string.lower()
    return backward[::-1]==backward


def palindrome_sentence(sentence):
    strings=''
    for char in sentence:
        if char.isalnum():
            strings+= char
    return strings[::-1].casefold()==strings.casefold()


def fibonacci_sequence(n):
    """ write a code that calculates fibonaccis(x +y= z then do y+z=a and z+a=b and so on)
    
    param: n
    """
    if 0 <=n<=1:
        return n
    n_minus1, n_minus2=1,0
    result=None
    for f in range(n-1):
        result=n_minus2+n_minus1
        n_minus2=n_minus1
        n_minus1=result
    return result


for i in range(36):
    print(i, fibonacci_sequence(i))
sentences=input('please put in a sentence')

if palindrome_sentence(sentences):
    print('{} is a palindrome'.format(sentences))
else:
    print('{} is not a sentence'.format(sentences))    

word=input('please enter a word to check for palindromes:')
if palindrome_true(word):
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))   
#format for functions is two line seperation above and below
answer=multiply(10.5,4)
print(answer)

for val in range(1,5):
    two_times=multiply(2,val)
    print(two_times)

