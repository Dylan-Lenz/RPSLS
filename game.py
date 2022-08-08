from human import Human
from time import sleep
from ai import AI

class Game():

    def __init__(self):
        super().__init__()
        self.game_over = False
        self.p1 = ''
        self.p2 = ''
 
    def run_game(self):
        self.display_welcome()
        self.set_player()
        self.set_round()
        self.set_game()
    
    def display_welcome(self):
        print('\n\n\nWelcome to Rock-Papers-Scissors-Lizard-Spock!!\n')
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
        user_input = input('\nSelect How Many Players? Press: 1, 2, or 3 to Spectate A Bot Match: ')
        sleep(1)
        if user_input == '1':
            self.p1 = Human(input('Please Enter Player Name: '))
            self.p1.gesture_choice()
            self.p2 = AI('Bot')
            self.p2.gesture_choice()
            sleep(2)
        elif user_input == '2':
            self.p1 = Human(input('Please Enter 1st Players Name: '))
            self.p2 = Human(input('Please Enter 2nd Players Name: '))
            sleep(2)
            self.p1.gesture_choice()
            self.p2.gesture_choice()
            sleep(2)
        elif user_input == '3':
            self.p1 = AI('Bot1')
            self.p1.gesture_choice()
            self.p2 = AI('Bot2')
            self.p2.gesture_choice()
            sleep(2)
        else:
            print('Invalid Entry: Please Try Again...')
            sleep(1)
        
    def set_round(self):
        if self.p1.set_gesture == '0' and self.p2.set_gesture == '2':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '0' and self.p2.set_gesture == '3':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '1' and self.p2.set_gesture == '0':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '1' and self.p2.set_gesture == '4':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '2' and self.p2.set_gesture == '1':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '2' and self.p2.set_gesture == '3':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '3' and self.p2.set_gesture == '1':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '3' and self.p2.set_gesture == '4':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1
        elif self.p1.set_gesture == '4' and self.p2.set_gesture == '0':
            print(f'\n{self.p1.name} Has Won the Round!\n')
            self.p1.score += 1   
        elif self.p1.set_gesture == '4' and self.p2.set_gesture == '2':
            print(f'\n{self.p1.name} Has Won the Round!\n')   
            self.p1.score += 1   
        elif self.p2.set_gesture == '0' and self.p1.set_gesture == '2':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '0' and self.p1.set_gesture == '3':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '1' and self.p1.set_gesture == '0':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '1' and self.p1.set_gesture == '4':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '2' and self.p1.set_gesture == '1':
            self.p2.score += 1
            print(f'\n{self.p2.name} Has Won the Round!\n')
        elif self.p2.set_gesture == '2' and self.p1.set_gesture == '3':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '3' and self.p1.set_gesture == '1':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '3' and self.p1.set_gesture == '4':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '4' and self.p1.set_gesture == '0':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == '4' and self.p1.set_gesture == '2':
            print(f'\n{self.p2.name} Has Won the Round!\n')
            self.p2.score += 1
        elif self.p2.set_gesture == self.p1.set_gesture:
            print(f'Round Tied, No Score, Try Again!\n')  

    def set_game(self):
        while self.game_over is False:
            if self.p1.score == 2:
               self.game_over = True
               print(f'{self.p1.name} Won the Game!')
               self.reset_game()
            elif self.p2.score == 2:
                self.game_over = True
                print(f'{self.p2.name} Won the Game!')
                self.reset_game()
            else:
               self.game_over = False
               self.p1.gesture_choice()
               self.p2.gesture_choice()
               self.set_round() 
    
    def reset_game(self):
        user_input = input('\nWould you like to Replay the Game? y/n :')
        if user_input == 'n':
            self.game_over = True
        elif user_input == 'y':
            self.game_over = False
            self.p1.score = 0
            self.p2.score = 0
            self.run_game()
        else:
            self.game_over is False
            print('Invalid Entry: Please Try Again.')
            self.run_game()