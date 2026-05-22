#basics
import random
import time
import os


cards =   [11,2,3,4,5,6,7,8,9,10,10,10,10]
def random_cards():
    '''
deal random cards
'''
    random_card= random.choice(cards)
    return random_card

#append

def calculate(cards):
    '''
    this function count the score
    '''    
    #black jack?
    if sum(cards) == 21 and len(cards)==2:
        return 0
    
    #11 in cards
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)    

#scores

def clear_screen():
    os.system('cls') if os.name=='nt' else os.system('clear')

def compare(player_score,dealer_score):
    messages ={
        'p over 21': '💥 BOOM! You went over 21. You lose! 💸',
        'dealer over 21': '🤖 Computer went bust! You win! 🎉',
        'p_black jak': '🃏 BLACKJACK! You hit the jackpot! 🏆',
        'dealer balck jak': '💀 Ouch! Computer got 21. Better luck next time! 📉',
        'draw ': '👔 It\'s a Draw! Both scores are equal. 🤝',
        'dealer win': '🦁 The Dealer wins this round! You lose. ❌',
        'p_win ': '🔥 NICE! Your score is higher. You won! 💰'
    }
    if player_score>21:
        return messages['p over 21']
    elif dealer_score>21:
        return messages['dealer over 21']
    elif player_score ==21:
        return messages['p_black jak']
    elif dealer_score ==21:
        return messages['dealer balck jak']
    elif dealer_score == player_score:
        return messages['draw']
    elif player_score> dealer_score:
        return messages['p_win']
    elif dealer_score>player_score:
        return messages['dealer win']
    elif dealer_score >21 and player_score>21:
        return messages['draw']

def leader():
    clear_screen()
    player_cards=[random_cards() for _ in range(2)]
    dealer_cards=[random_cards()for _ in range(2)]
    game_continue = True
    
    # player turn
    while game_continue:
        player_score = calculate(player_cards)
        dealer_score = calculate(dealer_cards)
        print(f'\n\nur cards are {player_cards} with score {player_score}')
        print(f'computer first card is {dealer_cards[0]}')
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_continue = False
        else:
            another_card = input('do u want another card? (yes/no):').lower()
            if another_card == 'yes':
                player_cards.append(random_cards())
            else:
                game_continue = False
    
    # dealer turn - UPDATED: recalculate score inside the loop
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(random_cards())
        dealer_score = calculate(dealer_cards) # Recalculate score here

    print(f'\n\nur cards are {player_cards} with score {player_score}')
    print(f'computer cards are {dealer_cards} with score {dealer_score}')
    print(compare(player_score, dealer_score))



def start():
    print('starting game....please wait ')
    time.sleep(2)
    print('''
       
       /\          
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`
''')
    print('''
  ____  _               _____ _  __       _         _____ _  __
 |  _ \| |        /\   / ____| |/ /      | |  /\   / ____| |/ /
 | |_) | |       /  \ | |    | ' /       | | /  \ | |    | ' / 
 |  _ <| |      / /\ \| |    |  <    _   | |/ /\ \| |    |  <  
 | |_) | |____ / ____ \ |____| . \  | |__| / ____ \ |____| . \ 
 |____/|______/_/    \_\_____|_|\_\  \____/_/    \_\_____|_|\_\
                                                                                                       
''')
    rules = '''  
### **The Goal**

Beat the dealer by getting closer to **21** without going over.

---

### **Card Values**

* **2-10:** Face value
* **J, Q, K:** 10
* **Ace:** 1 or 11

---

### **The Play**

1. **Deal:** You get two cards. Dealer gets one up, one down.
2. **Hit:** Take a card (to get closer to 21).
3. **Stand:** Keep your cards (and end your turn).
4. **Bust:** If you go over 21, you lose instantly.

---

### **Winning**

* **Higher than dealer:** You win.
* **Lower than dealer:** You lose.
* **Dealer busts:** You win.
* **Tie:** You keep your money (a "Push").
'''
    question = input('print yes if u want to know the rules:').lower()
    if question == 'yes':
        print(rules)
    input('press any key to continue')
    clear_screen()

def game():
    start()
    leader()

#results
while True:
 game()
 start_again= input('do u wanna play another round (y/n)?:').lower()
 clear_screen()
 if start_again== 'y':
     game()

 else:
     break