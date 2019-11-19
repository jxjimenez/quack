import random
wheel={'0':'green','00':'green','1':'red','2':'black','3':'red','4':'black','5':'red','6':'black','7':'red','8':'black','9':'red','10':'black','11':'black','12':'red','13':'black','14':'red','15':'black','16':'red','17':'black','18':'red','19':'red','20':'black','21':'red','22':'black','23':'red','24':'black','25':'red','26':'black','27':'red','28':'black','29':'black','30':'red','31':'black','32':'red','33':'black','34':'red','35':'black','36':'red'}
player='x'
bank=0

result = random.choice(list(wheel.items()))  # will return result of random color/number for roulette game


#------------------------lobby will allow user to input name and bank. Will also guide user to table games.
def lobby():
    global player
    while player =='x':
        player=input('what is your name?\n')
    global bank
    while bank==0:
        bank=int(input('welcome '+player+',how much would you like in chips?\n''$'))
    game=input('What game would you like to play? Roulette(r) or Blackjack(b) or Quit(q)\n')
    if game=="r":
        roul()
    elif game=='b':
        black()
    elif game== 'q':
        quit()
    else:
        print('Hmm, I don\'t understand')
        lobby()
#------------------------Roulette will pick random results from result function based on wheel
def roul():
    global bank
    bet=input('Roulette table is open for bets. You have $'+str(bank)+'. How much would you like to bet:\n$')
    while int(bet)>bank:
        print('You don\'t have enough chips for that')
        roul()
    wager=input('where would you like to place your wager? 00,0-36, Red, or Black\n')
#    if wager == '00':
#       print('No more bets')
#   else:
#       print('that is an illegal wager')
#       roul()
    print('spinning...spinning...spinning...')
    num=result[0]
    color=result[1]
    print(num +" "+ color+'!')
    if str(wager)==result[0]:
        winning=int(bet)*35
        print('You win $'+str(winning))
        bank+=int(bet)*35
        print('You now have $'+str(bank)+' in chips')
    elif wager==str(result[1]):
        print('you win!')
        bank+=int(bet)
        print('You now have $'+str(bank)+' in chips')
    else:
        print('Sorry. Better luck next time!')
        bank-=int(bet)
        print('You now have $'+str(bank)+' remaining.')
    if bank>0:
        again=input('would you like to play again? y/n\n')
        if again=='y':
            roul()
        elif again=='n':
            lobby()
        else:
            print('Hmm, maybe the front desk can help with that')
            lobby()
    else:
        print("Sorry you\'re out of money. Might be time to hit the Mad Ducks Credit Union for some funds.")
        lobby()

#------------------------Blackjack will deal hands to player and dealer
def black():
    print('This service is not yet available')
    lobby()

#------------------------Quits the program
def quit():
    print("Thank you for playing!")


print('Welcome to Madducks Casino!')
lobby()
