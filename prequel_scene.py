#Prequel animation

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 12 # frames per second setting
fpsClock = pygame.time.Clock()

# coordinates are stored in the top left
# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Anakin vs Obi-Wan')
bg = pygame.image.load('mustafar.png')

WHITE = (255, 255, 255)
PURPLE = (238, 184, 255)

platImg = pygame.image.load('platform1.png')
platX = 50
platY = 430

anakinImg = pygame.image.load('anakin1.png')
anX = 70
anY = 260
anakinPostJump = pygame.image.load('anakinPostJump.png')

obiImg = pygame.image.load('obiwan1.png')
obiX = 500
obiY = 200

fontObj = pygame.font.SysFont('trebuchetms', 32)
text1 = fontObj.render("It's over Anakin, I have the high ground", True, PURPLE, WHITE)
t1X = -50
t1Y = -50

text2 = fontObj.render("You underestimate my power", True, PURPLE, WHITE)
t2X = -50
t2Y = -50

text3 = fontObj.render("Don't try it", True, PURPLE, WHITE)
t3X = -50
t3Y = -50

text4 = fontObj.render("Lightsaber swooshes", True, PURPLE, WHITE)
t4X = -50
t4Y = -50

text5 = fontObj.render("You were the chosen one! It was said that", True, PURPLE, WHITE)
t5X = -500
t5Y = -500

text5_1 = fontObj.render("you would destroy the Sith, not join", True, PURPLE, WHITE)
t5_1X = -500
t5_1Y = -500

text5_2 = fontObj.render("them! Bring balance to the Force,", True, PURPLE, WHITE)
t5_2X = -500
t5_2Y = -500

text5_3 = fontObj.render("not leave it in darkness!", True, PURPLE, WHITE)
t5_3X = -500
t5_3Y = -500

text6 = fontObj.render("I HATE YOU!", True, PURPLE, WHITE)
t6X = -50
t6Y = -50

text7 = fontObj.render("You were my brother Anakin, I loved you", True, PURPLE, WHITE)
t7X = -50
t7Y = -50

sound1 = pygame.mixer.Sound('highground1.wav')
sound2 = pygame.mixer.Sound('mypower2.wav')
sound3 = pygame.mixer.Sound('tryit3.wav')
sound4 = pygame.mixer.Sound('triesit4.wav')
sound5 = pygame.mixer.Sound('chosenone5.wav')
sound6 = pygame.mixer.Sound('hateyou6.wav')
sound7 = pygame.mixer.Sound('brother7.wav')

scene = 'scene0'

jumping = [pygame.image.load('anJump1.png'), pygame.image.load('anJump2.png'), pygame.image.load('anJump3.png'), pygame.image.load('anJump4.png')]

vel = 15
isJump = False
right = False
PostJump = 0
jumpCount = 10
walkCount = 0

while True: 
    DISPLAYSURF.blit(bg, (0, 0))

    DISPLAYSURF.blit(platImg, (platX, platY))
    #DISPLAYSURF.blit(anakinImg, (anX, anY))
    DISPLAYSURF.blit(obiImg, (obiX, obiY))
    DISPLAYSURF.blit(text1, (t1X, t1Y))
    DISPLAYSURF.blit(text2, (t2X, t2Y))
    DISPLAYSURF.blit(text3, (t3X, t3Y))
    DISPLAYSURF.blit(text4, (t4X, t4Y))
    DISPLAYSURF.blit(text5, (t5X, t5Y))
    DISPLAYSURF.blit(text5_1, (t5_1X, t5_1Y))
    DISPLAYSURF.blit(text5_2, (t5_2X, t5_2Y))
    DISPLAYSURF.blit(text5_3, (t5_3X, t5_3Y))
    DISPLAYSURF.blit(text6, (t6X, t6Y))
    DISPLAYSURF.blit(text7, (t7X, t7Y))

    if isJump == False:
        if PostJump == 1:
            DISPLAYSURF.blit(anakinPostJump, (anX, anY))
        elif PostJump == 0:
            DISPLAYSURF.blit(anakinImg, (anX, anY))
    if walkCount + 1 >= 12:
        walkCount = 0
    if right:
        DISPLAYSURF.blit(jumping[walkCount//3], (anX, anY))
        walkCount += 1
    if isJump == True:
        anX += vel
        right = True
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            anY -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            right = False
            isJump = False
            jumpCount = 10
        
    if scene == 'scene0':
        t1X = 0
        t1Y = 0
        pygame.mixer.Sound.play(sound1)
        scene = 'scene1'
    if scene == 'scene1' and not pygame.mixer.get_busy(): #if no sound is playing
        t1X = -50
        t1Y = -50
        t2X = 0
        t2Y = 0
        pygame.mixer.Sound.play(sound2)
        scene = 'scene2'
    if scene == 'scene2' and not pygame.mixer.get_busy():
        t2X = -50
        t2Y = -50
        t3X = 0
        t3Y = 0
        pygame.mixer.Sound.play(sound3)
        scene = 'scene3'
    if scene == 'scene3' and not pygame.mixer.get_busy(): #jump scene
        t3X = -50
        t3Y = -50
        t4X = 0
        t4Y = 0
        isJump = True
        pygame.mixer.Sound.play(sound4)
        scene = 'scene4'
    if scene == 'scene4' and not pygame.mixer.get_busy():
        PostJump = 1
        t4X = -50
        t4Y = -50
        t5X = 0
        t5Y = 0
        t5_1X = 0
        t5_1Y = 38
        t5_2X = 0
        t5_2Y = 76
        t5_3X = 0
        t5_3Y = 114
        pygame.mixer.Sound.play(sound5)
        scene = 'scene5'
    if scene == 'scene5' and not pygame.mixer.get_busy():
        t5X = -500
        t5Y = -500
        t5_1X = -500
        t5_1Y = -500
        t5_2X = -500
        t5_2Y = -500
        t5_3X = -500
        t5_3Y = -500
        t6X = 0
        t6Y = 0
        pygame.mixer.Sound.play(sound6)
        scene = 'scene6'
    if scene == 'scene6' and not pygame.mixer.get_busy():
        t6X = -50
        t6Y = -50
        t7X = 0
        t7Y = 0
        pygame.mixer.Sound.play(sound7)
        scene = 'end'
    if scene == 'end' and not pygame.mixer.get_busy():
        t7X = -50
        t7Y = -50

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fpsClock.tick(FPS)
