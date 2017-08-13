# Maxwell Andrew
# Apr 23, 2015
# Interactive game of Blackjack

from Tkinter import *
from random import randint

suits = ['spades','hearts','diamonds','clubs']
ranks = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
# computer as p1
p1 = []
# player as p2
p2 = []
# values of each card
val = {}

for i in range(len(ranks)):
    if i >= 9:
        val.update({ranks[i]:10})
    else:
        val.update({ranks[i]:i+1})
    
def play_action():
    global deck
    global p1
    global p2

    # reset game
    p1 = []
    p2 = []
    dealer_text.delete('0.0', END)
    player_text.delete('0.0', END)
    de.set('Dealer:')
    pl.set('Player:')
    
    deck = make_deck()
    shuffle(deck)
    
    deal(p1)
    deal(p1)
    deal(p2)
    deal(p2)
    
    player_text.insert(END, make_card(p2[0],p2[1]),'\n')
    player_text.insert(END, make_card(p2[2],p2[3]),'\n')
    # keep first hand hidden
    dealer_text.insert(END,'***\n')
    dealer_text.insert(END,make_card(p1[2],p1[3]),'\n')

    if is_blackjack(p1) or is_blackjack(p2):
        finish_game()
        return None

    play_button['state'] = DISABLED
    hit_button['state'] = NORMAL
    stand_button['state'] = NORMAL

def hit_action():
    deal(p2)
    player_text.insert(END, make_card(p2[len(p2)-2],p2[len(p2)-1]),'\n')
    if get_value(p2) > 21:
        finish_game()

def stand_action():
    while get_value(p1) < 17:
        h = 4
        deal(p1)
        dealer_text.insert(END,make_card(p1[h],p1[h+1]),'\n')
        h += 2
    finish_game()

def shuffle(deck):
    for k in range(100): # do it 100 times
        card = deck.pop(randint(0,51)) # remove a random card from the deck
        deck.append(card)

def make_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit,rank))
    return deck
deck = make_deck()
shuffle(deck)

def make_card(suit,rank):
    return rank + ' of ' + suit + '\n'

def deal(player):
    global deck
    card = deck.pop(randint(0,len(deck)-1))
    player += card

def is_blackjack(player):
    for i in player:
        if (val.get(player[0][1]) == 1 or val.get(player[0][1]) == 10) and (val.get(player[1][1]) == 1 or val.get(player[1][1]) == 10):
            return True
        else:
            return False

def get_value(player):
    value = 0
    for i in range(1,len(player),2):
        if player[i][:] == 'ace':
            if value + 10 <= 21:
                value += 10
            else:
                value += 1
        else:
            value += val.get(player[i])
    return value

def finish_game():
    # show card
    dealer_text.delete('1.0', '2.0')
    dealer_text.insert('0.0',make_card(p1[0],p1[1]),'\n')
    
    de.set('Dealer: ' + str(get_value(p1)))
    # determine winner
    if is_blackjack(p1) and is_blackjack(p2):
        pl.set('Push')
    elif is_blackjack(p1):
        pl.set('House wins')
    elif is_blackjack(p2):
        pl.set('Player wins')
    elif get_value(p2) > 21:
        pl.set('Player busts')
    elif get_value(p1) > 21:
        pl.set('House busts')
    elif get_value(p1) > get_value(p2):
        pl.set('House wins')
    elif get_value(p2) > get_value(p1):
        pl.set('Player wins')
    elif get_value(p1) == get_value(p2):
        pl.set('Push')

    play_button['state'] = NORMAL
    hit_button['state'] = DISABLED
    stand_button['state'] = DISABLED


window = Tk()
window.title('Blackjack')

# create the text widgets
pl = StringVar()
player_label = Label(window,textvariable=pl)
pl.set('Player:')
player_label.grid(row=0,column=0,sticky='W')
player_score = Label(window)
player_score.grid(row=0,column=1,sticky='W')
player_text = Text(window,width=40)
player_text.grid(row=1,column=0,columnspan=3,padx=10,pady=10)

de = StringVar()
dealer_label = Label(window,textvariable=de)
de.set('Dealer:')
dealer_label.grid(row=0,column=3,sticky='W')
dealer_score = Label(window)
dealer_score.grid(row=0,column=4,sticky='W')
dealer_text = Text(window,width=40)
dealer_text.grid(row=1,column=3,columnspan=3)

# create buttons
play_button = Button(window,text='Play',command=play_action)
play_button.grid(row=2,column=0,columnspan=2)
hit_button = Button(window,text='Hit Me',command=hit_action)
hit_button.grid(row=2,column=2,columnspan=2)
stand_button = Button(window,text='Stand',command=stand_action)
stand_button.grid(row=2,column=4,columnspan=2)

play_button['state'] = NORMAL
hit_button['state'] = DISABLED
stand_button['state'] = DISABLED

window.mainloop()
