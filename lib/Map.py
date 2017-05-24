import pygame
import json
import math

class Map:
  def __init__(self, filename, display):
    self.filename = filename                        # map filename
    self.display = display                          # pygame.display
    self.width = 10                                 # width of tile
    self.height = 10                                # height of tile
    self.thickness = 0                              # thickness (0 = fill)

    # Tiles
    self.groundTile = pygame.Color(255, 255, 255)   
    self.wallTile = pygame.Color(0, 0, 0)

    # Set map data from json file
    with open('map.json') as json_data:
      self.mapData = json.load(json_data)

  def draw(self):
    row = 0
    for j in self.mapData['map']:
      column = 0
      for i in j:
        x = column*self.width
        y = row*self.height
        colour = self.groundTile if i == 0 else self.wallTile
        pygame.draw.rect(self.display, colour, (x,y,self.width,self.height), self.thickness)
        column += 1
      row += 1

  # x: integer, x position
  # y: integer, y position
  def getTile(self,x,y):
    row = math.floor(y/10)
    column = math.floor(x/10)
    return self.mapData['map'][row][column]

  # position: tuple, is an x1,y1,x2,y2 value
  def isCollision(self,position):
    x1 = position[0]
    y1 = position[1]
    x2 = position[2]
    y2 = position[3]

    # map borders: right / left / bottom / top
    if x1 > self.width*self.mapData['columns'] or x1 < 0 or y1 > self.height*self.mapData['rows'] or y1 < 0:
      return True

    # if x2 > self.width*self.mapData['columns'] or x2 < 0 or y2 > self.height*self.mapData['rows'] or y2 < 0:
    #   return True

    print('-----')
    print('x1: ',x1, 'y1: ',y1)
    print('x2: ',x2, 'y2: ',y2)
    
    # map tile
    if self.getTile(x1,y1) == 1:
      return True

    if self.getTile(x2,y2) == 1:
      return True

    return False
  