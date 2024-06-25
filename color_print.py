# some ANSI escape sequences for colors and effects 

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED,'this text will be in red')


def color_print(text: str,*effects:str):
    """ prints text in color 

    Args:
        text (str):the text to print
        effects (str): The effect we want 
    """
    effect_string=''.join(effects)
    output_string='{}{}{}'.format(effects,text,RESET)
    print(output_string)
    
    
color_print(RED,'Hi in red?')
print("This should be in the default terminal colour")
color_print("Hello, Blue", BLUE,BOLD)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
print()
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)