import pygame as game
import numpy as num
import random
from peice import Peice
from peice import Block
gamex = 500
gamey = 500
game.init()
win = game.display.set_mode((gamex, gamey))
run = True
newpeice = True
scale = 20

#       0    1    2    3    4    5    6
#bag =["I", "J", "L", "O", "S", "T", "Z"]

peices = []

blocks = []



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

def displayBlock(block):
    game.draw.rect(win, block.c, (block.x * scale, block.y * scale, scale, scale))


def makePeice(peice):
    for i in range(4):
        blocks.append(Block(peice.x + R[peice.tipe][peice.r][i * 2], peice.y + R[peice.tipe][peice.r][i * 2 + 1], COLOR[peice.tipe]))
    

        

while run:
    #check for quit
    for event in game.event.get():
        if event.type == game.QUIT:
            run = False
    #
    #create new peice
    if newpeice:
        peices.append(Peice(0, gamex/2/scale, 4, 0))
        makePeice(peices[-1])
        #random.choice(bag)
        newpeice = False
    #display all peices
    for block in blocks:
        displayBlock(block)
    game.display.update()
    

    
game.quit()



