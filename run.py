# https://github.com/Takeshidze/Prom/tree/game
import pygame
import sys

def main():
    exit = False
    size = width, height = 800, 600
    BG_COLOR = (0, 0, 0)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    paddle_w = 60
    paddle_h = 15
    paddle_speed = 10
    paddle = pygame.Rect(width // 2 - paddle_w // 2, height - paddle_h - 10, paddle_w, paddle_h)
    while exit == False:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, pygame.Color('darkorange'), paddle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.VIDEORESIZE:
                size = width, height = event.w, event.h
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and paddle.left > 0:
                paddle.left -= paddle_speed
            if key[pygame.K_d] and paddle.right < width:
                paddle.right += paddle_speed
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
