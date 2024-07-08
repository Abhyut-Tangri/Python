a_string='this is \n string split \t and tabbed'
print(a_string)

#ignores tabs etc
raw_string=r'this is \n string split \t and tabbed'
print(raw_string)

b_string='this is'+chr(10)+'a string split'+chr(9)+'and tabbed'
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
print(error_string)