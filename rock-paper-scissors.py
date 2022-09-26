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
#Code by Ekta Kapase

list = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 1 for rock, 2 for paper, 3 for scissors."))

print(list[player_choice -1])

print("Computer's choice:\n")

import random

computer_choice = random.choice(list)
print(computer_choice)


if player_choice == 1 and computer_choice == paper:
  print("You lose!")
elif player_choice == 1 and computer_choice == scissors:
  print("You win!")
elif player_choice == 2 and computer_choice == scissors:
  print("You lose!")
elif player_choice == 3 and computer_choice == rock:
  print("You lose!")
elif player_choice == 3 and computer_choice == paper:
  print("You win!")
elif player_choice == 2 and computer_choice == rock:
  print("You win!")
else:
  print("It's tie! ")
