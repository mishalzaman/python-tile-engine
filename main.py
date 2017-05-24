import pygame
import configparser
from lib.Map import Map
from lib.Player import Player

pygame.init() # Start pygame 

# configuration
# Retrieve information from the game.ini file in conf directory
config = configparser.ConfigParser()
config.read('conf/game.ini')
print(config.get('Map','width'))

# pygame instances
display = pygame.display.set_mode((640,480))
pygame.display.set_caption('test')
clock = pygame.time.Clock()

# game instances
map = Map('map.json', display)
player = Player(display)

quitGame = False

while not quitGame:

    # end game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True

    # get player movement control
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
      if map.isCollision(player.collisionPosition('up')) == False:
        player.updatePosition('up')
    if pressed[pygame.K_s]:
      if map.isCollision(player.collisionPosition('down')) == False:
        player.updatePosition('down')
    if pressed[pygame.K_a]:
      if map.isCollision(player.collisionPosition('left')) == False:
        player.updatePosition('left')
    if pressed[pygame.K_d]:
      if map.isCollision(player.collisionPosition('right')) == False:
        player.updatePosition('right')

    map.draw()
    player.draw()

    pygame.display.update()
    clock.tick(60)
