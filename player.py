from unicodedata import name


def Player(self):
    self.name = name
    self.score = 0
    self.gestures = []
    self.chosen_gesture = 'Rock'