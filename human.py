from player import Player
from time import sleep

class Human(Player):
    
    def __init__(self, name):
        super().__init__(Player)
        self.score = 0
        self.name = name

    def gesture_choice(self):
        user_input = input(f'{self.name} Select What to Throw: Press: 0-Rock 1-Paper 2-Scissor 3-Lizard 4-Spock: ')
        self.gestures = ['Rock', 'Paper','Scissors', 'Lizard', 'Spock']
        self.set_gesture = user_input
        sleep(1)
        if user_input == '0':
            print(f'{self.name} has chosen {self.gestures[0]}.')
            sleep(1)
        elif user_input == '1':
            print(f'{self.name} has chosen {self.gestures[1]}.')
            sleep(1)
        elif user_input == '2':
            print(f'{self.name} has chosen {self.gestures[2]}.')
            sleep(1)
        elif user_input == '3':
            print(f'{self.name} has chosen {self.gestures[3]}.')
            sleep(1)
        elif user_input == '4':
            print(f'{self.name} has chosen {self.gestures[4]}.')
            sleep(1)
        else:
            print('Invalid Entry: Please Try Again\n')
            self.gesture_choice()