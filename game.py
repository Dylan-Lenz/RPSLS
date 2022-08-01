from human import Human
from time import sleep
from ai import AI

class Game():

    def __init__(self):
        super().__init__
        self.player1 = ''
        self.player2 = ''

    def display_welcome(self):
        sleep(1)
        print('/nWelcome to Rock-Papers-Scissors-Lizard-Spock!!/n')
        print('Rules of the Game Are:')
        print('Rock Crushes Paper')
        print('Rock Crushes Scissors')
        print('Paper Covers Rock')
        print('Paper Disproves Spock')
        print('Scissors Cuts Paper')
        print('Scissors Decapitates Lizard')
        print('Lizard Poisons Spock')
        print('Lizard Eats Paper')
        print('Spock Smashes Scissors')
        print('Spock Vaporizes Rock/n')