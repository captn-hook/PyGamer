from sprite import Sprite

class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Box.png", startx, starty)
