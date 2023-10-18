import pygame
from player import Player
from box import Box

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player1 = Player(100, 200)

    boxes = pygame.sprite.Group()
    for bx in range(0,400,70):
        boxes.add(Box(bx,300))

    while True:
        pygame.event.pump()
        player1.update()

        # Draw loop
        screen.fill(BACKGROUND)
        player1.draw(screen)
        boxes.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()

