import random

action_u = input("Enter a choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
action_c = random.choice(actions)
print(f"\nYou chose {action_u}, computer chose {action_c}.\n")

if action_u == action_c:
    print(f"Both players selected {action_c}. It's a tie!")
elif action_u == "rock":
    if action_c == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif action_u == "paper":
    if action_c == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif action_u == "scissors":
    if action_c == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")