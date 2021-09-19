import pygame
import random
import math

# initialising the pygame

pygame.init()

# creating the screen

screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background0.2.jpg')

# Caption & Icon.
pygame.display.set_caption("xenos hunter")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player and starting position
playerImg = icon = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
# enemy speed
enemyX_change = 0.3
enemyY_change = 40

# bullet

# ready - Bullet can not be seen on screen.
# fire - bullet in movement
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# collision function is a edit of pythageros therom d=√((x_2-x_1)²+(y_2-y_1)²)

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop to stop window closing.
running = True
while running:

    # RGB - Red , Green , Blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether it's Right or Left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get the current x coordinate of the ship.
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    # checking player boundary
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 100
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    # enemy movement
    enemyX += enemyX_change

    # also enemy speed
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

playerX_change = 0
