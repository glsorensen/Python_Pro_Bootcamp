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

#make list of variables

rps_list = [rock,paper,scissors]


#Have player pick rock, paper, or scissors

player_choice = input("What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors\n")

# Convert choice to integer

player_choice_integer = int(player_choice)

#Match player choice to rps list

rps_player = rps_list[player_choice_integer]

#print the choice

if player_choice_integer == 0:
    print(f"Player has chosen Rock: \n {rps_list[0]}")
elif player_choice_integer == 1:
    print(f"Player has chosen Paper: \n {rps_list[1]}")
else:
    print(f"Player has chosen Scissors: \n {rps_list[2]}")

# Have computer pick rock, paper, or scissors

computer_choice = random.randrange(len(rps_list))


if computer_choice == 0:
    print(f"Computer has chosen Rock: \n {rps_list[0]}")
elif computer_choice == 1:
    print(f"Computer has chosen Paper: \n {rps_list[1]}")
else:
    print(f"Computer has chosen Scissors: \n {rps_list[2]}")

#evaluate who wins

if player_choice_integer == computer_choice:
    print("It's a tie!")
elif (player_choice_integer == 0 and computer_choice == 2) or \
     (player_choice_integer == 2 and computer_choice == 1) or \
     (player_choice_integer == 1 and computer_choice == 0):
    print("You win!")
else:
    print("You lose!")