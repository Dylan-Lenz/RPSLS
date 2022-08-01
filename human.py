from player import Player
from time import sleep
import random

class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def gesture_choice(self):
        user_input = input('/nPlease make your selection: ')
        self.set_gesture = user_input
        gestures = ['Rock', 'Paper','Scissors', 'Lizard', 'Spock']
        sleep(1)
        print(f'{self.name} has chosen to throw {gestures[int(self.set_gesture)]} /n')