panagram='The quick brown fox jumps over the lazy dog'
letters=sorted(panagram)
print(letters)

numbers=[2.3,4.5,8.7,3.1,9.2,1.5]
#make sure if you make a variable sort/sorted that when using the term sorted it will use the variable not the actual function
#sorted=sorted(numbers): this would not work as sorted now is a var

sorted_numbers=sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter=sorted('the quick brown fox jumped over the lazy dog',key=str.casefold)
print(missing_letter)

names=['Graham','John','terry','eric','Terry','michael']

names.sort(str.casefold)
print(names)
