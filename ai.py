from player import Player
from time import sleep
import random

class AI(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def gesture_choice(self):
        self.set_gesture = str(random.randint(0,4))
        gestures = ['Rock', 'Paper','Scissors', 'Lizard', 'Spock']
        sleep(1)
        print(f'{self.name} has chosen to throw {gestures[int(self.set_gesture)]}')