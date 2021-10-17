from random import randint
import pygame
import sys

def main():
    size = width, height = 800, 600
    BG_COLOR = (0, 0, 0)
    exit = False
    logo = pygame.image.load('basketball.png')
    logo = pygame.transform.scale(logo, (100, 100))
    img_size = logo.get_rect().size
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    x = randint(50, width-100)
    y = randint(50, height-100)
    x_speed = 2.5
    y_speed = 2.5
    def move(x, y):
        screen.blit(logo, (x, y))
    while exit == False:
        screen.fill(BG_COLOR)
        if (x + img_size[0] >= width) or (x <= 0):
            x_speed = -x_speed
        if (y + img_size[1] >= height) or (y <= 0):
            y_speed = -y_speed
        x += x_speed
        y += y_speed
        move(x, y)
        pygame.display.flip()
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.VIDEORESIZE:
                size = width, height = event.w, event.h
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    sys.exit()
if __name__ == '__main__':
    main()
