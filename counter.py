# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
x='abcdefghijklmnopqrstuvwxyz'
# Your code goes here ...
for char in text.casefold():
    word_count[char]=len(char)  
    if char.isalnum:
        word_count[char]=word_count.setdefault(char,0) +1  
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
