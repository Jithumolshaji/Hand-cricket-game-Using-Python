import random

def play_hand_cricket():
    player_score = 0
    computer_score = 0
    player_name = input("Enter your name: ")
    print(f"Welcome to Hand Cricket, {player_name}!")
    
# Player code ...........................................
    while True:
        player_choice = int(input("Choose a number  1 to 6: "))

        if player_choice < 1 or player_choice > 6:
            print("Invalid choice. Choose a number  1 to 6.")
            continue

        computer_choice = random.randint(1, 6)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print(f"{player_name}, you're out! Your final score: {player_score}")
            break
        else:
            player_score += player_choice
            print(f"Your current score: {player_score}")

# Computer code ................................................
    while True:
        computer_choice = random.randint(1, 6)
        player_choice = int(input("Choose a number  1 to 6: "))

        if player_choice < 1 or player_choice > 6:
            print("Invalid choice. Choose a number 1 to 6.")
            continue

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print(f"The computer is out! Computer's final score: {computer_score}")
            break
        else:
            computer_score += computer_choice
            print(f"Computer's current score: {computer_score}")

# the winner code.....................................................
    if player_score > computer_score:
        print(f"The winnner is {player_name}  score  {player_score}... Congratulations!")
    elif player_score < computer_score:
        print(f"The winner is {computer_score}!")
    else:
        print(f"It's a tie! Both {player_name} and the computer scored {player_score}!")

    print("Game Over!")

play_hand_cricket()