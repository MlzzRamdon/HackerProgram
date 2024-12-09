import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flashlight Enemy Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

player = pygame.Rect(300, 250, 50, 50)

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.state = "warning"  # States: "warning", "searching", "circle", "complete" 
        self.warning_duration = 180  # 3 seconds at 60 fps
        self.warning_timer = 0
        self.x = 0
        self.y = 100
        self.speed = 5
        self.circle_passes = 0  # Fixed typo in variable name

        # Warning cone properties
        self.warning_width = 300
        self.warning_height = 400

    def draw_warning_cone(self):
        # Create a surface for the warning cone
        warning_surface = pygame.Surface((self.warning_height, self.warning_width), pygame.SRCALPHA)

        # Draw the warning cone with pulsing opacity
        pulse = math.sin(pygame.time.get_ticks() * 0.01) * 50 + 100
        warning_color = (255, 165, 0, int(pulse))

        pygame.draw.polygon(warning_surface, warning_color, [
            (0, self.warning_height // 2),
            (self.warning_width, 0),
            (self.warning_width, self.warning_height)
        ])

        # Blit the surface onto the screen
        self.screen.blit(warning_surface, (self.x, self.y))

    def draw_searching_cone(self):
        # Create a surface for the searching cone
        searching_surface = pygame.Surface((self.warning_width, self.warning_height), pygame.SRCALPHA)

        # Draw the searching cone
        pygame.draw.polygon(searching_surface, (255, 0, 0, 150), [
            (0, self.warning_height // 2),
            (self.warning_width, 0),
            (self.warning_width, self.warning_height)
        ])

        # Blit the surface onto the screen
        self.screen.blit(searching_surface, (self.x, self.y))

    def update(self, player):
        if self.state == "warning":
            # Increment warning timer
            self.warning_timer += 1

            # Move warning cone slowly
            self.x += 1

            # After warning duration
            if self.warning_timer >= self.warning_duration:
                self.state = "searching"
                self.warning_timer = 0
                self.x = 0

        elif self.state == "searching":
            # Move searching cone faster
            self.x += self.speed

            # Check if player is hidden
            if self.is_player_hidden(player):
                self.state = "circle"
                self.x = 0

            # If searching cone reaches end of screen
            if self.x > SCREEN_WIDTH:
                self.game_over()

        elif self.state == "circle":
            # Move circle across screen
            self.x += self.speed

            if self.x > SCREEN_WIDTH:
                self.circle_passes += 1
                self.x = 0

            if self.circle_passes >= 2:
                self.state = "complete"

    def is_player_hidden(self, player):
        # Placeholder for hiding logic
        return False

    def game_over(self):
        print("Game Over! You were caught!")
        pygame.quit()
        exit()

# Game setup
clock = pygame.time.Clock()
enemy = Enemy(screen)

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, player)

    # Update and draw enemy
    enemy.update(player)

    if enemy.state == "warning":
        enemy.draw_warning_cone()
    elif enemy.state == "searching":
        enemy.draw_searching_cone()
    elif enemy.state == "circle":
        enemy.draw_searching_cone()  # Placeholder for circle drawing

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()