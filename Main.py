#imports
import pygame
import sys
from Sprite import Sprite

#set up pyGame
pygame.init()
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()

#set up the screen
screenW = 650
screenH = 850
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Player Test")

#setup player sprite
spriteList = pygame.sprite.Group()
player = Sprite("sprite/Disaster_Player.png", .5 * screenW - 40, .75 * screenH, 80, 80, 1)
spriteList.add(player)

while True:
    for event in pygame.event.get():
        # give player option to quit the game at any time
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

        # player input checks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # move up
                player.uSpeed = -player.speed
            if event.key == pygame.K_a:  # move left
                player.lSpeed = -player.speed
            if event.key == pygame.K_s:  # move down
                player.dSpeed = player.speed
            if event.key == pygame.K_d:  # move right
                player.rSpeed = player.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:  # move up
                player.uSpeed = 0
            if event.key == pygame.K_a:  # move left
                player.lSpeed = 0
            if event.key == pygame.K_s:  # move down
                player.dSpeed = 0
            if event.key == pygame.K_d:  # move right
                player.rSpeed = 0

    spritesToModify = spriteList.sprites()
    for sprite in spritesToModify:
        # update positions (using pixel-perfect movement)
        if sprite.rect.bottom < screenH and sprite.rect.top > 0 and sprite.rect.right < screenW and sprite.rect.left > 0:
            sprite.rect.centery += sprite.uSpeed + sprite.dSpeed
            sprite.rect.centerx += sprite.lSpeed + sprite.rSpeed

        # position adjustments
        while sprite.rect.bottom >= screenH:
            if sprite.destructable == True:  # if the obj is destructible and it hits a wall, get rid of it
                spriteList.remove(sprite)
            sprite.rect.y += -1
        while sprite.rect.top <= 0:
            if sprite.destructable == True:  # if the obj is destructible and it hits a wall, get rid of it
                spriteList.remove(sprite)
            sprite.rect.y += 1
        while sprite.rect.right >= screenW:
            if sprite.destructable == True:  # if the obj is destructible and it hits a wall, get rid of it
                spriteList.remove(sprite)
            sprite.rect.x += -1
        while sprite.rect.left <= 0:
            if sprite.destructable == True:  # if the obj is destructible and it hits a wall, get rid of it
                spriteList.remove(sprite)
            sprite.rect.x += 1

    # update screen
    spriteList.update()
    screen.fill((0, 0, 0))
    spriteList.draw(screen)

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)