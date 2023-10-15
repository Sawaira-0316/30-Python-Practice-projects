import random

choices = ['rock', 'scissor', 'paper']

while True:
    computer_score = 0
    user_score = 0

    user_choice = int(input('''
    Start Game...
    1. Yes
    2. No / Exit
    '''))

    if user_choice == 1:
        for _ in range(1, 6):
            user_input = int(input('''
    1. Rock
    2. Scissor
    3. Paper
            '''))

            user_choice_text = choices[user_input - 1]
            computer_choice = random.choice(choices)

            if computer_choice == user_choice_text:
                print("Computer choice:", computer_choice)
                print("User choice:", user_choice_text)
                print("Game Draw")
            elif (user_choice_text == "rock" and computer_choice == "scissor") or \
                 (user_choice_text == "scissor" and computer_choice == "paper") or \
                 (user_choice_text == "paper" and computer_choice == "rock"):
                print("Computer choice:", computer_choice)
                print("User choice:", user_choice_text)
                print("You win")
                user_score += 1
            else:
                print("Computer choice:", computer_choice)
                print("User choice:", user_choice_text)
                print("Computer wins")
                computer_score += 1

        print("\nFinal Game Result:")
        if user_score == computer_score:
            print("Final game Draw")
        elif user_score > computer_score:
            print("You win the final game")
        else:
            print("Computer wins the final game")

        print("User score:", user_score)
        print("Computer score:", computer_score)

    else:
        break
1