import pygame

class Player:
  def __init__(self,display):
    self.x = 0
    self.y = 0
    self.width = 10
    self.height = 10
    self.thickness = 0
    self.playerTile = pygame.Color(200, 200, 200) 
    self.display = display
    self.step = 2

  def draw(self):
    pygame.draw.rect(self.display, self.playerTile, (self.x,self.y,self.width,self.height), self.thickness)

  def updatePosition(self, direction):
    if direction == 'right':
      self.x += self.step
    if direction == 'left':
      self.x -= self.step 
    if direction == 'up':
      self.y -= self.step 
    if direction == 'down':
      self.y += self.step  

  # direction: string
  # return => a tuple
  def collisionPosition(self, direction):

    #           x+1,y-1 *    up      * x+width-1,y-1
    #                  ,............... 
    #        x-1,y+1 * |              | * x+width+1,y+1
    #                  |              | 
    #            left  |              |  right
    #                  |              | 
    # x-1,y+height-1 * |              | * x+width+1,y+height-1
    #                  |............../ 
    #     x+1,y+height+1 *     down   * x+width-1,y+height+1

    x = self.x
    y = self.y
    width = self.width
    height = self.height

    if direction == 'right':
      return (x+width+1,y+1,x+width+1,y+height-1)
    if direction == 'left':
      return (x-1,y+1,x-1,y+height-1)
    if direction == 'up':
      return (x+1,y-1,x+width-1,y-1)
    if direction == 'down':
      return (x+1,y+height+1,x+width-1,y+height+1)
