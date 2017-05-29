from tkinter import *
from beam import *

class Game:
    def __init__(self, gameWidth, gameHeight):
        self.root = Tk()
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.beam = beam(self.canvas, x=self.gameWidth / 2,y=self.gameHeight / 2, width=50, height=50, turnspeed=10)
        self.root.bind('<Left>', self.beam.rotate)
        self.root.bind('<Right>', self.beam.rotate)
        
        self.root.mainloop()

    def gameWindow(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)

        self.canvas = Canvas(self.frame,width=self.gameWidth, height=self.gameHeight, bg="purple", takefocus=1)
        self.canvas.pack(fill=BOTH, expand=YES)     

asteroids = Game(600,600)
