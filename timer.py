import pygame
pygame.init()

#variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#set time left  in seconds
time_left = 256
font = pygame.font.SysFont('Calibri', 50, True, True)


#SETUPSECTION__________________
#SCREEN SETUP
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PYGAME TEMPLET")
#CLOCK
clock = pygame.time.Clock()


def timer():
    #timer position on screen
    timer_x = screen_width / 6
    timer_y = screen_height / 6
    #get time passed
    elapsed_time = (pygame.time.get_ticks() - startTime) / 1000
    remaining_time = int(time_left - elapsed_time)
    minutes_left = remaining_time // 60
    seconds_left = remaining_time - minutes_left * 60
    #formating the time
    if seconds_left < 10 and minutes_left < 10:
        timer_text = font.render(f"0{minutes_left}:0{seconds_left}", True, (255, 255, 255))
    elif minutes_left < 10:
        timer_text = font.render(f"0{minutes_left}:{seconds_left}", True, (255, 255, 255))
    elif seconds_left < 10:
        timer_text = font.render(f"{minutes_left}:0{seconds_left}", True, (255, 255, 255))
    else:
        timer_text = font.render(f"{minutes_left}:{seconds_left}", True, (255, 255, 255))
    #display the time to the screen
    timer_rect = timer_text.get_rect(center=(timer_x, timer_y))
    screen.blit(timer_text, timer_rect)

#get start time
startTime = pygame.time.get_ticks()

#________________________________MAIN PROGRAM LOOP____________________
running = True
while running:
    #_____________MAIN EVENT LOOP_____________
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #1 - CLEAR SCREEN
    screen.fill(BLACK)
    #2 - DRAW DRAW DRAW DRAW DARW
    timer() 

    #3 - FLIP THE SCREEN / STAMP IT ON
    pygame.display.flip()

    #FPS
    clock.tick(60)


pygame.QUIT
