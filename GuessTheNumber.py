import random
logo = """
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     

"""

#func to generate random num
def generate_num():
  num = random.randint(1,100)
  return num

# func comparing user number with computer number
def compare_nums(user_guess, generated_number):
  if user_guess > generated_number:
    return "Too high."
  elif user_guess < generated_number:
    return "Too low."
  else:
    return "Congratulations, you got it!"

#func to play game
def play_game():
  
  print(logo)
  print("Welcome to the Number Guessing Game!\n\nI'm thinking of a number between 1 and 100.\n")
  computer_num = generate_num()
  
  game_choice = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
  if game_choice != 'easy' and game_choice != 'hard':
    print("Your choice is invalid! Please answer again.")
  else:
    easy_attempts = 10
    hard_attempts = 5
    
    while game_choice == 'easy':
      print(f"\nYou have {easy_attempts} attempts remaining to guess the number.\n")
      user_guess = int(input("Make a guess: "))
      result = compare_nums(user_guess, computer_num)
      print(result)
      easy_attempts -= 1
      if easy_attempts == 0:
        print("\nYou ran out of attempts.\n")
        print(f"The number was {computer_num}.")
        game_choice = 'stop easy'
      elif user_guess == computer_num:
        game_choice = 'stop easy'
      
    while game_choice == 'hard':
      print(f"\nYou have {hard_attempts} attempts remaining to guess the number.\n")
      user_guess = int(input("Make a guess: "))
      result = compare_nums(user_guess, computer_num)
      print(result)
      hard_attempts -= 1
      if hard_attempts == 0:
        print("\nYou ran out of attempts.\n")
        print(f"The number was {computer_num}.")
        game_choice = 'stop hard'
      elif user_guess == computer_num:
        game_choice = 'stop hard'
    
      
ask_user = input("Would you like to play the Number Guessing Game with me?  Type 'y' or 'n': ")
while ask_user == 'y':
  play_game()
  ask_user_again = input("Would you like to play the Number Guessing Game with me again?  Type 'y' or 'n': ")
  if ask_user_again == 'n':
    ask_user = 'stop'

while ask_user == 'n':
  print("Okay, come back next time!")
  ask_user = 'stop'