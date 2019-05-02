import pygame

from physics import *
from settings import *

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

def menu(screen, clock):
    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        return
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        font = "comicsans"
        screen.fill(BLUE)
        title=text_format("Space Create",font , 90, SILVER)
        if selected=="start":
            text_start=text_format("START", font, 75, WHITE)
        else:
            text_start = text_format("START", font, 75, BLACK)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, WHITE)
        else:
            text_quit = text_format("QUIT",font, 75, BLACK)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
