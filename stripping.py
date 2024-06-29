def removeprefix(string:str,prefix:str)->str:
    if string.starts(prefix):
        return string[len(prefix):]
    else:
        return string[:]
    
    
def remove_suffix(string:str,suffix:str)->str:
    if suffix and string.endswith(suffix):
    #suffix should not start with string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]

file_name='Jabberwocky.txt'
with open(file_name) as poem:
    first=poem.readline().rstrip()

print(first)
chars="'Twasebv"
#no_apostrophe=first.strip(chars)
#print(no_apostrophe)
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
for character in first[::-1]:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
    
#twas_removed=first.removeprefix("'Twas")
twas_removed=removeprefix(first,"'Twas")
print(twas_removed)
toves_removed=first.removesuffix('toves')
print(toves_removed)