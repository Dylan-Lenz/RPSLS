from human import Human
from time import sleep
from ai import AI

class Game():

    def __init__(self):
        super().__init__
        self.player1 = ''
        self.player2 = ''

    def display_welcome(self):
        print('\nWelcome to Rock-Papers-Scissors-Lizard-Spock!!\n')
        sleep(1)
        print('Best of Three Rounds:')
        sleep(1)
        print('Rock Beats Lizard & Scissor')
        sleep(1)
        print('Paper Beats Rock & Spock')
        sleep(1)
        print('Scissors Beats Paper & Lizard')
        sleep(1)
        print('Lizard Beats Spock & Paper')
        sleep(1)
        print('Spock Beats Scissors & Rock\n')
        sleep(1)

    def set_player(self):
        user_input = input('\nSelect Players? Press: 1, 2, or 3 to Spectate: ')
        sleep(1)
        self.set_player = user_input
        if user_input == '1':
            return user_input
        elif user_input == '2':
            return user_input
        elif user_input == '3':
            return user_input
        else:
            print('Please Try Again...')