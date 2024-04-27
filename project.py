import pygame
from pygame import gfxdraw

x = 1600
y = 800

pygame.init()
window = pygame.display.set_mode((x,y))
black = (0, 0 ,0)
red = (255, 0, 0)


window.fill (black)
curr = (10, 10)
window.set_at(curr, red)
prev = (0, 0)

mainmenu = True
while mainmenu:
    game_close = False  

    pygame.draw.line(window, red, (0, 0), (0, 30))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.quit()
                pygame.quit()
            if event.key == pygame.K_a: #move it forward 10 spaces
                window.set_at(curr, black)
                prev = curr
                curr_list = list(curr)
                curr_list[0] += 20
                curr = tuple(curr_list)
                window.set_at(curr, red)