import random


class RSP:
    def __init__(self, choice):
        self.choice = choice.lower()

    def game(self):
        computerChoices = ['Rock', 'Paper', 'Scissors']
        computerChoice = random.choice(computerChoices).lower()
        if self.choice == 'rock' and computerChoice == 'rock':
            print(f'It\'s a draw!, Computer chose {computerChoice}.')
        elif self.choice == 'paper' and computerChoice == 'rock':
            print(f'You WIN!, Computer chose {computerChoice}.')
        elif self.choice == 'scissors' and computerChoice == 'rock':
            print(f'You Lose!, Computer chose {computerChoice}.')
        if self.choice == 'rock' and computerChoice == 'paper':
            print(f'You Lose!, Computer chose {computerChoice}.')
        elif self.choice == 'paper' and computerChoice == 'paper':
            print(f'It\'s a draw!, Computer chose {computerChoice}.')
        elif self.choice == 'scissors' and computerChoice == 'paper':
            print(f'You WIN!, Computer chose {computerChoice}.')
        if self.choice == 'rock' and computerChoice == 'scissors':
            print(f'You Win!, Computer chose {computerChoice}.')
        elif self.choice == 'paper' and computerChoice == 'scissors':
            print(f'You Lose!, Computer chose {computerChoice}.')
        elif self.choice == 'scissors' and computerChoice == 'scissors':
            print(f'It\'s a draw!, Computer chose {computerChoice}.')
        else:
            print("Something seems to be wrong?")


player1 = RSP(input("Rock, Paper or Scissors: "))
player1.game()
