text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
new_text=set(text.split())
preps_used=new_text.intersection(prepositions)
print(preps_used)
