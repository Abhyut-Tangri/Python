def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)



# call the function
s1=centre_text("spam and eggs")
print(s1)
s2=centre_text("spam, spam and eggs")
print(s2)
s3=centre_text(12)
print(s3)
s4=centre_text("spam, spam, spam and spam")
print(s4)
s5=centre_text("first", "second", 3, 4, "spam", sep=":")
print(s5)

print()

