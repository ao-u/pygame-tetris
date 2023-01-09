class Peice:
    def __init__(self, tipe, x, y, r, blocks):
        #type is taken :(
        self.tipe = tipe
        self.x = x
        self.y = y
        self.r = r
        self.blocks = [Block(0, 0, 0), Block(0, 0, 0), Block(0, 0, 0), Block(0, 0, 0)]

class Block:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c