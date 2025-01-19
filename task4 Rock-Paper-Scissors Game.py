import random

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
           (user_choice == 'scissors' and computer_choice == 'paper') or \
           (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        return 'computer'

    def play_round(self):
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        print("\n=======================================")
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round!")
            self.user_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        print("=======================================\n")

    def play_game(self):
        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            while play_again not in ['yes', 'no']:
                play_again = input("Invalid input. Please enter yes or no: ").lower()
            if play_again == 'no':
                break
        print("Thanks for playing!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
