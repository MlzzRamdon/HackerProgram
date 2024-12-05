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
input_lines = [] # User-written lines of "code"
current_line = ''  # Current line being typed
msg = '' # Message at the bottom of the screen

# Buttons
save_button = pygame.Rect(50, HEIGHT - 60, 140, 40)  # Save button
run_button = pygame.Rect(WIDTH - 190, HEIGHT - 60, 140, 40)  # Run button

# Function to save user input to a file
def save_code(lines, filename="user_code.txt"):
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
            # Check if Run button is clicked
            if run_button.collidepoint(event.pos):
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Submit the current line

                # Checks if this is the first line. If it is, we cannot check the previous line or we will get a list index error. It's not clean but it works.
                if len(input_lines) > 0:
                    # Checks is the previous line is a recognized command (more commands wil be added later)
                    if input_lines[len(input_lines) - 1] == "Print: ":
                        input_lines[len(input_lines) - 1] = "Print: " + current_line
                        current_line = ''
                        msg = ''
                    else:
                        # Checks for recognized commands (more commands wil be added later)
                        if current_line.lower() == "print":
                            input_lines.append("Print: ")
                            current_line = ''
                            msg = ''

                        # Displays an error message to the console if the current code meets neither requirement
                        else:
                            msg = "Unrecognized command."
                else:
                        # if there are no lines already in the console, we simply check whether or not this line is a valid command.
                        if current_line.lower() == "print":
                            input_lines.append("Print: ")
                            current_line = ''
                            msg = ''

                        # Displays an error message to the console if the current code meets neither requirement
                        else:
                            msg = "Unrecognized command."

            elif event.key == pygame.K_BACKSPACE:  # Backspace key
                if len(current_line) != 0: # Are there any characters to delete in the current line?
                    current_line = current_line[:-1]
                elif len(input_lines) > 0: # Is there a previous line?
                    input_lines.pop() # Delete that line
            else:  # Add typed character
                current_line += event.unicode

    # Draw everything
    screen.fill(BLACK)

    # Render previous lines
    y_offset = 50
    for line in input_lines[-14:]:  # Show last 14 lines
        line_surface = font.render(line, True, GREEN)
        screen.blit(line_surface, (50, y_offset))
        y_offset += 30
    line_surface = font.render(msg, True, RED)
    screen.blit(line_surface, (50, 500))

    # Render current line being typed
    current_line_surface = font.render(current_line, True, GREEN)
    screen.blit(current_line_surface, (50, y_offset))

    # Draw Save button
    pygame.draw.rect(screen, BUTTON_COLOR, save_button)  # Button background
    pygame.draw.rect(screen, BUTTON_BORDER, save_button, 2)  # Button border
    save_text = button_font.render("Save Code", True, TEXT_COLOR)
    screen.blit(save_text, (save_button.x + 15, save_button.y + 8))

    # Draw Run button
    pygame.draw.rect(screen, BUTTON_COLOR, run_button)  # Button background
    pygame.draw.rect(screen, BUTTON_BORDER, run_button, 2)  # Button border
    run_text = button_font.render("Run", True, TEXT_COLOR)
    screen.blit(run_text, (run_button.x + 45, run_button.y + 8))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.run()
