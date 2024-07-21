import timeit

text = "what have the romans ever done for us"

# Define your functions
def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals

def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words

def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w

# Main block
if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())

    # Timing the functions
    print(timeit.timeit("comp_caps()", setup='from __main__ import comp_caps', number=10000))
    print(timeit.timeit("map_caps()", setup='from __main__ import map_caps', number=10000))
    print(timeit.timeit("comp_words()", setup='from __main__ import comp_words', number=10000))
    print(timeit.timeit("map_words()", setup='from __main__ import map_words', number=10000))

