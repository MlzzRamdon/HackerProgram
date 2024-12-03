import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hacker Coding Terminal")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BUTTON_COLOR = (200, 200, 200)  # Light gray for buttons
BUTTON_BORDER = (50, 50, 50)  # Dark gray for button borders
TEXT_COLOR = BLACK

# Font
font = pygame.font.Font(None, 32)
button_font = pygame.font.Font(None, 28)

# Terminal variables
input_lines = []  # User-written lines of "code"
current_line = ''  # Current line being typed

# Buttons
save_button = pygame.Rect(50, HEIGHT - 60, 140, 40)  # Save button
exit_button = pygame.Rect(WIDTH - 190, HEIGHT - 60, 140, 40)  # Exit button

# Function to save user input to a file
def save_code(lines, filename="user_code.py"):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if Save button is clicked
            if save_button.collidepoint(event.pos):
                save_code(input_lines)
                input_lines.append("# Code saved successfully!")
            # Check if Exit button is clicked
            if exit_button.collidepoint(event.pos):
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Submit the current line
                input_lines.append(current_line)  # Add to code lines
                current_line = ''  # Reset current line
            elif event.key == pygame.K_BACKSPACE:  # Backspace key
                current_line = current_line[:-1]
            else:  # Add typed character
                current_line += event.unicode

    # Draw everything
    screen.fill(BLACK)

    # Render previous lines
    y_offset = 50
    for line in input_lines[-20:]:  # Show last 20 lines
        line_surface = font.render(line, True, GREEN)
        screen.blit(line_surface, (50, y_offset))
        y_offset += 30

    # Render current line being typed
    current_line_surface = font.render(current_line, True, GREEN)
    screen.blit(current_line_surface, (50, y_offset))

    # Draw Save button
    pygame.draw.rect(screen, BUTTON_COLOR, save_button)  # Button background
    pygame.draw.rect(screen, BUTTON_BORDER, save_button, 2)  # Button border
    save_text = button_font.render("Save Code", True, TEXT_COLOR)
    screen.blit(save_text, (save_button.x + 15, save_button.y + 8))

    # Draw Exit button
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)  # Button background
    pygame.draw.rect(screen, BUTTON_BORDER, exit_button, 2)  # Button border
    exit_text = button_font.render("Exit", True, TEXT_COLOR)
    screen.blit(exit_text, (exit_button.x + 45, exit_button.y + 8))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
