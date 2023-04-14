'''from tkinter import font'''
import pygame
import sys
import random
from pygame.locals import *
import pygame.freetype

class PiusMon:

    def __init__(self):
        self.sys = sys
        self.width = 900
        self.height = 650
        self.backgroundColor = (100, 150, 200)
        self.textColor = (255, 255, 255)

    '''
    Functions
    '''

    def draw_screen(self, caption,width,height):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        screen.fill(self.backgroundColor)
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
        return screen

    # draws button - does not handle collision
    def draw_button(self, x, y, width, height, screen, button_color, text, font, text_color, outline=0):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (button_color), button, outline)
        self.draw_text(text, font, text_color, screen, x+10, y+10)
        return button

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    '''
    Screens
    '''

    def start_screen(self):

        screen = self.draw_screen('PiusMon',self.width,self.height)

        running = True
        while running:
            click = False

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('PiusMon', font, self.textColor, screen, 250, 40)


            Splayer_button = self.draw_button(400, 400, 200, 50, screen, (200, 210, 100), 'Single Player', font, self.textColor)
            Mplayer_button = self.draw_button(400, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            # Button 1 collision
            if Splayer_button.collidepoint((mx, my)):
                if click:
                    self.singlePick_screen(screen)
            if Mplayer_button.collidepoint((mx, my)):
                if click:
                    self.multiPick_screen(screen)

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)

    def multiPick_screen(self,screen):

        screen = self.draw_screen('Pick screen',self.width,self.height)

        running = True
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)


            Splayer_button = self.draw_button(400, 400, 200, 50, screen, (200, 210, 100), 'Single Player', font, self.textColor)
            Mplayer_button = self.draw_button(400, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            # Button 1 collision
            if Splayer_button.collidepoint((mx, my)):
                if click:
                    self.Splayer_screen(screen)
            if Mplayer_button.collidepoint((mx, my)):
                if click:
                    self.registor_screen(screen)

            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)
    
    def singlePick_screen(self,screen):

        screen = self.draw_screen('Pick screen',self.width,self.height)

        running = True
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)


            Splayer_button = self.draw_button(400, 400, 200, 50, screen, (200, 210, 100), 'Single Player', font, self.textColor)
            Mplayer_button = self.draw_button(400, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            # Button 1 collision
            if Splayer_button.collidepoint((mx, my)):
                if click:
                    self.Splayer_screen(screen)
            if Mplayer_button.collidepoint((mx, my)):
                if click:
                    self.registor_screen(screen)

            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)

'''
Main
'''

def main():
    PM = PiusMon()
    pygame.init()

    global mainClock
    mainClock = pygame.time.Clock()

    PM.start_screen()


if __name__ == "__main__":
    main()