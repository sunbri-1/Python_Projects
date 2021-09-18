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
import random
choices = [rock, paper, scissors]
computer_choice = (random.choice(choices))
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
human_choice = choices[human_choice]

print(f"You Chose: \n {human_choice}")
print(f"Computer Chose: \n {computer_choice}")
if human_choice == computer_choice:
  print("Draw.")
elif (human_choice == choices[0]) and (computer_choice == choices[1]):
  print("You Lose.")
elif (human_choice == choices[1]) and (computer_choice == choices[2]):
  print("You lose.")
elif (human_choice == choices[2]) and (computer_choice == choices[0]):
  print("You lose.")
else:
  print("You win!")
