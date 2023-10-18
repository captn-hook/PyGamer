from sprite import Sprite

class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Player.png", startx, starty)
        
