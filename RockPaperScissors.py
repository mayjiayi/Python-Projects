import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#printing player's choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

choices = [rock, paper, scissors]
if player_choice < 3 and player_choice>=0:
  print(f"You chose:\n{choices[player_choice]}")
  
  #printing computer's choice
  computer_choice = random.randint(0,2)
  
  if computer_choice == 0:
    print("Computer chose:" + rock)
  elif computer_choice == 1:
    print("Computer chose:" + paper)
  else:
    print("Computer chose:" + scissors)
  
  #printing win/lose statement
  if player_choice+1 == computer_choice:
    print("You lose.")
  elif player_choice == 2 and computer_choice ==0:
    print("You lose.")
  elif player_choice == computer_choice:
    print("Draw.")
  else:
    print("You win.")
else:
  print("You typed an invalid number, you lose!")