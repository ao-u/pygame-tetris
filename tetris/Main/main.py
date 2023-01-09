import pygame as game
import numpy as num
import random
from peice import Peice
from peice import Block
gamex = 700
gamey = 1000
game.init()
win = game.display.set_mode((gamex, gamey))
run = True
newpeice = True
scale = 50

#       0    1    2    3    4    5    6
#bag =["I", "J", "L", "O", "S", "T", "Z"]

currentPeice = Peice(0, 0, 0, 0, [])

deadBlocks = []

#rotation for I block
COLOR = (
    (161, 190, 228),
    (),
    (),

)
R =    (
    (
        #I, 0
        (-1, 0, 0, 0, 1, 0, 2, 0),
        (0, -1, 0, 0, 0, 1, 0, 2), 
        (-2, 0, -1, 0, 0, 0, 1, 0),
        (0, -2, 0, -1, 0, 0, 0, 1)
    ),
    (
        #J, 1
    )
)




def makeDeadPeice(peice):
    for i in range(4):
        deadBlocks.append(Block(peice.x + R[peice.tipe][peice.r][i * 2], peice.y + R[peice.tipe][peice.r][i * 2 + 1], COLOR[peice.tipe]))
    
def updateCurrentPeiceBlocks():
    for i in range(4):
        currentPeice.blocks[i] = Block(currentPeice.x + R[currentPeice.tipe][currentPeice.r][i * 2], currentPeice.y + R[currentPeice.tipe][currentPeice.r][i * 2 + 1], COLOR[currentPeice.tipe])

def currentPeiceColliding():
    for block in currentPeice.blocks:
        if block.y == 20:
            return True
        for blockk in deadBlocks:
            if (block.x == blockk.x and block.y == blockk.y):
                return True
    return False
    
def peiceOutOfBounds():
    for block in currentPeice.blocks:
        if block.x < 0 or block.x > 9:
            return True
    return False
        

while run:
    #check for quit
    for event in game.event.get():
        if event.type == game.QUIT:
            run = False
    #fill bg with nothing
    win.fill((0, 0, 0))
    #make grid
    for x in range(10):
        for y in range(20):
            game.draw.rect(win, (255, 255, 255), (x * scale, y * scale, scale, scale), 1)
    
      
    #try to move current peice down by 1, make it dead if it hits something
    currentPeice.y+=1
    updateCurrentPeiceBlocks()
    if currentPeiceColliding():
        currentPeice.y-=1
        updateCurrentPeiceBlocks()
        makeDeadPeice(currentPeice)
        newpeice = True
        
    #create new peice if needed
    if newpeice:
        currentPeice.x = 5
        currentPeice.y = 0
        currentPeice.r = 0
        currentPeice.tipe = 0
        updateCurrentPeiceBlocks()
        #makePeice(peices[-1])
        #random.choice(bag)
        newpeice = False
    
    
    
    #display current peice
    for i in range(4):
        game.draw.rect(win, currentPeice.blocks[i].c, (currentPeice.blocks[i].x * scale, currentPeice.blocks[i].y * scale, scale, scale))
    #display all dead peices
    for block in deadBlocks:
        game.draw.rect(win, block.c, (block.x * scale, block.y * scale, scale, scale))
        print(f"x: {block.x}, y: {block.y}, c: {block.c}")
    
    #input
    keys = game.key.get_pressed()
    if keys[game.K_UP]:
        currentPeice.r +=1
    if keys[game.K_DOWN]:
        currentPeice.r -=1
    if keys[game.K_a]:
        currentPeice.x-=1
        updateCurrentPeiceBlocks()
        if peiceOutOfBounds():
            currentPeice.x+=1
            updateCurrentPeiceBlocks()
    if keys[game.K_d]:
        currentPeice.x+=1
        updateCurrentPeiceBlocks()
        if peiceOutOfBounds():
            currentPeice.x-=1
            updateCurrentPeiceBlocks()
    currentPeice.r %=4

    game.display.update()
    game.time.delay(100)
    

    
game.quit()



