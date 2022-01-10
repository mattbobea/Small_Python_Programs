############### Blackjack Project #####################
import random
import os
  
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#----------------Functions----------------

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Generates starting hands
def generate_hands():
  #generate user's hand
  user_hand = []
  user_hand.append(cards[random.randint(0,12)])
  user_hand.append(cards[random.randint(0,12)])
  #generate computer's hand
  computer_hand = []
  computer_hand.append(cards[random.randint(0,12)])
  computer_hand.append(cards[random.randint(0,12)])
  return user_hand, computer_hand

#User gets a new random card
def add_user_card(user_hand3):
  random_card = random.choice(cards)
  user_hand3.append(random_card)
  return user_hand3

#Checks for Blackjack 
def check_hand(user_func, dealer_func):
  if dealer_func == 21:
    return 100
  elif user_func == 21:
    return 90
  elif user_func > 21:
    return 80
  elif dealer_func > 21:
    return 70
  else:
    return 10

#prints end game text
def end_print (score):
  if score == 100:
    print("The dealer has won!")
  elif score == 90:
    print("Blackjack! You won!")
  elif score == 80:
    print("Sorry, you busted!")
  elif score == 70:
    print("The dealer busted! You win!")

def convert_aces(convert_hand):
   index = -1
   for conv_card in convert_hand:
      index += 1
      if conv_card == 11:
            convert_hand[index] = 1
            return convert_hand
      else:
        return convert_hand



#----------------Main Code----------------
#Starting variables
是 = "y"
want_to_play = "yes"

while (want_to_play == "yes" 
or  want_to_play == "y" 
or  want_to_play == "是"):
  #displays starting hand while solidfying variables.  
  clearConsole()
  print(logo)
  user_hand = generate_hands()[0]
  dealer_hand = generate_hands()[1]
  user_total = user_hand[0]+user_hand[1]
  dealer_total = dealer_hand[0]+dealer_hand[1]

  #prints starting informaiton
  print(f"Your starting hand is: {user_hand[0]} and {user_hand[1]}\nYour total is: {user_total}")
  print(f"The dealer's starting hand is: {dealer_hand[0]} and a face down card")

  #check hands
  check_score = check_hand(user_total, dealer_total)
  if check_score > 10:  
    end_print(check_score)
  else:
    while input("Do you want another card?\nType yes or no: ").lower() == "yes":
      #adds a new card to the user's hand
      user_hand = add_user_card(user_hand3=user_hand)
      #calcualtes the user's new total
      user_total=0
      for card in user_hand:
        user_total += card
      if user_total>21:
        user_hand = convert_aces(user_hand)
        user_total = 0
        for var in user_hand:
          user_total += var

      check_score = check_hand(user_total, dealer_total)
      print(f"your new hand is:{user_hand}\nYour new total is: {user_total}")
      #checks if the user won or busted and prints coresponding text.
      if check_score > 10:  
        end_print(check_score)
        hit = "no"
      else:
        hit = input("Do you want another card?\nType yes or no: ").lower()

  #dealer will keep drawing cards until their score goes over 16.
  if check_score == 10:
    while dealer_total < 17:
      #adds a card to the dealer's hand
      dealer_hand = add_user_card(user_hand3=dealer_hand)
      #calcualtes the user's new total
      dealer_total = 0
      for card in dealer_hand:
        dealer_total += card
      print(f"The dealer chooses to draws a card.  Her new hand is {dealer_hand} and her new total is {dealer_total}")
      #checks is the dealer busted
    if dealer_total > 21:
      print("The dealer busted! you win!")
    else:
      if user_total > dealer_total:
        print(f" You have {user_total} and the dealer has {dealer_total}. \n You win!")
      else: 
        print(f"You have {user_total} and the dealer has {dealer_total}. \n You Lose!")
  #for num in range(0, len(user_hand)):
  #  user_total = user_total + user_hand[num]
  #print(user_hand[0])
  #user_total = user_hand[0] + user_hand[1]
  
  
  
  want_to_play = input("Do you want to play another game? yes/no? \n").lower()
