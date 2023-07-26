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

#Write your code below this line 👇

opt = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
com = random.randint(0, 2)

# Game Rule

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

print(f"You \n {opt[user]}")

print(f"Computer \n {opt[com]}")

user_rock = opt[user] == opt[0]
user_paper = opt[user] == opt[1]
user_scissors = opt[user] == opt[2]


com_rock = opt[com] == opt[0]
com_paper = opt[com] == opt[1]
com_scissors = opt[com] == opt[2]


if user_rock and com_scissors:
  print("You Win")
elif user_scissors and com_paper:
  print("You Win")
elif user_paper and com_rock:
  print("You Win")
elif user_paper and com_paper or user_rock and com_rock or user_scissors and com_scissors:
  print("Draw")
else:
  print("You lose")
