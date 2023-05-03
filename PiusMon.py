'''from tkinter import font'''
import pygame
import sys
import random
import json
from pygame.locals import *
import pygame.freetype
from fighters import Fighter
import fighters

class PiusMon:

    def __init__(self):
        self.sys = sys
        self.width = 900
        self.height = 650
        self.backgroundColor = (100, 150, 200)
        self.textColor = (255, 255, 255)
        self.fn = "fighters.json"

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

    def draw_fighterButton(self, x, y, width, height, screen, selected,list,key, text, font, text_color, outline=0, img = False,img_file='',img_w=10,img_h=10):
        button = pygame.Rect(x, y, width, height)
        if selected:
            if list[0] == key:
                button_color = (200, 0, 0)
            else:
                button_color = (255,165,0)
        else:
            button_color = (200, 210, 100)
        pygame.draw.rect(screen, (button_color), button, outline)
        self.draw_text(text, font, text_color, screen, x+10, y+10)
        if img:
            self.draw_image(screen,img_file,x,y,img_w,img_h)
        return button
    

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_image(self, screen, img_file,x,y,w,h):
        img = pygame.image.load(img_file).convert_alpha()
        img = pygame.transform.smoothscale(img, (w, h)) 
        screen.blit(img,(x,y))

    def select(self,selection,fighter_key,XX):
        if XX == True:
            if len(selection) <= 2:
                XX = False
                selection = selection.remove(fighter_key)
                print(selection)
                return (selection,XX)
            else:
                if len(selection) <= 2:
                    XX = True
                    selection = selection.append(fighter_key)
                    print(selection)
                    return (selection,XX)

    '''
    Screens
    '''

    def start_screen(self):

        screen = self.draw_screen('PiusMon',self.width,self.height)
        click = False
        running = True
        while running:
            

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)


            Splayer_button = self.draw_button(350, 400, 200, 50, screen, (200, 210, 100), 'Single Player', font, self.textColor)
            #Mplayer_button = self.draw_button(350, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            self.draw_image(screen,'Art/logo.png',300,20,300,300)
            self.draw_text('PiusMon', font, self.textColor, screen, 400, 200)
            # Button 1 collision
            if Splayer_button.collidepoint((mx, my)):
                if click:
                    self.singlePick_screen(screen)
            # if Mplayer_button.collidepoint((mx, my)):
            #     if click:
            #         self.multiPick_screen(screen)

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
        click = False
        running = True

        PB,PT,R,RS,SJ,SR = False,False,False,False,False,False
        selection = []

        paperBoy = Fighter('Paperboy','paper',40,20,20)
        paperToy = Fighter('paperToy','paper',12,12,12)

        rockson = Fighter('Rockson','rock',50,25,25)
        rocko_socko = Fighter('RockO SockO','rock',50,25,25)

        scissorFeet_john = Fighter('Scissorfeet John','scissors',50,25,25)
        scissorFeet_ron = Fighter('Scissorfeet Ron','scissors',50,25,25)
        
        
        with open(self.fn,"r") as f:
            inp = f.read()
            #print(inp)
            fighters = json.loads(inp)
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            
            
            
            #print(fighters['PB'])
            

            

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 50, 50, screen, (200, 0, 0), '<--', font, self.textColor)

            paperBoy_button = self.draw_fighterButton(200, 150, 120, 175, screen, PB,selection,'PB', (paperBoy.name).upper(), font, self.textColor,0,True,'Art/paperBoy_1.png',125,200)
            paperToy_button = self.draw_fighterButton(200, 350, 120, 175, screen, PT,selection,'PT', (paperToy.name).upper(), font, self.textColor,0,True,'Art/paperBoy_2.png',125,200)

            rockson_button = self.draw_fighterButton(350, 150, 120, 175, screen, R,selection,'R' ,(rockson.name).upper(), font, self.textColor,0,True,'Art/Rockson_1.png',125,200)
            rockoSocko_button = self.draw_fighterButton(350, 350, 120, 175, screen, RS,selection,'RS', (rocko_socko.name).upper(), font, self.textColor,0,True,'Art/Rockson_2.png',125,200)

            scissorFeetjohn_button = self.draw_fighterButton(500, 150, 120, 175, screen, SJ,selection, 'SJ', (scissorFeet_john.name).upper(), font, self.textColor,0,True,'Art/johnScissorfeet_1.png',125,200)
            scissorFeetron_button = self.draw_fighterButton(500, 350, 120, 175, screen, SR,selection,'SR', (scissorFeet_ron.name).upper(), font, self.textColor,0,True,'Art/johnSCissorfeet_2.png',125,200)

            
            ready_button = self.draw_button(350, 550, 200, 50, screen, (0,200,0), 'READY', font, self.textColor)


            if paperBoy_button.collidepoint((mx, my)):
                if click:
                    if PB == True: 
                        PB = False
                        selection.remove('PB')
                        print(selection)
                    else: 
                        if len(selection) < 2:  
                            PB = True
                            selection.append('PB')
                            print(selection)
            if paperToy_button.collidepoint((mx, my)):
                if click:
                    if PT == True:
                        PT = False
                        selection.remove('PT')
                        print(selection)
                    else:
                        if len(selection) < 2:
                            PT = True
                            selection.append('PT')
                            print(selection)
            if rockson_button.collidepoint((mx, my)):
                if click:
                    if R == True:
                        R = False
                        selection.remove('R')
                        print(selection)
                    else:
                        if len(selection) < 2:
                            R = True
                            selection.append('R')
                            print(selection)
            if rockoSocko_button.collidepoint((mx, my)):
                if click:
                    if RS == True:
                        RS = False
                        selection.remove('RS')
                        print(selection)
                    else:
                        if len(selection) < 2:
                            RS = True
                            selection.append('RS')
                            print(selection)
            if scissorFeetjohn_button.collidepoint((mx, my)):
                if click:
                    if SJ == True:
                        SJ = False
                        selection.remove('SJ')
                        print(selection)
                    else:
                        if len(selection) < 2:
                            SJ = True
                            selection.append('SJ')
                            print(selection)
            if scissorFeetron_button.collidepoint((mx, my)):
                if click:
                    if SR == True:
                        SR = False
                        selection.remove('SR')
                        print(selection)
                    else:
                        if len(selection) < 2:
                            SR = True
                            selection.append('SR')
                            print(selection)

            if Back_button.collidepoint((mx,my)):
                if click:
                    
                    running = False

            if ready_button.collidepoint((mx,my)):
                if click:
                    if len(selection) == 2:
                        self.Splayer_screen(screen,selection)


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


    def Splayer_screen(self,screen,selection):

        screen = self.draw_screen('Single player ',self.width,self.height)
        click = False
        running = True

        with open(self.fn,"r") as f:
            inp = f.read()
            #print(inp)
            fighters = json.loads(inp)

            fightingMon = selection[0]
            restingMon = selection[1]
            
            P_primeMon = Fighter(fighters[fightingMon]['name'],fighters[fightingMon]['type'],fighters[fightingMon]['speed'],fighters[fightingMon]['attack'],fighters[fightingMon]['life'])
            S_primeMon = Fighter(fighters[restingMon]['name'],fighters[restingMon]['type'],fighters[restingMon]['speed'],fighters[restingMon]['attack'],fighters[restingMon]['life'])
        
            print(P_primeMon.name)
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('Play', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 200, 50, screen, (200, 210, 100), '<--', font, self.textColor)


            self.draw_image(screen, fighters[fightingMon]['img_file'], 100, 250, 400, 400)
            self.draw_image(screen, fighters[restingMon]['img_file'], 25, 300, 200, 200)

            # if Mplayer_button.collidepoint((mx, my)):
            #     if click:
                    

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

    def multiPick_screen(self,screen):

        screen = self.draw_screen('Pick screen',self.width,self.height)
        click = False
        running = True
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 200, 50, screen, (200, 210, 100), '<--', font, self.textColor)


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