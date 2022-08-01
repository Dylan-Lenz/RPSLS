from unicodedata import name


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = []
        self.chosen_gesture = 'Rock'