

screen_width = 80
def banner_text(text,screen_width):
    
    """ this function creates a banner around a text
    

    Raises:
        ValueError: if the text is larger than given width a error will be raised
        
    Parameters: 
        Text, Screen Width: these are the text strings inputed by used by using the banner_text() 
        funtion and the screen_width is a integer input asked before the function begins 
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))
        
    

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*",screen_width)
banner_text("Always look on the bright side of life...",screen_width)
banner_text("If life seems jolly rotten,",screen_width)
banner_text("There's something you've forgotten!",screen_width)
banner_text("And that's to laugh and smile and dance and sing,",screen_width)
banner_text(" ",screen_width)
banner_text("When you're feeling in the dumps,",screen_width)
banner_text("Don't be silly chumps,",screen_width)
banner_text("Just purse your lips and whistle - that's the thing!",screen_width)
banner_text("And... always look on the bright side of life...",screen_width)
banner_text("*",screen_width)
# shows doctsring
print(banner_text.__doc__)