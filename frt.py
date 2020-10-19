import pygame
from pygame.locals import *
import random
import math
from pygame import mixer


pygame.init()

# Colores
BLACK = (0, 0, 0)



pygame.display.set_caption("Space Invader")
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# BALAS


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(BULLET_IMG, (x + 16, y + 10))
    
    pygame.display.update()

BULLET_IMG = pygame.image.load('bullets.png')
BULLET_X = 0
BULLET_Y = 480
BULLET_X_CHANGE = 0
BULLET_Y_CHANGE = 8
bullet_state = "ready"


# Fondo

background = pygame.image.load('background.png')



#EMEEMIGOS
ENEMY_IMG = []
ENEMY_Y = []
ENEMY_X =  []
ENEMY_X_CHANGE = []
ENEMY_Y_CHANGE = []
N_OF_ENEMIES = 10 

# Enemigos

for i in range(N_OF_ENEMIES):
    ENEMY_IMG.append(pygame.image.load('ufo32.png'))
    ENEMY_Y.append(random.randint(10, 150)) 
    ENEMY_X.append(random.randint(0, 735))
    ENEMY_X_CHANGE.append(4)
    ENEMY_Y_CHANGE.append(40)


#Colision

def isCollision(ENEMY_X,ENEMY_Y, BULLET_X, BULLET_Y):
    distance = math.sqrt(math.pow(ENEMY_X - BULLET_X, 2) + (math.pow(ENEMY_Y- BULLET_Y, 2)))
    if distance < 27:
        return True
    else:
        return False


# Jugador

PLAYER_IMG = pygame.image.load('spaceship.png')
PLAYER_Y = 450
PLAYER_X = 400
PLAYER_X_CHANGE = 0


score = 0

def Player(x, y):
    screen.blit(PLAYER_IMG, (x, y))
    pygame.display.update()

reloj = pygame.time.Clock()


# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)


def enemy(x, y, i):
    screen.blit(ENEMY_IMG[i], (x, y))

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Ciclo juego
RUNNING = True
while RUNNING:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        screen.fill(BLACK)
        pygame.display.update()

        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 5
                

            if event.key == pygame.K_SPACE and bullet_state =="ready":
                BULLET_X = PLAYER_X
                fire_bullet(PLAYER_X,BULLET_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 0

    # Movimiento

    
    if PLAYER_X <= 0:
        PLAYER_X = 0

    elif PLAYER_X >= 736:
        PLAYER_X = 736


    for i in range(N_OF_ENEMIES):
        
        # Game Over
        if ENEMY_Y[i] > 440:
            for j in range(N_OF_ENEMIES):
                ENEMY_Y[j] = 2000
            game_over_text()
            break

        ENEMY_X[i] += ENEMY_X_CHANGE[i]
        if ENEMY_X[i] >= 738:
            ENEMY_X_CHANGE[i] = -2
            ENEMY_Y[i] += ENEMY_Y_CHANGE[i]

        elif ENEMY_X[i] <= 0:
            ENEMY_X_CHANGE[i] = 2
            ENEMY_Y[i] += ENEMY_Y_CHANGE[i]


        #Colision 
        colision = isCollision(ENEMY_X[i],ENEMY_Y[i],BULLET_X,BULLET_Y)
        if colision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            BULLET_Y = 480
            bullet_state = "ready"
            score_value += 1

            ENEMY_X[i] = random.randint(0, 736)
            ENEMY_Y[i] = random.randint(50, 150)

            print(score_value)

        enemy(ENEMY_X[i], ENEMY_Y[i], i)



    if bullet_state == "fired":
        fire_bullet(BULLET_X,BULLET_Y)
        BULLET_Y -= BULLET_Y_CHANGE

    if BULLET_Y <= 0:
        BULLET_Y = 480
        bullet_state = "ready"

    
    


    

    PLAYER_X += PLAYER_X_CHANGE
    show_score(textX, testY)

    Player(PLAYER_X, PLAYER_Y)

    
