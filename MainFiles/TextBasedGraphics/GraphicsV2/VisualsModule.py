from random import gammavariate
import numpy as np

#Graphics() (class) is used for creating the default screen components such as the ScreenBorder() and DefaultScreen() functions.
class Graphics():
    def __init__(self, LOWER, PREFIX, BORDER, SCREENSIZE):
        self.LOWER = LOWER
        self.PREFIX = PREFIX
        self.BORDER = BORDER
        self.SCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = (SCREENSIZE*3)+2
        self.YSCREENSIZE = SCREENSIZE+2

    def RefreshBorder(self, gameVisuals):
        gameVisuals[0:self.XSCREENSIZE, 0] = "a"
        return gameVisuals
# AddShapes(Graphics) (sub-class) creates the different shapes in the governing gameVisuals Variable.
# AddShapes(Graphics) gets his input parameters from GameManager().
