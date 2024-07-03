import tkinter
import random

streak = 0

def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
        
    # For each suit retrieve the image for the cards
    for suit in suits:
        # First the number cards 1 through 10
        for card in range(1, 11):
            name = 'blackjackpictures/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        # Next, face cards
        for card in face_cards:
            name = 'blackjackpictures/{}_{}.{}'.format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global deck

    # Destroy the old frames and create new ones
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    
    # Create a new deck and shuffle it
    deck = list(cards)
    random.shuffle(deck)

    result_text.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    
    
def deal_cards(frame):
    # Pop the next card off the top of the deck
    next_card = deck.pop(0)
    # Add the image to a label and display the label     
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # Now return the card's face value
    return next_card


def shuffle():
    random.shuffle(deck)
    

def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for card in hand:
        card_value = card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    
    dealer_score = score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(deal_cards(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set('Dealer wins')
        streak = 0
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player wins')
        streak = 1
    elif dealer_score > player_score:
        result_text.set('Dealer wins')
        streak=0
    else:
        result_text.set('Draw')


def deal_player():
    player_hand.append(deal_cards(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    
    if player_score > 21:
        result_text.set('Dealer Wins')





# Set up the screen and frames for dealer and player
mainwindow = tkinter.Tk()

mainwindow.title('Black Jack')
mainwindow.geometry('640x480')
mainwindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text, background='green', fg='white')
result.grid(row=0, column=0, columnspan=3)

# Streak
streak_label = tkinter.Label(mainwindow, text='Streak: {}'.format(streak), fg='white', background='green')
streak_label.grid(row=0, column=3)

card_frame = tkinter.Frame(mainwindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, columnspan=3, sticky='ew')

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')



player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# Embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')


dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

#clear game button
newgame=tkinter.Button(button_frame,text='New Game',command=new_game)
newgame.grid(row=0,column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# Load cards
cards = []
load_images(cards)

# Create a deck of cards and shuffle them
deck = list(cards) + list(cards) + list(cards)
random.shuffle(deck)

# Create the list to store the dealer's and player's hands
player_hand = []
dealer_hand = []


deal_player()
dealer_hand.append(deal_cards(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

mainwindow.mainloop()
