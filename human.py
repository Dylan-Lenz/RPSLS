from player import Player
from time import sleep
import random

class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name