import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  return sum(cards)

def compare_cards(player_score, computer_score):
  if player_score == computer_score:
    return "Draw.\n"
  elif computer_score == 21:
    return "Lose, computer has BlackJack!\n"
  elif player_score == 21:
    return "Win with a Blackjack\n"
  elif computer_score > 21:
    return "Computer went over, you win!\n"
  elif player_score < computer_score:
    return "Computer has a higher score. You lose!\n"
  elif player_score > computer_score:
    return "You have a higher score. You win!\n"

def play_game():
  
  # conditions
  draw_cards = True
  compare = True

  # deal cards
  player_cards = []
  computer_cards = []
  
  for i in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

  # add up player and computer scores
  player_score = calculate_score(player_cards)
  computer_score = calculate_score(computer_cards)
  

  # check for winners before continuing
  if player_score == 21:
    draw_cards = False
    compare = False
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}\n")
    print("BlackJack! You have a score of 21, you win!\n")
  elif computer_score == 21:
    draw_cards = False
    compare = False
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}\n")
    print("Computer has BlackJack, you lose!\n")
  else:
    # display player card and scores
    # display computer first card
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}\n")


  #loop when player draws cards
  while draw_cards == True:
    pick_card = input("Do you want to draw another card? Type 'y' or 'n': ")
    if pick_card == 'y':
      new_player_card = deal_card()
      if new_player_card == 11:
        new_player_card = 1
      player_cards.append(new_player_card)
      player_score += new_player_card
      
      print(f"\nYour cards: {player_cards}, current score: {player_score}\n")
      
      if player_score > 21:
        print("You went over, you lose :(\n")
        draw_cards = False
        compare = False
      elif player_score == 21:
        print("You win!\n")
        draw_cards = False
        compare = False
        
    if pick_card == 'n':
      draw_cards = False
    
  while computer_score < 17:
    new_computer_card = deal_card()
    if new_computer_card == 11:
      new_computer_card = 1
    computer_cards.append(new_computer_card)
    computer_score += new_computer_card
    if 11 in computer_cards and calculate_score(computer_cards) > 21:
        computer_cards.remove(11)
        computer_cards.append(1)

  # compare after player stops drawing cards
  while compare:
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Computer cards: {computer_cards}, current score: {computer_score}\n")
  
    results = compare_cards(player_score, computer_score)
    compare = False
    print(results)



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()