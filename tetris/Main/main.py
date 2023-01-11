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
tick = 0

#       0I    1J    2L    3O    4S    5T    6Z
bag =[0, 1, 2, 3, 4, 5, 6]

currentPeice = Peice(0, 0, 0, 0, [])

deadBlocks = []

delayperkey = [0, 0, 0, 0]

delay = 150

ticks = 120


#colors for each peice
COLOR = (
    (161, 190, 228),
    (51, 76, 178),
    (216, 127, 51),
    (229, 229, 51),
    (127, 204, 25),
    (197, 66, 245),
    (200, 0, 0)
)
#rotation matrices for each peice
R =     (
    (
        #I, 0
        (-1, 0, 0, 0, 1, 0, 2, 0),
        (0, -1, 0, 0, 0, 1, 0, 2), 
        (-2, 0, -1, 0, 0, 0, 1, 0),
        (0, -2, 0, -1, 0, 0, 0, 1)
    ),
    (
        #J, 1
        (-1, -1, -1, 0, 0, 0, 1, 0),
        (1, -1, 0, -1, 0, 0, 0, 1),
        (1, 1, -1, 0, 0, 0, 1, 0),
        (-1, 1, 0, -1, 0, 0, 0, 1)
    ),
    (
        #L, 2
        (1, -1, -1, 0, 0, 0, 1, 0),
        (1, 1, 0, -1, 0, 0, 0, 1),
        (-1, 1, -1, 0, 0, 0, 1, 0),
        (-1, -1, 0, -1, 0, 0, 0, 1)
    ),
    (
        #O, 3
        (-1, 0, -1, -1, 0, -1, 0, 0),
        (-1, 0, -1, -1, 0, -1, 0, 0),
        (-1, 0, -1, -1, 0, -1, 0, 0),
        (-1, 0, -1, -1, 0, -1, 0, 0)
    ),
    (
        #S, 4
        (1, -1, -1, 0, 0, 0, 0, -1),
        (1, 1, 0, -1, 0, 0, 1, 0),
        (-1, 1, 0, 1, 0, 0, 1, 0),
        (-1, -1, -1, 0, 0, 0, 0, 1)
    ),
    (
        #T, 5
        (1, 0, -1, 0, 0, 0, 0, -1),
        (0, 1, 0, -1, 0, 0, 1, 0),
        (-1, 0, 0, 1, 0, 0, 1, 0),
        (0, -1, -1, 0, 0, 0, 0, 1)
    ),
    (
        #Z, 6
        (1, 0, -1, -1, 0, 0, 0, -1),
        (0, 1, 1, -1, 0, 0, 1, 0),
        (-1, 0, 0, 1, 0, 0, 1, 1),
        (0, -1, -1, 0, 0, 0, -1, 1)
    )
)




def makeDeadPeice(peice):
    for i in range(4):
        deadBlocks.append(currentPeice.blocks[i])
    
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

def makeGrid():
    for x in range(10):
        for y in range(20):
            game.draw.rect(win, (255, 255, 255), (x * scale, y * scale, scale, scale), 1)
            
def input(key):
    match key:
        case 'A':
            currentPeice.x-=1
            updateCurrentPeiceBlocks()
            if peiceOutOfBounds() or currentPeiceColliding():
                currentPeice.x+=1
        case 'D':
            currentPeice.x+=1
            updateCurrentPeiceBlocks()
            if peiceOutOfBounds() or currentPeiceColliding():
                currentPeice.x-=1
        case 'UP':
            currentPeice.r +=1
            currentPeice.r %=4
            updateCurrentPeiceBlocks()
            if peiceOutOfBounds() or currentPeiceColliding():
                currentPeice.r -=1
        case 'DOWN':
            currentPeice.r -=1
            currentPeice.r %=4
            updateCurrentPeiceBlocks()
            if peiceOutOfBounds() or currentPeiceColliding():
                currentPeice.r +=1
    updateCurrentPeiceBlocks()
        

while run:
    keyy = []
    #check for quit
    for event in game.event.get():
        if event.type == game.QUIT:
            run = False

    #input
    keys = game.key.get_pressed()
    if keys[game.K_UP] and delayperkey[0] <= tick:
        input('UP')
        delayperkey[0] = tick + delay
    if keys[game.K_a] and delayperkey[1] <= tick:
        input('A')
        delayperkey[1] = tick + delay
    if keys[game.K_d] and delayperkey[2] <= tick:
        input('D')
        delayperkey[2] = tick + delay
    if keys[game.K_DOWN] and delayperkey[3] <= tick:
        input('DOWN')
        delayperkey[3] = tick + delay
    
    tick+=1
    if tick % ticks == 0:
        
        #fill bg with nothing
        win.fill((0, 0, 0))
        #make grid
        makeGrid()
      
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
            
            bagchoice = random.choice(bag)
            bag.remove(bagchoice)
            currentPeice.tipe = bagchoice
            if len(bag) == 0:
                bag = [0, 1, 2, 3, 4, 5, 6]
            updateCurrentPeiceBlocks()
            #makePeice(peices[-1])
            #random.choice(bag)
            newpeice = False


        #clear lines
        lineClearer = [ [] for _ in range(20)]
        j = 0
        for block in deadBlocks:
            lineClearer[block.y].append(block.x)
        for i in range(len(lineClearer)):
            if sum(lineClearer[i]) == 45:
                while j != len(deadBlocks):
                    if deadBlocks[j].y == i:
                        deadBlocks.remove(deadBlocks[j])
                    else:
                        j+=1
                for blockk in deadBlocks:
                    if blockk.y < i:
                        blockk.y+=1


        
        
    
    
    
        #display current peice
        for i in range(4):
            game.draw.rect(win, currentPeice.blocks[i].c, (currentPeice.blocks[i].x * scale, currentPeice.blocks[i].y * scale, scale, scale))
        #display all dead peices
        for block in deadBlocks:
            game.draw.rect(win, block.c, (block.x * scale, block.y * scale, scale, scale))
            #print(f"x: {block.x}, y: {block.y}, c: {block.c}")
    
        #input
        
        
            
        
    

        game.display.update()
        #exec("print('hello')")
    game.time.delay(1)
game.quit()
