import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Flashlight Enemy Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

player = pygame.Rect((300, 250, 50, 50))


class Enemy:
    def __init__(self,screen):
        self.screen = screen
        self.state = "warning" # States: "warning", "searching", "circle", "complete" 
        self.warning_duration = 180 # 3 seconds at 60 fps
        self.warning_timer = 0
        self.x = 0
        self.y = 100
        self.speed = 5
        self.cirtcle_passes = 0

        # Warning code properties
        self.warning_width = 300
        self.warning_height = 400


def drawing_warning_cone(self):
    # Create a surface for the warning cone
    warning_surface = pygame.Surface((self.warning_width, self.warning_height), pygame.SRCALPHA)

    # Draw the warning cone with pulsing opacity
    pulse = math.sin(pygame.time.get_ticks() * 0.01) * 50 + 100
    warning_color = (255, 165, 0, int(pulse))

    pygame.draw.polygon(warning_surface, warning_color, [
        (0, self.warning height),
        (self.warning_height),
        (self.warning_width // 2, 0),
        (self.warning_width, self.warning_height)
    ])


def update(self, player):
    if self.state == "warning":
        # Increment warning timer
        self.warning_timer += 1

        # Move warning code slowly
        self.x += 1

        # After warning duration
        if self.warning_timer >= self.warning_dration:
            self.state = "searching"
            self.warning_timer = 0
            self.x = 0

        elif self.state == "searching":
            # Move searching cone faster
            self.x += self.speed

            # check if player is hidden
            if self.is_player_hidden(player):
                self.state = "circle"
                self.x = 0


run = True
while run:

    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False

pygame.quit()
