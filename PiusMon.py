'''from tkinter import font'''
import pygame
import sys
import random
import json
from pygame.locals import *
import pygame.freetype
from fighters import Fighter
import fighters
import time


'''TODO:

GamePlay:
- [X]when in battle a trainer may choose 2 thingsattack (may expand) or swap.
- [X]the monster with the fastest speed will hit first.
- []if you choose to swap and your monster is the fastest he may swap and not get hit
- []if you choose to swap and he is the slowest he will take the damage from the attack first.
- [X]trainers may only swap 3 times per battle
- [X]If a PiusMon is Knocked out he is instantly switched with the next PiusMon
- [X]If there are no other Piusmon left the other player is the winner
- []Sound

Animation:
- [X]normal state
- [X]attacking state
- [X]getting hit


    '''

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
        #pygame.display.update()
        return button

    def draw_fighterButton(self, x, y, width, height, screen, selected,list,key, text, font, text_color, outline=0, img = False,img_file='',img_w=10,img_h=10,flip = False):
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
            self.draw_image(screen,img_file,flip,x,y,img_w,img_h)
        return button
    

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_image(self, screen, img_file,flip,x,y,w,h):
        img = pygame.image.load(img_file).convert_alpha()
        img = pygame.transform.scale(img, (w, h)) 
        if flip == True:
            img = pygame.transform.flip(img, True, False)
        screen.blit(img,(x,y))
        
    def draw_card2(self,screen,x,y,w,h,PiusMon,flip,fighters_list,fighters_file,font,color,resting=False):

        self.draw_image(screen, fighters_file[PiusMon]['img_file'], flip, x, y, w, h)
        if resting == True:
            x= x-150
        self.draw_text(f"{fighters_file[PiusMon]['name']}",font,color,screen,x+150,y)
        self.draw_text(f"Life : {fighters_file[PiusMon]['life']}",font,color,screen,x+150,y+325)
        self.draw_text(f"speed : {fighters_file[PiusMon]['speed']}",font,color,screen,x+150,y+350)
        self.draw_text(f"attack : {fighters_file[PiusMon]['attack']}",font,color,screen,x+150,y+375)

    def draw_card(self,screen,x,y,w,h,PiusMon,PM,flip,fighters_list,fighters_file,frame,font,color,resting=False):

        self.draw_image(screen, fighters_file[PiusMon]['img_file'][frame], flip, x, y, w, h)
        if resting == True:
            x= x-150   
        self.draw_text(f"{fighters_file[PiusMon]['name']}",font,color,screen,x+150,y)
        self.draw_text(f"Life : {PM.life}",font,color,screen,x+150,y+325)
        self.draw_text(f"speed : {fighters_file[PiusMon]['speed']}",font,color,screen,x+150,y+350)
        self.draw_text(f"attack : {fighters_file[PiusMon]['attack']}",font,color,screen,x+150,y+375)

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


        logo_sprite = ["Art\Sprite sheets\Logo\planet-1.png.png",
        "Art\Sprite sheets\Logo\planet-2.png.png",
        "Art\Sprite sheets\Logo\planet-3.png.png",
        "Art\Sprite sheets\Logo\planet-4.png.png",
        "Art\Sprite sheets\Logo\planet-5.png.png",
        "Art\Sprite sheets\Logo\planet-6.png.png",]
        sprite_value = 0

        score = [0,0]

        while running:
            

            font = pygame.font.Font('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)



            sprite_value +=0.1
            logo = logo_sprite[int(sprite_value)]
            
            if sprite_value >= len(logo_sprite)-1:
                sprite_value = 0


            Splayer_button = self.draw_button(350, 400, 200, 50, screen, (200, 210, 100), 'Single Player', font, self.textColor)
            Mplayer_button = self.draw_button(350, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            self.draw_image(screen,logo,False,300,20,300,300)

            self.draw_text('PiusMon', font, self.textColor, screen, 400, 200)
            # Button 1 collision
            if Splayer_button.collidepoint((mx, my)):
                if click:
                    self.singlePick_screen(screen,score)
            if Mplayer_button.collidepoint((mx, my)):
                if click:
                    self.multiPick_screen(screen,score)

            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)

    
    def singlePick_screen(self,screen,score):

        screen = self.draw_screen('Pick screen',self.width,self.height)
        click = False
        running = True

        PB,PT,R,RS,SJ,SR = False,False,False,False,False,False
        selection = []

        paperBoy = Fighter('PB','Paperboy','paper',40,20,20)
        paperToy = Fighter('PT','paperToy','paper',12,12,12)

        rockson = Fighter('R','Rockson','rock',50,25,25)
        rocko_socko = Fighter('RS','RockO SockO','rock',50,25,25)

        scissorFeet_john = Fighter('SJ','Scissorfeet John','scissors',50,25,25)
        scissorFeet_ron = Fighter('SR','Scissorfeet Ron','scissors',50,25,25)
        
        
        with open(self.fn,"r") as f:
            inp = f.read()
            fighters = json.loads(inp)
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            
            

            

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 50, 50, screen, (200, 0, 0), '<--', font, self.textColor)

            paperBoy_button = self.draw_fighterButton(200, 150, 120, 175, screen, PB,selection,'PB', (paperBoy.name).upper(), font, self.textColor,0,True,'Art/paperBoy.png',125,200,False)
            paperToy_button = self.draw_fighterButton(200, 350, 120, 175, screen, PT,selection,'PT', (paperToy.name).upper(), font, self.textColor,0,True,'Art/paperToy.png',125,200,False)

            rockson_button = self.draw_fighterButton(350, 150, 120, 175, screen, R,selection,'R' ,(rockson.name).upper(), font, self.textColor,0,True,'Art/Rockson.png',125,200,False)
            rockoSocko_button = self.draw_fighterButton(350, 350, 120, 175, screen, RS,selection,'RS', (rocko_socko.name).upper(), font, self.textColor,0,True,'Art/RockoSocko.png',125,200,False)

            scissorFeetjohn_button = self.draw_fighterButton(500, 150, 120, 175, screen, SJ,selection, 'SJ', (scissorFeet_john.name).upper(), font, self.textColor,0,True,'Art/johnScissorfeet.png',125,200,False)
            scissorFeetron_button = self.draw_fighterButton(500, 350, 120, 175, screen, SR,selection,'SR', (scissorFeet_ron.name).upper(), font, self.textColor,0,True,'Art/ronScissorfeet.png',125,200,False)

            
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
                        self.Splayer_screen(screen,selection,score)


            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

    

            pygame.display.update()
            mainClock.tick(60)
        
    def multiPick_screen(self,screen,score):

        screen = self.draw_screen('Pick screen',self.width,self.height)
        click = False
        running = True

        P1_PB,P1_PT,P1_R,P1_RS,P1_SJ,P1_SR = False,False,False,False,False,False
        P1_selection = []
        

        P1_paperBoy = Fighter('PB','Paperboy','paper',40,20,20)
        P1_paperToy = Fighter('PT','paperToy','paper',12,12,12)

        P1_rockson = Fighter('R','Rockson','rock',50,25,25)
        P1_rocko_socko = Fighter('RS','RockO SockO','rock',50,25,25)

        P1_scissorFeet_john = Fighter('SJ','Scissorfeet John','scissors',50,25,25)
        P1_scissorFeet_ron = Fighter('SR','Scissorfeet Ron','scissors',50,25,25)

        P2_PB,P2_PT,P2_R,P2_RS,P2_SJ,P2_SR = False,False,False,False,False,False
        P2_selection = []

        P2_paperBoy = Fighter('PB','Paperboy','paper',40,20,20)
        P2_paperToy = Fighter('PT','paperToy','paper',12,12,12)

        P2_rockson = Fighter('R','Rockson','rock',50,25,25)
        P2_rocko_socko = Fighter('RS','RockO SockO','rock',50,25,25)

        P2_scissorFeet_john = Fighter('SJ','Scissorfeet John','scissors',50,25,25)
        P2_scissorFeet_ron = Fighter('SR','Scissorfeet Ron','scissors',50,25,25)
        
        
        with open(self.fn,"r") as f:
            inp = f.read()
            fighters = json.loads(inp)
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            
            

            

            screen.fill(self.backgroundColor)
            self.draw_text('Pick PiusMon', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 50, 50, screen, (200, 0, 0), '<--', font, self.textColor)

            P1_paperBoy_button = self.draw_fighterButton(100, 150, 80, 140, screen, P1_PB,P1_selection,'PB', (P1_paperBoy.key).upper(), font, self.textColor,0,True,'Art/paperBoy.png',85,125,False)
            P1_paperToy_button = self.draw_fighterButton(100, 300, 80, 140, screen, P1_PT,P1_selection,'PT', (P1_paperToy.key).upper(), font, self.textColor,0,True,'Art/paperToy.png',85,125,False)

            P1_rockson_button = self.draw_fighterButton(200, 150, 80, 140, screen, P1_R,P1_selection,'R' ,(P1_rockson.key).upper(), font, self.textColor,0,True,'Art/Rockson.png',85,125,False)
            P1_rockoSocko_button = self.draw_fighterButton(200, 300, 80, 140, screen, P1_RS,P1_selection,'RS', (P1_rocko_socko.key).upper(), font, self.textColor,0,True,'Art/RockoSocko.png',85,125,False)

            P1_scissorFeetjohn_button = self.draw_fighterButton(300, 150, 80, 140, screen,P1_SJ,P1_selection, 'SJ', (P1_scissorFeet_john.key).upper(), font, self.textColor,0,True,'Art/johnScissorfeet.png',85,125,False)
            P1_scissorFeetron_button = self.draw_fighterButton(300, 300, 80, 140, screen, P1_SR,P1_selection,'SR', (P1_scissorFeet_ron.key).upper(), font, self.textColor,0,True,'Art/ronScissorfeet.png',85,125,False)

            P2_paperBoy_button = self.draw_fighterButton(450, 150, 80, 140, screen, P2_PB,P2_selection,'PB', (P2_paperBoy.key).upper(), font, self.textColor,0,True,'Art/paperBoy.png',85,125,False)
            P2_paperToy_button = self.draw_fighterButton(450, 300, 80, 140, screen, P2_PT,P2_selection,'PT', (P2_paperToy.key).upper(), font, self.textColor,0,True,'Art/paperToy.png',85,125,False)
            P2_rockson_button = self.draw_fighterButton(550, 150, 80, 140, screen, P2_R,P2_selection,'R' ,(P2_rockson.key).upper(), font, self.textColor,0,True,'Art/Rockson.png',85,125,False)
            P2_rockoSocko_button = self.draw_fighterButton(550, 300, 80, 140, screen, P2_RS,P2_selection,'RS', (P2_rocko_socko.key).upper(), font, self.textColor,0,True,'Art/RockoSocko.png',85,125,False)
            P2_scissorFeetjohn_button = self.draw_fighterButton(650, 150, 80, 140, screen,P2_SJ,P2_selection, 'SJ', (P2_scissorFeet_john.key).upper(), font, self.textColor,0,True,'Art/johnScissorfeet.png',85,125,False)
            P2_scissorFeetron_button = self.draw_fighterButton(650, 300, 80, 140, screen, P2_SR,P2_selection,'SR', (P2_scissorFeet_ron.key).upper(), font, self.textColor,0,True,'Art/ronScissorfeet.png',85,125,False)

            
            ready_button = self.draw_button(350, 550, 200, 50, screen, (0,200,0), 'READY', font, self.textColor)


            if P1_paperBoy_button.collidepoint((mx, my)):
                if click:
                    if P1_PB == True: 
                        P1_PB = False
                        P1_selection.remove('PB')
                        print(P1_selection)
                    else: 
                        if len(P1_selection) < 2:  
                            P1_PB = True
                            P1_selection.append('PB')
                            print(P1_selection)
            if P1_paperToy_button.collidepoint((mx, my)):
                if click:
                    if P1_PT == True:
                        P1_PT = False
                        P1_selection.remove('PT')
                        print(P1_selection)
                    else:
                        if len(P1_selection) < 2:
                            P1_PT = True
                            P1_selection.append('PT')
                            print(P1_selection)
            if P1_rockson_button.collidepoint((mx, my)):
                if click:
                    if P1_R == True:
                        P1_R = False
                        P1_selection.remove('R')
                        print(P1_selection)
                    else:
                        if len(P1_selection) < 2:
                            P1_R = True
                            P1_selection.append('R')
                            print(P1_selection)
            if P1_rockoSocko_button.collidepoint((mx, my)):
                if click:
                    if P1_RS == True:
                        P1_RS = False
                        P1_selection.remove('RS')
                        print(P1_selection)
                    else:
                        if len(P1_selection) < 2:
                            P1_RS = True
                            P1_selection.append('RS')
                            print(P1_selection)
            if P1_scissorFeetjohn_button.collidepoint((mx, my)):
                if click:
                    if P1_SJ == True:
                        P1_SJ = False
                        P1_selection.remove('SJ')
                        print(P1_selection)
                    else:
                        if len(P1_selection) < 2:
                            P1_SJ = True
                            P1_selection.append('SJ')
                            print(P1_selection)
            if P1_scissorFeetron_button.collidepoint((mx, my)):
                if click:
                    if P1_SR == True:
                        P1_SR = False
                        P1_selection.remove('SR')
                        print(P1_selection)
                    else:
                        if len(P1_selection) < 2:
                            P1_SR = True
                            P1_selection.append('SR')
                            print(P1_selection)

            if P2_paperBoy_button.collidepoint((mx, my)):
                if click:
                    if P2_PB == True: 
                        P2_PB = False
                        P2_selection.remove('PB')
                        print(P2_selection)
                    else: 
                        if len(P2_selection) < 2:  
                            P2_PB = True
                            P2_selection.append('PB')
                            print(P2_selection)
            if P2_paperToy_button.collidepoint((mx, my)):
                if click:
                    if P2_PT == True:
                        P2_PT = False
                        P2_selection.remove('PT')
                        print(P2_selection)
                    else:
                        if len(P2_selection) < 2:
                            P2_PT = True
                            P2_selection.append('PT')
                            print(P2_selection)
            if P2_rockson_button.collidepoint((mx, my)):
                if click:
                    if P2_R == True:
                        P2_R = False
                        P2_selection.remove('R')
                        print(P2_selection)
                    else:
                        if len(P2_selection) < 2:
                            P2_R = True
                            P2_selection.append('R')
                            print(P2_selection)
            if P2_rockoSocko_button.collidepoint((mx, my)):
                if click:
                    if P2_RS == True:
                        P2_RS = False
                        P2_selection.remove('RS')
                        print(P2_selection)
                    else:
                        if len(P2_selection) < 2:
                            P2_RS = True
                            P2_selection.append('RS')
                            print(P2_selection)
            if P2_scissorFeetjohn_button.collidepoint((mx, my)):
                if click:
                    if P2_SJ == True:
                        P2_SJ = False
                        P2_selection.remove('SJ')
                        print(P2_selection)
                    else:
                        if len(P2_selection) < 2:
                            P2_SJ = True
                            P2_selection.append('SJ')
                            print(P2_selection)
            if P2_scissorFeetron_button.collidepoint((mx, my)):
                if click:
                    if P2_SR == True:
                        P2_SR = False
                        P2_selection.remove('SR')
                        print(P2_selection)
                    else:
                        if len(P2_selection) < 2:
                            P2_SR = True
                            P2_selection.append('SR')
                            print(P2_selection)

            if Back_button.collidepoint((mx,my)):
                if click:
                    
                    running = False

            if ready_button.collidepoint((mx,my)):
                if click:
                    if len(P1_selection) == 2:
                        self.Mplayer_screen(screen,P1_selection,score)


            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

    

            pygame.display.update()
            mainClock.tick(60)


    def Splayer_screen(self,screen,selection,score):

        screen = self.draw_screen('Single player ',self.width,self.height)
        click = False
        running = True
        turn = False


        PM = ["PB","PT","R","RS","SJ","SR"]
        choices = ['att','swap']

        
        

        with open(self.fn,"r") as f:
            inp = f.read()
            #print(inp)
            fighters = json.loads(inp)

            fightingMon = selection[0]
            restingMon = selection[1]

            enemy1 = random.choice(PM)
            PM.remove(enemy1)
            enemy2 = random.choice(PM)

            P_enemyMon = Fighter(enemy1,fighters[enemy1]['name'],fighters[enemy1]['type'],fighters[enemy1]['speed'],fighters[enemy1]['attack'],fighters[enemy1]['life'])
            S_enemyMon = Fighter(enemy2,fighters[enemy2]['name'],fighters[enemy2]['type'],fighters[enemy2]['speed'],fighters[enemy2]['attack'],fighters[enemy2]['life'])
            
            P_playerMon = Fighter(fightingMon,fighters[fightingMon]['name'],fighters[fightingMon]['type'],fighters[fightingMon]['speed'],fighters[fightingMon]['attack'],fighters[fightingMon]['life'])
            S_playerMon = Fighter(restingMon,fighters[restingMon]['name'],fighters[restingMon]['type'],fighters[restingMon]['speed'],fighters[restingMon]['attack'],fighters[restingMon]['life'])
            effect_txt = P_playerMon.something(P_playerMon,P_enemyMon)

        check1 = False
        check2 = False
        check3 = False

        P_swaps = 3
        E_swaps = 3

        PPMon_ani = 0
        PSMon_ani = 0
        EPMon_ani = 0
        ESMon_ani = 0
        
        
        if P_playerMon.speed > P_enemyMon.speed:
            turn = True
        while running:

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)
            self.draw_text('Play', font, self.textColor, screen, 250, 40)
            Back_button = self.draw_button(10, 10, 50, 50, screen, (200, 0, 0), '<--', font, self.textColor)

            self.draw_text(f"Player Swaps:{P_swaps}", font, self.textColor, screen, 20, 200)
            self.draw_text(f"Enemy Swaps:{E_swaps}", font, self.textColor, screen, 725, 200)
            # if check1 == False:
            #     if P_playerMon.life > 0: # if the player is still alive
            #         self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters, font, self.textColor)
            #     else:
            #         if P_playerMon.life  and S_playerMon.life < 0: #check if they are both dead
            #             running = False
            #         check1 = True
            #         fightingMon,restingMon = restingMon,fightingMon

            if P_playerMon.life<= 0 and S_playerMon.life <=0:
                    winer = "ENEMY"
                    score[1]+=1
                    self.win_screen(winer,score)

            if P_enemyMon.life<= 0 and S_enemyMon.life <= 0:
                winer = "PLAYER"
                score[0]+=1
                self.win_screen(winer,score)

            if P_playerMon.life > 0: # if the player is still alive
                PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
            else:
                if check1 == False:
                    print('player died')
                    fightingMon,restingMon = restingMon,fightingMon
                    P_playerMon,S_playerMon = S_playerMon,P_playerMon
                    check2 = True
                    check1 =True

         
            
            if check2 ==False:
                if S_playerMon.life > 0:
                    PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

         

            
            if P_enemyMon.life > 0:
                EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
            else:            
                if check3 == False:
                    print("enemy died")
                    enemy1,enemy2 = enemy2,enemy2
                    P_enemyMon,S_enemyMon = S_enemyMon,P_enemyMon
                    check3 = True
            
            if check3 == False:
                if S_enemyMon.life > 0:
                    ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)

            
 
            if P_playerMon.life > 0 and S_playerMon.life > 0:
                if P_swaps > 0:
                    swap_Button = self.draw_button(400, 500, 100, 50, screen, (0,200,0), 'swap', font, self.textColor)
            

            attack_Button = self.draw_button(400, 425, 100, 50, screen, (0,200,0), 'attack', font, self.textColor)

          # for images just make the json file have a list of images and by defult the first one is restingi and if its attack then just change the json imaage o t the next one

            #make it so within each attack thing where it changes the animation you draw another card
            

            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if Back_button.collidepoint((mx,my)):
                    if click:
                        running = False
                if swap_Button.collidepoint((mx,my)):
                    if click:
                        if turn:
                
                            effect_txt = "PLAYER SWAPS"
                            fightingMon,restingMon = restingMon,fightingMon
                            P_playerMon,S_playerMon = S_playerMon,P_playerMon
                            print(effect_txt)
                            turn = False
                            P_swaps -= 1
                            self.draw_button(350, 200, 200, 50, screen, (200,0,0), effect_txt, font, self.textColor)
                            PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                            PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

                            pygame.display.update()
                            time.sleep(2)
                            
                        #fightingMon.swap()
                if attack_Button.collidepoint((mx,my)):
                    if click:
                        if turn:
                            
                            if fightingMon == P_playerMon.key:
                                if enemy1 == P_enemyMon.key:
                                    P_playerMon.Attack(P_playerMon,P_enemyMon)
                                    PPMon_ani = 1
                                    EPMon_ani = 2
                                    PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                                    EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)

                                    effect_txt = "PLAYER ATTACKS"
                                    turn = False

                                else:
                                    P_playerMon.Attack(P_playerMon,S_enemyMon)
                                    PPMon_ani = 1
                                    ESMon_ani = 2
                                    PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                                    ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)

                                    effect_txt = "PLAYER ATTACKS"
                                    turn = False
                            else:
                                if enemy1 == P_enemyMon.key:
                                    S_playerMon.Attack(S_playerMon,P_enemyMon)
                                    PSMon_ani = 1
                                    EPMon_ani = 2

                                    EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
                                    PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

                                    effect_txt = "PLAYER ATTACKS"
                                    turn = False
                                else:
                                    S_playerMon.Attack(S_playerMon,S_enemyMon)
                                    PSMon_ani = 1
                                    ESMon_ani = 2

                                    ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)
                                    PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

                                    effect_txt = "PLAYER ATTACKS"
                                    turn = False
                            effect_txt = "PLAYER ATTACKS"
                            self.draw_button(350, 200, 200, 50, screen, (200,0,0), effect_txt, font, self.textColor)
                            pygame.display.update()
                            time.sleep(2)
                            PPMon_ani = 0
                            PSMon_ani = 0
                            EPMon_ani = 0
                            ESMon_ani = 0
                            
                            ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)
                            PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)
                            PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                            EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
                            pygame.display.update()



            
    
            if turn == False:
                
                #pygame.display.update()
                #.delay(2000)
                if P_enemyMon.life and S_enemyMon.life<0:
                    if E_swaps > 0:
                        move = random.choice(choices)
                    else:
                        move = 'att'
                else:
                    move = 'att'

                if move == 'att':
                    if enemy1 == P_enemyMon.key:
                        if fightingMon == P_playerMon.key:
                            effect_txt = "ENEMY ATTACKS"
                            P_enemyMon.Attack(P_enemyMon,P_playerMon)
                            PPMon_ani = 2
                            EPMon_ani = 1
                            PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                            EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)

                            print('enemt attacks')
                            turn = True
                        else:
                            effect_txt = "ENEMY ATTACKS"
                            P_enemyMon.Attack(P_enemyMon,S_playerMon)
                            PSMon_ani = 2
                            EPMon_ani = 1
                            EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
                            PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

                            turn = True
                    else:
                        if enemy1 == P_enemyMon.key:
                            effect_txt = "ENEMY ATTACKS"
                            S_enemyMon.Attack(S_enemyMon,P_playerMon)
                            PPMon_ani = 2
                            ESMon_ani = 1
                            PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                            ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)

                            turn = True
                        else:
                            effect_txt = "ENEMY ATTACKS"
                            S_enemyMon.Attack(S_enemyMon,S_playerMon)
                            PSMon_ani = 2
                            ESMon_ani = 1

                            ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)
                            PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)

                            turn = True
                    effect_txt = "ENEMY ATTACKS"
                    self.draw_button(350, 200, 200, 50, screen, (200,0,0), effect_txt, font, self.textColor)
                    pygame.display.update()
                    time.sleep(2)
                    PPMon_ani = 0
                    PSMon_ani = 0
                    EPMon_ani = 0
                    ESMon_ani = 0
                    
                    ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)
                    EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
                    PSMon = self.draw_card(screen, 25, 250, 200, 200, restingMon,S_playerMon, False, PM, fighters,PSMon_ani, font, self.textColor,True)
                    PPmon = self.draw_card(screen, 100, 200, 400, 400, fightingMon,P_playerMon, False, PM, fighters,PPMon_ani, font, (self.textColor))
                    pygame.display.update()

                            
                if move == 'swap':
        
                    effect_txt = "ENEMY SWAPS"
                    self.draw_button(350, 200, 200, 50, screen, (200,0,0), effect_txt, font, self.textColor)
                    enemy1,enemy2 = enemy2,enemy1
                    P_enemyMon,S_enemyMon = S_enemyMon,P_enemyMon
                    print('enemy swap')
                    E_swaps -=1
                    ESMon = self.draw_card(screen, 700, 250, 200, 200, enemy2,S_enemyMon, True, PM, fighters,ESMon_ani, font, self.textColor,True)
                    EPMon = self.draw_card(screen, 400, 200, 400, 400, enemy1,P_enemyMon, True, PM, fighters,EPMon_ani, font, self.textColor)
   
                    turn = True

                    pygame.display.update()
                    time.sleep(2)
                    
                if P_playerMon.life<= 0 and S_playerMon.life <=0:
                    winer = "ENEMY"
                    score[1]+=1
                    self.win_screen(winer,score)

                if P_enemyMon.life<= 0 and S_enemyMon.life <= 0:
                    winer = "PLAYER"
                    score[0]+=1
                    self.win_screen(winer,score)

                
                
                turn = True

            bar_txt = f"{fighters[fightingMon]['type']} vs {fighters[enemy1]['type']}"
            action_bar = self.draw_button(300, 75, 200, 25, screen, (0,23,200), bar_txt, font, self.textColor)
            #effect_bar = self.draw_button(300, 120, 200, 25, screen, (0,23,200), effect_txt, font, self.textColor)

            
            
            

            pygame.display.update()
            mainClock.tick(60)

    def Mplayer_screen(self,screen):  



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
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)


    def win_screen(self,winer,score):

        screen = self.draw_screen('PiusMon',self.width,self.height)
        click = False
        running = True


        logo_sprite = ["Art\Sprite sheets\Logo\planet-1.png.png",
        "Art\Sprite sheets\Logo\planet-2.png.png",
        "Art\Sprite sheets\Logo\planet-3.png.png",
        "Art\Sprite sheets\Logo\planet-4.png.png",
        "Art\Sprite sheets\Logo\planet-5.png.png",
        "Art\Sprite sheets\Logo\planet-6.png.png",]
        sprite_value = 0



        while running:
            

            font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
            mx, my = pygame.mouse.get_pos()

            screen.fill(self.backgroundColor)



            sprite_value +=0.1
            logo = logo_sprite[int(sprite_value)]
            if sprite_value >= len(logo_sprite)-1:
                sprite_value = 0
            self.draw_image(screen,logo,False,300,20,300,300)

            self.draw_text(f'{winer} won!', font, self.textColor, screen, 400, 200)
            self.draw_text("Score", font, self.textColor, screen, 400, 300)
            self.draw_text(f"{score[0]}:{score[1]}", font, self.textColor, screen, 400, 350)

            playAgain_button = self.draw_button(250, 400, 200, 50, screen, (200, 210, 100), 'PLAY AGAIN', font, self.textColor)
            #Mplayer_button = self.draw_button(350, 500, 200, 50, screen, (200, 210, 100), 'Multiplayer', font, self.textColor)

            menu_button = self.draw_button(500, 400, 200, 50, screen, (200,210,100), "MAIN MENU", font, self.textColor)


            # Button 1 collision
            if playAgain_button.collidepoint((mx, my)):
                if click:
                    self.singlePick_screen(screen,score)
            if menu_button.collidepoint((mx, my)):
                if click:
                    self.start_screen()
            

            # Events
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
    #PM.win_screen()


if __name__ == "__main__":
    main()