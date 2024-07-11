import random
actions = ['rock', 'paper', 'scissors']
while True:
    player = input('Enter your choice (rock, paper or scissors): ')
    computer = random.choice(actions)
    print(f"Your choice {player}, computer choice {computer}\n")
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win! because Rock smashes scissors.")
        else:
            print("You lose :( Paper covers rock!")
    elif player == "paper":
        if computer == "rock":
            print("You win! because Paper covers rock.")
        else:
            print("You lose :( Scissors cuts paper!")
    elif player == "scissors":
        if computer == "paper":
            print("You win! because Scissors cuts paper.")
        else:
            print("You lose :( Rock smashes scissors!")

    play_again = input('Play again? (y/n)')
    if (play_again.lower() == 'n'):
        break
        random

